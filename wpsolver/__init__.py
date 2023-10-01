import basicwebsolver as solv
import mbsolver as MB
import requests as req
from bs4 import BeautifulSoup as BS
import warnings
import NameProc
import re

def GetXML():
    Code = req.get('https://xoi.home.blog/sitemap.xml')
    return Code.text

global XML
XML = GetXML()

def GetLocate():
    with warnings.catch_warnings():#消除使用html.parser产生的警告
        warnings.simplefilter('ignore')
        soup = BS(XML,features = 'html.parser')
    lst = soup.find_all('loc')
    ls = []
    for i in lst:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            sp = BS(str(i),features = 'html.parser')
        ls.append(sp.string)
    return ls

#尚未开发网站中搜索
def GetName(url):
    htm = solv.GetHTMLText(url)
    try:
        soup = BS(str(htm),features = 'html.parser')
    except:
        return -1
    table = soup.find('div',{'class':'entry-content'}).table
    td = table.find_all('td')
    name = BS(str(td[1]),'html.parser').text
    return str(name)

def ChkState():
    lst = GetLocate()
    ls = [ ]
    csv = open('results.csv','a')
    csv.write('---分割线---\n')
    csv.close()
    for i in range(len(lst)):
        csv = open('results.csv','a')
        print('--- --- ---',end = '')
        try:
            name = GetName(lst[i])
            name = NameProc.SplitLartinName(name)
            print('\r>>>',end = ' ')
        except:
            print('\r--- --- --- 错误：无法访问CLSDB！')
            continue
        try:
            Lt = name
            print('>>>',end = ' ')
        except:
            print('--- --- 错误：拉丁名不纯净！')
            continue
        try:
            state = MB.GetStatus(Lt[0]+' '+Lt[1],'')
            print('>>>',end = '\n')
        except:
            print('--- 错误：无法访问MB的相应页面！')
            state = 'Error:MBPage Not Found!'
        try:
            csv.writelines(Lt[0]+' '+Lt[1]+','+(state)+','+(lst[i])+'\n')
            ls.append([name,Lt[0],Lt[1],state,lst[i]])
        except Exception as e:
            print('错误：',e)
            print(name)
            #csv.writelines((name)+','+'gbk Error\n')#+','+(state)+','+(lst[i])+'\n')
        csv.close()
    return ls
