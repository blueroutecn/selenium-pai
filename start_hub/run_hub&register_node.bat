@echo off&setlocal enabledelayedexpansion		rem ���ñ����ӳ�

rem ����selenium-sever��jar������Ŀ¼
F:
cd BaiduYunDownload	

set iteration=5555	rem �����ӳٱ�����ͨ�׵ĵ�����

echo "��������hub�ڵ㣬���Ժ�....."&ping -n 5 127.1 > nul
start /min cmd /c java -jar selenium-server-standalone-2.49.0.jar -role hub	rem ��һ����cmd��������hub�ڵ�
echo "hub�����ɹ���"

echo "����ע��node�ڵ㣬���Ժ�....."&ping -n 2 127.1 > nul
for /l %%i in (1,1,2) do (
rem ����һ���µ�cmd���ڲ�ִ��ע��ڵ�����
start /min cmd /c java -jar selenium-server-standalone-2.49.0.jar -role node -port !iteration! -hub  http://192.168.1.4:4444/grid/register/

set /a iteration=iteration+1

)
echo "node�ڵ�ע��ɹ���"&ping -n 2 127.1 > nul



