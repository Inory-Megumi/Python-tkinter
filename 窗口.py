import tkinter as tk
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x200')#窗口尺寸
l=tk.Label(window,text='',bg='yellow')
l.pack()
counter=0
def do_job():
	global counter
	l.config(text='do'+str(counter))
	counter+=1

menubar=tk.Menu(window)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

submenu=tk.Menu(filemenu,tearoff=0)#添加子菜单
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu 1',command=do_job)



editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=filemenu)
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

window.config(menu=menubar)
