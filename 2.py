import tkinter as tk
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x200')#窗口尺寸
var=tk.StringVar()
t=tk.Text(window,height=2)
e=tk.Entry(window,show='*')
e.pack()
def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
    t.insert('end',var)

b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2=tk.Button(window,text='insert end',width=15,height=2,command=insert_end)
b2.pack()
t.pack()
window.mainloop()
