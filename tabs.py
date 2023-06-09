import tkinter as tk 
from tkinter import ttk
win=tk.Tk()
win.title('tabs')

nb=ttk.Notebook(win)

page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='one')
nb.add(page2,text='two')
nb.pack(expand=True,fill='both')

namelabel=ttk.Label(page1,text='enter your name')
# namelabel.pack(expand=True,fill='both').
namelabel.grid(row=0 ,column=0)


nameentry=ttk.Entry(page1 ,width=15)
nameentry.grid(row=0 ,column=1)
# nameentry.pack(expand=True,fill='both')



namelabel=ttk.Label(page2,text='email')
# namelabel.pack(expand=True,fill='both').
namelabel.grid(row=0 ,column=0)


nameentry=ttk.Entry(page2 ,width=15)
nameentry.grid(row=0 ,column=1)
# nameentry.pack(expand=True,fill='both')













win.mainloop()