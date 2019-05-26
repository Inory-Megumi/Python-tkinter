import tkinter as tk
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x100')#窗口尺寸

var=tk.StringVar()#声明text字符串变量
l=tk.Label(window,textvariable=var, bg='green',font=('Arial',12),width=15,height=2)
l.pack()#布局，默认上方
on_hit = False
def hit_me():
    global  on_hit
    if on_hit == False:
        on_hit = True
        var.set('You hit me!')
    else:
        on_hit=False
        var.set('')


b=tk.Button(window,text='Hit me!',width=15,height=2,command=hit_me)
#command可以传入函数，点击Button进入函数
b.pack()

window.mainloop()#主循环
