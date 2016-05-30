@echo off&setlocal enabledelayedexpansion		rem 启用变量延迟

rem 进入selenium-sever的jar包所在目录
F:
cd BaiduYunDownload	

set iteration=5555	rem 设置延迟变量及通俗的迭代器

echo "正在启动hub节点，请稍后....."&ping -n 5 127.1 > nul
start /min cmd /c java -jar selenium-server-standalone-2.49.0.jar -role hub	rem 在一个新cmd窗口启动hub节点
echo "hub启动成功！"

echo "正在注册node节点，请稍后....."&ping -n 2 127.1 > nul
for /l %%i in (1,1,2) do (
rem 启动一个新的cmd窗口并执行注册节点命令
start /min cmd /c java -jar selenium-server-standalone-2.49.0.jar -role node -port !iteration! -hub  http://192.168.1.4:4444/grid/register/

set /a iteration=iteration+1

)
echo "node节点注册成功！"&ping -n 2 127.1 > nul



