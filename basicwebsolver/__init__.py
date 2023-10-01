import requests as req
from bs4 import BeautifulSoup as BS
import re
import easygui


def GetHTMLText(url):
    try:
        r = req.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return -1   #错误码-1：爬取错误

def GetCsvText(FileName):
    csvfile = open(FileName + '.csv','r')
    ls = []
    lns = []
    i = 0
    for line in csvfile:
        line = line.replace('\n',' ')
        ls = line.split(',')
        lns[i] = [ ]
        j = 0
        for s in ls:
            lns[i][j] = s
            j+=1
        i+=1

    return lns


