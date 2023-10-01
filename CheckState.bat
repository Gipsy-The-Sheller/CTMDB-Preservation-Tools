title Restart...
mode con:cols=50 lines=20
echo off
cls
color f0
echo 爬取内容默认输出到result.csv。现在按任意键开始爬取。
pause
title CheckingState...
python CheckState.py
echo 爬取完毕
title Checking Completed.
pause
start excel results.csv
exit