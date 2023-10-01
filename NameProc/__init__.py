import re

#该功能只能断句最最基本的属名+种名并以长度为2的列表返回
def SplitLartinName(name):
    splt = re.split('[ ()\xa0]',name)
    return splt[0:2]