import SuEnt
import easygui as api
import especiessolver as es
import os
import re
import wpformat as wp

version = 'v0.1.0 for test'

def Menu(default):
    choice = api.choicebox(msg='选择模式',
                           title = '菜单 - 中国动物主题数据库 爬取工具',
                           choices = ('1.默认','2.单行URL','3.读取URL列表','4.编辑URL列表','5.关键词爬取','6.设置','7.关于'))
    try:
        return int(choice.split('.')[0])
    except:
        return -1

def About(version):
    api.msgbox(msg = '中国动物主题数据库 数据爬取器'+version+'\n为高效建站而生\n开发者：gipsy@CLSDB\n任意事宜请联系1274103602@qq.com\n',
               title = '关于 - 中国动物主题数据库 爬取工具',
               ok_button = '确认')
    
def settings():
    sets = api.multchoicebox(msg = '点击以开启/关闭功能，全选为默认值',title = '设置 - 中国动物主题数据库',
                             choices = ('1.默认为单行URL，关闭后变为默认关键词','2.数据自动存剪贴板','3.默认完成时打开表格',
                                        '4.本次运行完成时打开表格','5.默认显示爬取结果','6.默认输出至results.csv，关闭变为results.txt'))
    sts = []
    for i in sets:
        bottle = i.split('.')
        sts.append(bottle[0])
    return sts

def SngCr():
    urls = api.enterbox(msg = '输入URL，若要输入多个，请用英文半角;隔开',title = '中国动物主题数据库 单行URL爬取',strip = True)
    if not(urls) or urls == '':
        return -1
    urls = urls.split(';')
    res = []
    for i in urls:
        try:
            sng = es.GetTheInf(i)
        except Exception as e:
            api.msgbox(msg = '错误'+str(e),title = '错误 - 中国动物主题数据库',ok_button = '确认')
            return -1 #错误码-1：参数错误
        res.append(sng)
    
    #注意：此段需后续DEBUG!:show
    return res

def SngSch():
    keys = api.enterbox(msg = '输入关键词，若要输入多个，请用英文半角;隔开',title = '中国动物主题数据库 关键词爬取',strip = True)
    try:
        keys = keys.split(';')
    except:
        keys = [keys]
    if keys == [None] or keys == ['']:
        return -1
    res = []
    ret = []
    cont = []
    for i in keys:
        try:
            sng = es.SearchInEs(i)
        except Exception as e:
            api.msgbox(msg = '错误'+str(e),title = '错误 - 中国动物主题数据库 爬取工具',ok_button = '确认')
            return -1
        num = 1
        for j in sng:
            cont.append(j)
            ret.append(str(num)+'.'+j[1]+j[0])
            num+=1
    ans = api.multchoicebox(msg = '选择需要爬取的条目，多选',title = '选择 - 中国动物主题数据库 爬取工具',choices = tuple(ret))
    for i in ans:
        # uplod = i.split('.')
        # num = int(uplod[0])
        # print(cont[num][0])
        # cbk = es.GetTheInf(cont[num-1][0])
        # print(cbk)
        try:
            uplod = i.split('.')
            num = int(uplod[0])
            cbk = es.GetTheInf(cont[num-1][0])
        except Exception as e:
            api.msgbox(msg = '错误'+str(e),title = '错误 - 中国动物主题数据库 爬取工具',ok_button = '确认')
            continue
        res.append(cbk)
    return res

def ShowPatchResults(inf):
    try:
        pic = ''
        for i in inf[5]:
            pic += i + '\n'
        SuEnt.NewEntry(title = str(inf[2]),content = wp.OrgTheEntry(None,None,None,None,str(inf[0]),str(inf[2]),str(inf[3]),str(inf[4])))
        choi = api.textbox(msg = '在此进行复制与校验，点击“确定”进入下一条，点击“取消”退出',
            title = '爬取结果 - 中国动物主题数据库 爬取工具',
            text = '拉丁学名：\n'+inf[0]+' '+inf[1]+'\n中文正名：\n'+inf[2]+'\n描述：\n'+inf[3]+'\n出处：\n'+inf[4]+'\n媒体：\n'+pic,codebox = False)
            #text = '拉丁学名：\n'+inf[0]+'\n描述：\n'+inf[1]+'\n出处：\n'+inf[2]+'\n媒体：\n'+inf[3],codebox = False
#       csv = open('data/results.csv','a')
 #       try:
  #          for i in re.split('[\n]',choi):
   #             csv.writelines(i+',')
    #    except:
     #       api.msgbox('错误：写入错误','错误',ok_button ='下一项/退出')"""
        #csv.close()
            #############################
        if choi == None:
            return -1 #取消键
        elif choi == '' or choi:
            return 0
        else:
            api.msgbox(msg = 'SPR01:Unknown Error!',title = '错误 - 中国动物主题数据库 爬取工具',ok_button = '退出') 
    except:
        api.msgbox(msg = 'SPR02:Unknown Error!',title = '错误 - 中国动物主题数据库 爬取工具',ok_button = '退出')
        return -1001

def OutputSets(sets):
    try:
        os.mkdir('data')
        os.system('cd data')
    except:
        os.system('cd data')
    filename = 'settings.ini'
    ini = open('data/'+filename,'w')
    if sets == ''or sets == None:
        return -1
    for i in sets:
        if i != '0':
            sets[int(i)-1] = '1'
    for i in sets:
        ini.write(i+' ')

def InputSets():
    try:
        os.cd('data')
        filename = 'settings.ini'
        ini = open('data/'+filename,'r')
        sets = ini.read().split()
        return sets
    except:
        return [1,1,1,1,1]
if __name__ == '__main__':
    
    #const

    Sets = InputSets()

    flag = True

    csv = open('data/results.csv','w')
    csv.write('')
    csv.close()
    while flag:
        choice = Menu(Sets)
        if choice == 1:
            if Sets[0] == 1:
                res = SngCr()
                if res == -1:
                    flag = False
                else:
                    for i in res:
                        cbk = ShowPatchResults(i)
                        if cbk == -1:
                            break
                        if cbk == -1001:
                            break
            elif Sets[0] == 0:
                res = SngSch()
                if res == -1:
                    flag = False
                else:
                    for i in res:
                        cbk = ShowPatchResults(i)
                        if cbk == -1:
                            break
                        # if cbk == -1001:
                        #     break
        elif choice == 2:
            res = SngCr()
            if res == -1:
                flag = False
            else:
                for i in res:
                    cbk = ShowPatchResults(i)
                    if cbk == -1:
                        break
                    if cbk == -1001:
                        break
        elif choice == 5:
            res = SngSch()
            if res == -1:
                flag = False
            else:
                for i in res:
                    cbk = ShowPatchResults(i)
                    if cbk == -1:
                        break
            # if cbk == -1001:
            #     break  
        elif choice == 4:
            api.msgbox(msg = '暂未完成',title = '错误 - 中国动物主题数据库 爬取工具',ok_button = '退出')
        elif choice == 3:
            api.msgbox(msg = '暂未完成',title = '错误 - 中国动物主题数据库 爬取工具',ok_button = '退出')
        elif choice == 6:
            Sets = settings()
            OutputSets(Sets)
        elif choice == 7:
            About('v0.1.0 for test')
        break
