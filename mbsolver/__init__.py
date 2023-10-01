import basicwebsolver as solv
from bs4 import BeautifulSoup as BS

##########注意，该库只进行了最基础的开发###########

#mb搜索：若结果匹配，直接进入条目；否则停留于结果页
def SearchInMB(keyword):
        htmcode = solv.GetHTMLText('https://molluscabase.org/aphia.php?p=taxlist&tid=-1&tName='+keyword+'&searchpar=0&tComp=begins&action=search&rSkips=0')
        soup = BS(htmcode,features = 'html.parser')
        if soup.title.string == 'Molluscabase':
                #物种页的标题不是Molluscabase,而是Molluscabase + 拉丁
                #此种情况只能是搜索页
                return -1 #错误码-1：该物种没有条目
                #到现在仍未考虑搜索结果分离问题，因为貌似没必要
        return htmcode

#解决无法进入的方法：进入第一个url
def GetSrRes(keyword):
        htmcode = solv.GetHTMLText('https://molluscabase.org/aphia.php?p=taxlist&tid=-1&tName='+keyword+'&searchpar=0&tComp=begins&action=search&rSkips=0')
        soup = BS(htmcode,features = 'html.parser')
        res = soup.find_all('li',{'class':'list-group-item'})
        ret = []
        for i in res:
                bot = BS(str(i),features = 'html.parser')
                lnk = bot.a.attrs
                ret.append(['https://molluscabase.org/'+lnk['href'],bot.text])
        return ret
#为多参数函数检查参数的函数
def Chk(keyword,url):
        mode = [0,0]
        if keyword:
                mode[0]=1
        if url:
                mode[1]=1
        #若同时给出两参数，则判定为错误
        if mode[0]+mode[1] == 2:
                return -1
        #若未给定参数，则判定为错误
        if mode[0]+mode[1] ==0:
                return -2
        return mode

#爬取拉丁学名
def GetName(keyword,url):
        chk = Chk(keyword,url)
        try:
                if chk <0:
                        return chk
        except:
                if chk[0] == 1:
                        soup = BS(SearchInMB(keyword),features = 'html.parser')
                elif chk[1] == 1:
                        soup = BS(solv.GetHTMLText(url),features = 'html.parser')
        nm0 = soup.find('h3',{'class':'aphia_core_header-inline'})
        #此处还包含一切分类信息
        
        nm1 = nm0.b
        nm2 = nm1.find_all('i')
        nm3 = BS(str(nm2[1]),features = 'html.parser')#分离
        name1 = nm1.string#不知道为啥，bs卡bug,<i/>标签后面的文本读不出来
        name2 = nm3.string
        return nm1.text

def GetStatus(keyword,url):
        chk = Chk(keyword,url)
        try:
                if chk <0:
                        return chk
        except:
                if chk[0] == 1:
                        try:
                                soup = BS(SearchInMB(keyword),features = 'html.parser')
                        except:
                                #return 'Unsupported!'
                                res = GetSrRes(keyword)
                                soup = BS(solv.GetHTMLText(res[0][0]),features = 'html.parser')
                elif chk[1] == 1:
                        try:
                                soup = BS(solv.GetHTMLText(url),features = 'html.parser')
                        except:
                                return 'Unknown error!'
        st0 = soup.find('div',{'id':'Status','class':'col-xs-12 col-sm-8 col-lg-10'})
        st1 = st0.font
        status = st1.text
        return status
