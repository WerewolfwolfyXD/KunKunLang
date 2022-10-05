import time
import tkinter.messagebox
from tkinter import Tk, Menu, Text

from win32ctypes import win32api
from win32ctypes import *

import tk_extended
from tk_extended import *

# # Load Language
# langpack_file = open("lang/zh_cn", "r+")
# langpack = langpack_file.read()
# class LiteralText:
#     def format(info):
#         return langpack[info]
# print("语言包已加载: "+langpack_file.name.__str__())
# a = LiteralText.format(0)


# applet here
applet = Tk()
global p_dev, width, height, win_width, win_height
p_dev=""
width = applet.winfo_screenwidth()
height = applet.winfo_screenheight()
win_width = 1024
win_height = 800
geometry_sizeof = '%dx%d+%d+%d' % (win_width, win_height, (width-win_width)/2, (height-win_height)/2)

if PROGRAM_DEVSTATUS: p_dev = " (Dev)"
bfe.applet.applet_title(applet, PROGRAM_NAME+" "+PROGRAM_VERSION+" Shell" + p_dev)

applet.geometry(geometry_sizeof)
bfe.applet.window.refreshTheme(applet, "white")



def menuCommand() :
    applet.messagebox.showinfo("PULL", "")
mm = Menu (applet)
filemenu = Menu(mm, tearoff=False)
filemenu.add_separator()
filemenu.add_command(label="退出",command=applet.quit)
applet.config(menu=mm)

text =Text(applet, width=win_width, heigh=win_height - win_height + 20)
text.pack()

ter =Text(applet, width=win_width, heigh=win_height - 20)
ter.pack()

def runonshell():
    comptime = time.time()
    codes = text.get("1.0", "1.end")
    ter.delete("1.0", "end")
    ter.insert("end", PROGRAM_NAME+" "+PROGRAM_VERSION+" "+PROGRAM_DEVSTATUS.__str__()+" | compilete time:"+(time.time() - comptime).__str__()+"\n")
    code_out = tk_extended.bf_ext.bf_formatter(tk_extended.bf_ext.kk(codes))
    ter.insert("end", "\nBF# > "+code_out)
    tkinter.messagebox.showinfo("坤坤编译器", "编译用时"+(time.time() - comptime).__str__()+"s"+"\n"+"编译结果："+code_out)



mm_debugger_menu = Menu(mm, tearoff=False)
mm_debugger_menu.add_command(label="在本地Shell调试",command=runonshell, accelerator="F5")
mm.add_cascade(label="调试",menu=mm_debugger_menu)
applet.bind("<F5>", runonshell())

applet.mainloop()
