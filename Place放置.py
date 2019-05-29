import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x200')#窗口尺寸
#for i in range(4):
	#for j in range(3):
		#tk.Label(window,text=1).grid(row=i,column=j,ipadx=10,ipady=10
tk.Label(window,text=1).place(x=10,y=100,anchor='nw')

window.mainloop()
