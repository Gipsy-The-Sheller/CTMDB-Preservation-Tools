from tkinter import *
from tkinter import messagebox
import pyperclip
import wpformat as wp

rootwnd = Tk()
#窗体大小与位置
rootwnd.geometry('370x400+300+150')
#窗体标题
rootwnd.title('CLSDB条目快速组织工具v0.1.0 for test')

#科
labelf = Label(rootwnd,
               text = '中文科名：',
               font = ('15')
               )
labelf.grid(row = 0,column = 1)
entryf = Entry(rootwnd,
               font = ('YaHei','15'))
entryf.grid(row = 0,column = 2)
#Lt
labelflt = Label(rootwnd,
               text = '拉丁科名：',
               font = ('15'))
labelflt.grid(row = 1,column = 1)
entryflt = Entry(rootwnd,
               font = ('YaHei','15'))
entryflt.grid(row = 1,column = 2)

#属
labelg = Label(rootwnd,
               text = '中文属名：',
               font = ('15'))
labelg.grid(row = 2,column = 1)
entryg = Entry(rootwnd,
               font = ('YaHei','15'))
entryg.grid(row = 2,column = 2)

#Lt
labelglt = Label(rootwnd,
               text = '拉丁属名：',
               font = ('15'))
labelglt.grid(row = 3,column = 1)
entryglt = Entry(rootwnd,
               font = ('YaHei','15'))
entryglt.grid(row = 3,column = 2)
#拉丁学名
label1 = Label(rootwnd,
               text = '拉丁学名：',
               font = ('15'))
label1.grid(row = 4,column = 1)
entry1 = Entry(rootwnd,
               font = ('YaHei','15'))
entry1.grid(row = 4,column = 2)

#中文正名
label2 = Label(rootwnd,
               text = '中文正名：',
               font = ('15'))
label2.grid(row = 5,column = 1)
entry2 = Entry(rootwnd,
               font = ('YaHei','15'))
entry2.grid(row = 5,column = 2)

#描述
label3 = Label(rootwnd,
               text = '描述：',
               font = ('15'))
label3.grid(row = 6,column = 1)
entry3 = Entry(rootwnd,
               font = ('YaHei','15'))
entry3.grid(row = 6,column = 2)

#出处
label4 = Label(rootwnd,
               text = '出处：',
               font = ('15'))
label4.grid(row = 7,column = 1)
entry4 = Entry(rootwnd,
               font = ('YaHei','15'))
entry4.grid(row = 7,column = 2)

#原始文献
label5 = Label(rootwnd,
               text = '原始文献：',
               font = ('15'))
label5.grid(row = 8,column = 1)
entry5 = Entry(rootwnd,
               font = ('YaHei','15'))
entry5.grid(row = 8,column = 2)

#原始文献URL
label6 = Label(rootwnd,
               text = '原始文献URL：',
               font = ('15'))
label6.grid(row = 9,column = 1)
entry6 = Entry(rootwnd,
               font = ('YaHei','15'))
entry6.grid(row = 9,column = 2)

#产地
label7 = Label(rootwnd,
               text = '产地：',
               font = ('15'))
label7.grid(row = 10,column = 1)
entry7 = Entry(rootwnd,
               font = ('YaHei','15'))
entry7.grid(row = 10,column = 2)

#模式产地
##原始文献URL
label8 = Label(rootwnd,
               text = '模式产地：',
               font = ('15'))
label8.grid(row = 11,column = 1)
entry8 = Entry(rootwnd,
               font = ('YaHei','15'))
entry8.grid(row = 11,column = 2)



def buttcmd():
	LtFam  = entryflt.get()
	ChFam  = entryf.get()
	LtGen  = entryglt.get()
	ChGen  = entryg.get()
	LtName = entry1.get()
	ChName = entry2.get()
	Desc   = entry3.get()
	Book   = entry4.get()
	Orig   = entry5.get()
	OrigURL= entry6.get()
	Loc    = entry7.get()
	TpLoc  = entry8.get()
	pyperclip.copy(wp.OrgTheEntry(ChFam = ChFam,LtFam = LtFam,ChGen = ChGen,LtGen = LtGen,LtName = LtName,ChName = ChName,Desc = Desc,
		Book = Book,Orig = Orig,OrigURL = OrigURL,Loc = Loc,TpLoc =TpLoc))
	messagebox.showinfo('消息 - CLSDB条目快速组织工具v0.1.0','已复制至剪贴板。请直接于模块编辑器中粘贴。')




butt_org = Button(rootwnd,
               borderwidth = 1,
               text = '快速组织至剪贴板',
               width = 15,
               font = ('YaHei','15'),
               command = buttcmd)
butt_org.grid(row = 12,column = 2)

mainloop()