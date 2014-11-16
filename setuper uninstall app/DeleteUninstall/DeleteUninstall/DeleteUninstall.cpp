// DeleteUninstall.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "DeleteUninstall.h"
#include "Shellapi.h"
#include "winbase.h"
#include "shlobj.h"

#define MAX_LOADSTRING 100

// Global Variables:

// Forward declarations of functions included in this code module:
int APIENTRY _tWinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPTSTR    lpCmdLine,
                     int       nCmdShow)
{
	// 删除uninstall.exe(快手版)
	int n=200;
	if (strlen(lpCmdLine)){
		do {
			if (DeleteFile(lpCmdLine)){
				break;
			}
			else{
				int nErrorCode=GetLastError();
				if (ERROR_FILE_NOT_FOUND == nErrorCode)
					break;
			}
			Sleep(10);
			n--;
		} while (n > 0);
	}

	SHELLEXECUTEINFO sei;  
	TCHAR szModule [MAX_PATH],szComspec[MAX_PATH],szParams [MAX_PATH];  
	//获取文件路径名  
	if((GetModuleFileName(0,szModule,MAX_PATH)!=0) &&  
		(GetShortPathName(szModule,szModule,MAX_PATH)!=0) &&  
		(GetEnvironmentVariable("COMSPEC",szComspec,MAX_PATH)!=0))  
	{  //设置命令行参数。  
		lstrcpy(szParams,"/c del ");  
		lstrcat(szParams, szModule);  
		lstrcat(szParams, " > nul");  

		//初始化SHELLEXECUTEINFO结构成员  
		sei.cbSize = sizeof(sei);//设置类型大小。  
		//命令窗口进程句柄，ShellExecuteEx函数执行时设置。  
		sei.hwnd = 0;  
		sei.lpVerb = "Open";//执行动作为“打开执行”。  
		sei.lpFile = szComspec;      //执行程序文件全路径名称。  
		sei.lpParameters = szParams; //执行参数。  
		sei.lpDirectory = 0;  
		//显示方式，此处使用隐藏方式阻止出现命令窗口界面。  
		sei.nShow = SW_HIDE;  
		//设置为SellExecuteEx函数结束后进程退出。  
		sei.fMask = SEE_MASK_NOCLOSEPROCESS;  
		//创建执行命令窗口进程。  
		if(ShellExecuteEx(&sei))  
		{  //设置命令行进程的执行级别为空闲执行,这使本程序有足够的时间从内存中退出。    
			SetPriorityClass(sei.hProcess,IDLE_PRIORITY_CLASS);  
			//设置本程序进程的执行级别为实时执行，这本程序马上获取CPU执行权，快速退出。    
			SetPriorityClass(GetCurrentProcess(),REALTIME_PRIORITY_CLASS);  
			SetThreadPriority(GetCurrentThread(),THREAD_PRIORITY_TIME_CRITICAL);    
			//通知Windows资源浏览器，本程序文件已经被删除。  
			SHChangeNotify(SHCNE_DELETE,SHCNF_PATH,szModule,0);  
			//执行退出程序  
			//EndDialog(0);  
		} 
	}
}



