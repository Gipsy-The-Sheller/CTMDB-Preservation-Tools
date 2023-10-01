import wx
class ChkFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent.id,title = 'CLSDB 校验器',
                          pos = (150,250),size = (500,400))
        
    panel = wx.Panel(self)
    
    self.bt_start = wx.Button(panel,label = '开始爬取')
    self.bt_stop  = wx.Button(panel,label = '停止爬取')
    self.bt_last  = wx.Button(panel,label = '上一项')
    self.bt_next  = wx.Button(panel,label = '下一项')
    self.bt_csv   = wx.Button(panel,label = '打开表格')
    self.bt_about = wx.Button(panel,label = '关于')
    
    self.et_LtName = wx.TextCtrl(panel,style = wx.TE_LEFT)
    self.bt_ser    = wx.Button(panel,label = '查找')
    
    self.txt_current = wx.StaticText(panel,label = '[None]')
    self.txt_prog0   = wx.StaticText(panel,label = '进度：')
    self.txt_prog1   = wx.StaticText(panel,label = '----------   %')
    self.txt_log0    = wx.StaticText(panel,label = '日志')
    self.txt_log1    = wx.StaticText(panel,label = '加载成功...')
    
    wndsz_button12 = wx.BoxSizer(wx.HORIZONTAL)
    wndsz_button12.Add(self.bt_start,proportion = 1,flag = wx.ALL,border = 15)
    wndsz_button12.Add(self.bt_stop ,proportion = 1,flag = wx.ALL,border = 15)
    
    wndsz_button34 = wx.BoxSizer(wx.HORIZONTAL)
    wndsz_button34.Add(self.bt_last,proportion = 1,flag = wx.ALL,border = 15)
    wndsz_button34.Add(self.bt_next,proportion = 1,flag = wx.ALL,border = 15)
    
    wndsz_button56 = wx.BoxSizer(wx.HORIZONTAL)
    wndsz_button56.Add(self.bt_csv  ,proportion = 1,flag = wx.ALL,border = 15)
    wndsz_button56.Add(self.bt_about,proportion = 1,flag = wx.ALL,border = 15)
    
    wndsz_search = wx.BoxSizer(wx.HORIZONTAL)
    wndsz_search.Add(self.bt_start,proportion = 1,flag = wx.ALL,border = 15)
    wndsz_search.Add(self.bt_start,proportion = 1,flag = wx.ALL,border = 15)