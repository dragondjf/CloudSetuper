local json = require 'json'
local argparse = require "argparse"

local function exists(name)
    if type(name)~="string" then return false end
    return os.rename(name,name) and true or false
end


local function isFile(name)
    if type(name)~="string" then return false end
    if not exists(name) then return false end
    local f = io.open(name)
    if f then
        f:close()
        return true
    end
    return false
end


local function isDir(name)
    return (exists(name) and not isFile(name))
end


local function readfile( fileName )
    local f = io.open(fileName,'rb')
    local content = f:read("*all")
    f:close()
    return content
end

local function writefile(fileName, content)
    local f = io.open(fileName,'wb')
    f:write(content)
    f:close()
end


local function file_exists(path)
  local file = io.open(path, "rb")
  if file then file:close() end
  return file ~= nil
end


local function length_of_file(filename)
  local fh = io.open(filename, "rb")
  local len = fh:seek("end")
  fh:close()
  return len
end

local function sortSize(a, b)
    return a.size < b.size
end


function generatePackageJson(package)
    -- body
    local jsonpath = package.."\\".."package.json"
    if not file_exists(jsonpath) then
        return nil
    end
    local content = readfile(jsonpath)
    local len = length_of_file(jsonpath)
    local packagejson = json.decode(content)
    for key, file in pairs(packagejson['files']) do
        for k,v in pairs(file) do
            if k == "path" then
                local flen
                if file_exists(v) then
                    flen = length_of_file(v)
                else
                    local fpath = package.."\\"..v
                    if file_exists(fpath) then
                        flen = length_of_file(fpath)
                    end
                end
                file['size'] = flen
            end
        end
    end

    table.sort(packagejson['files'], sortSize)

    local ppt_order = {}
    for i=1, #packagejson['files'] - 1 do
        local name = packagejson['files'][i]['name']
        ppt_order[i] = name
    end

    packagejson['ppt_order'] = ppt_order

    return packagejson
end

function generateParse( ... )
    -- body
    local parser = argparse()
       :description "An example."
    parser:option "-p" "--package"
       :default "package"
       :description "files in pacakge append to exe"
    parser:option "-t" "--template"
       :default "InstallerUI.exe"
       :description "install ui template exe"
    parser:option "-o" "--output"
       :default "output.exe"
       :description "output exe name"
    local args = parser:parse()
    return args, parser
end

local args, parser = generateParse()
local packagepath = args['package']
local packagejson = generatePackageJson(packagepath)

function copyFile2Exe( ... )
    -- body
    local content = readfile(args['template'])
    for key, file in pairs(packagejson['files']) do
        for k, v in pairs(file) do
            if k == "path" then
                local fcontent
                if file_exists(v) then
                    fcontent = readfile(v)
                else
                    local fpath = args['package'].."\\"..v
                    if file_exists(fpath) then
                        fcontent = readfile(fpath)
                    end
                end
                content = content..fcontent
            end
        end
    end
    local config = json.encode(packagejson)
    content = content..config.."|"..#(config)
    local outputPath = args['package'].."\\"..args['output']
    writefile(outputPath, content)
end

if isDir(packagepath) then
    copyFile2Exe()
else
    print(parser:get_help())
end
