title Restart...
mode con:cols=50 lines=20
echo off
cls
color f0
echo ��ȡ����Ĭ�������result.csv�����ڰ��������ʼ��ȡ��
pause
title CheckingState...
python CheckState.py
echo ��ȡ���
title Checking Completed.
pause
start excel results.csv
exit