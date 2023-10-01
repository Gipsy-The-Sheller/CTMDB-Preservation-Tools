from tkinter import *
from tkinter import messagebox
rootwnd = Tk()

'''
anchor
'''

def buttcmd():
    messagebox.showinfo('1','1')

#窗体大小与位置
rootwnd.geometry('600x400+300+150')
#窗体标题
rootwnd.title('tool v1.0')

#控件：Label
#background:'#rrggbb','<color>','SystemHighLight'
label1 = Label(rootwnd,
               background = 'SystemHighLight',
               text = '1',
               font = ('楷体','15'),
               fg = '#ff00ff')
label1.grid(row = 0,column = 1)
#label1.pack(side = RIGHT)

#控件：Entry
entry1 = Entry(rootwnd,
               font = ('YaHei','15'),
               fg = 'red')
entry1.grid(row = 1,column = 2)

#控件：Button
#relief = RIDGE:棱台
butt1 = Button(rootwnd,
               borderwidth = 1,
               text = '111',
               width = 15,
               font = ('YaHei','15'),
               fg = 'green',
               command = buttcmd)
butt1.grid(row = 1,column = 3)

rootwnd.mainloop()