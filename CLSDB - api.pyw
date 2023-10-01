from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from tcping import Ping
from functions import *
import os

#全局事件
global logo

if __name__ == '__main__':
	rtwnd = Tk()

	rtwnd.title('CLSDB建设与维护工具 - test vision')
	#rtwnd.geometry('700x500')
	rtwnd.resizable(0,0)
	rtwnd["background"] = "#C9C9C9"
	rtwnd.iconbitmap('favicon.ico')

	#菜单栏
	menu = Menu(rtwnd)

	#菜单>帮助
	mn_crowl = Menu(menu,tearoff = False)
	menu.add_cascade(label = '帮助',menu = mn_crowl)
	rtwnd.config(menu = menu)

	mn_crowl.add_command(label = '关于',command = About,accelerator = 'A')
	mn_crowl.add_separator()
	mn_crowl.add_command(label = '退出',command = rtwnd.quit)

	#在此添加新的菜单项

	#组件
	#左侧栏组件
	wnd_lft = Frame(rtwnd,background = '#D3D6C0',height = 10)
	wnd_lft.grid(row = 0,column = 0)

	fra_pth = Frame(wnd_lft)
	fra_pth.grid(row = 0,column = 0)
	lb_pth = Label(fra_pth,text = '路径',anchor = 'w',justify = 'left')
	lb_pth.grid(row = 0,column = 0)
	box_pth = Text(fra_pth,width = 30,height = 10)
	box_pth.grid(row = 1,column = 0)

	#pth = GetPth()

	# explorer = Frame(wnd_lft)
	# explorer.grid(row = 1,column = 0)

	txt_ctt = '内容 - [empty]'
	lb_ctt = Label(wnd_lft,text = txt_ctt,background = '#D3D6C0',anchor = 'w',justify = 'left')
	lb_ctt.grid(row = 2,column = 0)

	ctexplorer = Frame(wnd_lft)
	ctexplorer.grid(row = 3,column = 0)

	btdushboard = Frame(wnd_lft)
	btdushboard.grid(row = 4,column = 0)
	bt_sbmit = StdButton(btdushboard,'提交')
	bt_sbmit.grid(row = 0,column = 0)
	bt_chk = StdButton(btdushboard,'检查')
	bt_chk.grid(row = 0,column = 1)
	bt_edit = StdButton(btdushboard,'编辑')
	bt_edit.grid(row = 1,column = 0)
	bt_add = StdButton(btdushboard,'添加')
	bt_add.grid(row = 1,column = 1)

	bt_openfile = StdButton(wnd_lft,'打开目录',width = 21)
	bt_openfile.grid(row = 5,column = 0)

	#右侧栏组件
	wnd_rgt = Frame(rtwnd)
	wnd_rgt.grid(row = 0,column = 1)

	fra_dshbrd = Frame(wnd_rgt)
	fra_dshbrd.grid(row = 0,column = 0)

	logo = Image.open('logo.png')
	logo = logo.resize((100,100))
	logo = ImageTk.PhotoImage(logo)
	Logo = Label(fra_dshbrd,image = logo)
	Logo.grid(row = 0,column = 0)

	fra_tit = Frame(fra_dshbrd)
	fra_tit.grid(row = 0,column = 1)

	CLSDB_title = Label(fra_tit,text = '中国陆贝数据库',font = ('宋体','17'),justify = 'left',anchor = 'w')
	CLSDB_title.grid(row = 0,column = 0)

	CLSDB_en = Label(fra_tit,text = 'Chinese Landsnail Database',font = ('微软雅黑','10'),fg = '#999999')
	CLSDB_en.grid(row = 1,column = 0)

	CLSDB_frame = Frame(fra_tit)
	CLSDB_frame.grid(row = 2,column = 0)

	bt_opsite = Button(CLSDB_frame,borderwidth = 0,text = '打开网页',fg = 'blue',command = OpenWebSite,font = ('ms',10,'underline'))
	bt_opsite.grid(row = 0,column = 0)
	bt_opdsb = Button(CLSDB_frame,borderwidth = 0,text = '打开管理后台',fg = 'blue',command = OpenDashBoard,font = ('ms',10,'underline'))
	bt_opdsb.grid(row = 0,column = 1)

	lb_chkint = Label(fra_tit,text = '网络检查：NULL')
	lb_chkint.grid(row = 3,column = 0)

	Cho_frame = Frame(wnd_rgt)
	Cho_frame.grid(row = 1,column = 0)

	Cho_crowl = Frame(Cho_frame)
	Cho_crowl.grid(row = 0,column = 0)
	lb_crw = Label(Cho_crowl,text = '爬取')
	lb_crw.grid(row = 0,column = 0)

	crowl = StringVar()
	cb_crowl = ttk.Combobox(Cho_crowl,textvariable = crowl)
	cb_crowl['value'] = ('中国动物主题数据库')
	cb_crowl.current(0)
	cb_crowl.grid(row = 0,column = 1)

	Cho_dtbase = Frame(Cho_frame)
	Cho_dtbase.grid(row = 0,column = 1)
	lb_db = Label(Cho_dtbase,text = '数据库')
	lb_db.grid(row = 0,column = 0)

	dtbase = StringVar()
	cb_dtbase = ttk.Combobox(Cho_dtbase,textvariable = dtbase)
	cb_dtbase['value'] = ('Molluscabase')
	cb_dtbase.current(0)
	cb_dtbase.grid(row = 0,column = 1)


	fra_dw = Frame(wnd_rgt)
	fra_dw.grid(row = 2,column = 0)

	fra_sw = Frame(fra_dw)
	fra_sw.grid(row = 0,column = 0)

	fra_src = Frame(fra_sw)
	fra_src.grid(row = 0,column = 0)

	keyword = StringVar()
	ent_kwd = Entry(fra_src,exportselection = 0,justify = 'left',textvariable = keyword)
	ent_kwd.grid(row = 0,column = 0)

	bt_src = StdButton(fra_src,text = '检索')
	bt_src.grid(row = 0,column = 1)

	#此处放置下拉框
	
	res = '共 结果'
	lb_res = Label(fra_sw,text = res)
	lb_res.grid(row = 2,column = 0)

	fra_btzoon = Frame(fra_sw)
	fra_btzoon.grid(row = 3,column = 0)

	bt_new = StdButton(fra_btzoon,text = '+新建')
	bt_new.grid(row = 0,column = 0)

	bt_crowl = StdButton(fra_btzoon,text = '爬取')
	bt_crowl.grid(row = 0,column = 1)


	fra_se = Frame(fra_dw)
	fra_se.grid(row = 0,column = 1)

	lb_gwnl = Label(fra_se,text = '冈瓦纳拉英汉博物词典')
	lb_gwnl.grid(row = 0,column = 0)

	fra_src1 = Frame(fra_se)
	fra_src1.grid(row = 1,column = 0)

	keyword1 = StringVar()
	ent_kwd1 = Entry(fra_src1,exportselection = 0,justify = 'left',textvariable = keyword)
	ent_kwd1.grid(row = 0,column = 0)

	bt_src1 = StdButton(fra_src1,text = '检索')
	bt_src1.grid(row = 0,column = 1)

	#下拉结果
	cmd = StringVar()
	fra_cmd = Frame(fra_se)
	fra_cmd.grid(row = 2,column = 0)
	lb_cmd = Label(fra_cmd,text = '命令行',bg = None)
	lb_cmd.grid(row = 0,column = 0)
	ent_cmd = Entry(fra_cmd,textvariable = cmd)
	ent_cmd.grid(row = 0,column = 1)
	bt_cmd = StdButton(fra_cmd,text = '发送')
	bt_cmd.grid(row = 0,column = 2)

	rtwnd.mainloop()