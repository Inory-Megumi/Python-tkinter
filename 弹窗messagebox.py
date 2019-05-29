import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x200')#窗口尺寸
def hit_me():
	#tk.messagebox.showinfo(title='Hi',message='hahahha')
	#tk.messagebox.showwarning(title='Hi',message='nononono')
	#tk.messagebox.showerror(title='Hi',message='WTF!!!!!')
	print(tk.messagebox.askquestion(title='Hi',message='hhh'))
tk.Button(window,text='hit me',command=hit_me).pack()



window.mainloop()
