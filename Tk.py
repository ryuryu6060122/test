#tkinkerの使い方

import sys
import tkinter as tk
import tkinter.messagebox as tkm


#画面
win = tk.Tk()
win.title(u'test')    #タイトル
win.geometry("1080x800")    #半角英のx
                 #max1080x2000


#ラベル
Static1 = tk.Label(text = u'!!entry!!', foreground = '#ffffff', background = '#90caf9')
Static1.pack() #自動で要素を配置
#Static1.place(x=480, y=120)


#テキストボックス
Entry1 = tk.Entry(width = 30)
Entry1.insert(tk.END, u'挿入する文字列')
Entry1.pack()

Entry1.delete(0, tk.END)


#ボタンの関数
def eraseEntry():
	Entry1.delete(first = 0, last = 100)

def destroyEntry():
	Entry1.destroy()

def destroyTk():
	win.destroy()
	

#ダイアログの関数
def msgbox(text):
	tkm.showinfo('info', text)


#リストの関数
def addlist(text):
	Listbox1.insert(tk.END, text)

def deleteList():
	SelectedIndex = tk.ACTIVE   #選択されてるリストの番号
	Listbox1.delete(SelectedIndex) #delete(selectedIndex)関数


#操作系
Button1 = tk.Button(text = u'erase', width = 10, command = eraseEntry)
Button1.pack()

Button2 = tk.Button(text = u'destroy', width = 10, command = destroyEntry)
Button2.pack()

Button3 = tk.Button(text = u'quit', width = 10, command = destroyTk)
Button3.pack()


Button4 = tk.Button(text = u'msgbox', width = 10, command = lambda : msgbox(Entry1.get()))
#関数に因数を渡す場合は、commandオプションとlambda式を使う
Button4.pack()


Button5 = tk.Button(text = 'add', width = 10, command = lambda : addlist(Entry1.get()))
Button5.pack()

Listbox1 = tk.Listbox(width = 25, height = 10)
Listbox1.pack()

Button6 = tk.Button(text = 'delete', width = 6, command = lambda : deleteList())
Button6.pack()



win.mainloop()