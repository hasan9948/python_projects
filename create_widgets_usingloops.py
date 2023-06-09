import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('LOOP')

labels=['enter your name :' , 'enter your email :', 'enter your age :' ,'city :' ]

dict_var={
    'name':tk.StringVar(),
    'email':tk.StringVar(),
    'age':tk.StringVar(),
    'city':tk.StringVar()
}
for i in range(len(labels)):
    cur_label='label'+str(i)
    
    # cur_var='var'+str(i)
    # cur_var=tk.StringVar()
    cur_label=ttk.Label(win , text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=50 ,pady=50)
c=0
for i in dict_var:
    cur_entrybox='entrybox'+str(i)
    cur_entrybox=ttk.Entry(win , width=15,textvariable=dict_var[i])
    cur_entrybox.grid(row=c,column=1,padx=50 ,pady=50)
    c+=1
    
def action():
    for i in dict_var:
        print(dict_var[i].get())
        

    
btn=ttk.Button(win , text='submit' ,command=action)
btn.grid(row=10,column=0)

win.mainloop()