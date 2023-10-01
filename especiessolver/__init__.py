import basicwebsolver as solv
from bs4 import BeautifulSoup as BS

#爬取拉丁学名
def GetLTName(url):
    htmcode = solv.GetHTMLText(url)
    soup = BS(htmcode,features="html.parser")
    #beginn = soup.find('div',{'id':'app'})
    #beg2 = soup.find('div',{'class':'row'})
    beg3 = soup.find('div',{'class':'col-md-8'})
    #beg4 = beg3.h2
    #name = beg4.string
    name = beg3.i.string
    return name

#爬取命名者与标记
def GetTG(url):
    htmcode = solv.GetHTMLText(url)
    soup = BS(htmcode,features="html.parser")
    #beginn = soup.find('div',{'id':'app'})
    #beg2 = soup.find('div',{'class':'row'})
    beg3 = soup.find('div',{'class':'col-md-8'})
    beg4 = beg3.find('font',{'color':'#OFOFOF','size':'5'})
    beg4 = BS(str(beg4),features ="html.parser")
    tags = beg4.text
    return tags

#爬取正名
def GetZHName(url):
    htmcode = solv.GetHTMLText(url)
    soup = BS(htmcode,features="html.parser")
    #beginn = soup.find('div',{'id':'app'})
    #beg2 = soup.find('div',{'class':'row'})
    beg3 = soup.find('div',{'class':'col-md-8'})
    beg4 = beg3.h2
    name = beg4.string
    return name

#爬取描述信息
def GetScrpt(url):
    htmcode = solv.GetHTMLText(url)
    soup = BS(htmcode,features="html.parser")
    des0 = soup.find('div',{'style':'padding-left:2em; padding-right:2em; line-height:30px; font-size: 17px;'})
    desc = des0.text
    return desc

#爬取原文
def GetSrc(url):
    htmcode = solv.GetHTMLText(url)
    soup = BS(htmcode,features="html.parser")
    bk0 = soup.find('div',{'class':'col-md-11 col-xs-11 col-sm-11'})
    bk = bk0.text
    return bk

#爬取媒体地址
def GetImg(url):
    htmcode = solv.GetHTMLText(url)
    soup = BS(htmcode,features="html.parser")
    img0 = soup.find('div',{'class':'tab-pane fade','id':'multimedia'})
    try:
        img1 = img0.find('div',{'align':'right'})
        imglist = img1.find_all('a')
    except:
        return 'No images.'
    lst = []
    i = 0
    while True:
        try:
            a = BS(str(imglist[i]),features="html.parser")
        except IndexError:
            break
        a = a.a.attrs#第一个a是变量，第二个a是变量中存储的第一个<a>标签
        im = 'http://zoology.especies.cn'+a['href']
        lst.append(im)
        # try:
        #     test = imglist[i+1]
        # except:
        #     break
        i+=1
    '''
    for i in imglist:
        img0 = soup(i,features = 'html.phaser').find('a')
        a = img0.attrs
        im = a['href']
        lst.append(im)
    '''
    return lst
    
#总函数，返回列表
def GetTheInf(url):
    name = GetLTName(url)
    tag = GetTG(url)
    ZHName = GetZHName(url)
    Scr = GetScrpt(url)
    Src = GetSrc(url)
    img = GetImg(url)
    return [name,tag,ZHName,Scr,Src,img]

#一个美好的设想：自动搜索
##############该功能待完善##############

#搜索，返回htm代码列表。目前不支持换页
def SearchInEs(keyword):
    res = []
    for num in range(0,7):
        htmcode = solv.GetHTMLText('http://zoology.especies.cn/search/wordall?offset='+str(num*10)+'&search='+keyword)
        soup = BS(htmcode,features ='html.parser')
        lst = soup.find_all('div',{'class':'panel panel-default'})
        i = 0
        while True:
            a = BS(str(lst[i]),features="html.parser")
            a = a.a
            im = 'http://zoology.especies.cn'+a['href']
            fnt = a.font.string
            ti = a.i.font.string
            if ti and fnt:
                res.append([im,str(fnt)+str(ti)])
            elif ti:
                res.append([im,str(ti)])
            elif fnt:
                res.append([im,str(fnt)])
            try:
                test = lst[i+1]
            except:
                break
            i+=1
        num += 10
    return res
#返回格式：一级列表：[二级列表：[链接，名称],二级列表：[链接，名称]]