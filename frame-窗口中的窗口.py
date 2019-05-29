import tkinter as tk
window=tk.Tk()
window.title('小朋友快来玩呀')
window.geometry('200x200')#窗口尺寸
tk.Label(window,text='on the window').pack()
frm=tk.Frame(window)
frm.pack()
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l,text='on the window').pack()
tk.Label(frm_r,text='on the window').pack()




window.mainloop()
