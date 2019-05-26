import tkinter as tk
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x200')#窗口尺寸
var=tk.StringVar()
l =tk.Label(window,bg='yellow',width=18,text='empty')
l.pack()
def print_selection(v):
	l.config(text='you have selected '+v) 
s=tk.Scale(window,label='try me',from_=5,to=10,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=1,resolution=0.01,command=print_selection)
#from_ to起点和终点 length滑动条长度 showvalue显示数值 tickinterval最小显示分度 resolution 最小分度
s.pack()

window.mainloop()
