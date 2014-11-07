Clound Setuper 运行手册
========================
1. 下载monogdb
    http://www.mongodb.org/downloads
    按照自己操作系统下载相应的版本
    + windows
    首先在E盘创建一个这样的目录结构【E:\mongodb\data\db】和【E:\mongodb\data\log】
    +       
        
            cd CloudSetuper/windows
            mongod -f  mongodb.conf

    这样启动mongdb server

2. 安装python

    + 安装python2.7.8 https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi 

    + 安装pip http://www.jsxubar.info/install-pip.html

    + 安装mongokit  pip install mongokit

    + 运行server  python main.py

    在浏览器中输入 `localhost` 即可







