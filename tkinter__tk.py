# first way***************

# import tkinter 
# win = tkinter.Tk()
# win.title("GUI")
# win.mainloop()

# second way**************

# from tkinter import *
# win =Tk()
# win.mainloop()

import tkinter as tk 
from csv import DictWriter
import os
from tkinter import ttk
win = tk.Tk()
win.title('GUI')




# create lables************
# widgets =radio button 

name_label=ttk.Label(win,text='enter your name :')
name_label.grid(row=0,column=0,sticky=tk.W)                         # pack grid
# ttk.Label(win,text='enter your name :').pack()
email_label=ttk.Label(win, text='enter your email :')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win, text='enter your age :')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win, text='enter your gender :')
gender_label.grid(row=3,column=0,sticky=tk.W)


# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win , width=15,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win, width=15,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win, width=15,textvariable=age_var)
age_entrybox.grid(row=2,column=1)


# create combo box
gender_var=tk.StringVar()
combo_box=ttk.Combobox(win,width=14,textvariable=gender_var  ,state='readonly')
combo_box['values']=('males','female','other')
combo_box.current(0)
combo_box.grid(row=3,column=1)


# create radio button

radio_var=tk.StringVar()
radiobtn1=ttk.Radiobutton(win, text='student' ,value='student' ,variable=radio_var)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win , text='teacher' ,value='teacher' ,variable=radio_var)
radiobtn2.grid(row=4, column=1)

# create checkbutton 

check_var=tk.StringVar()
checkbtn=ttk.Checkbutton(win, text='check if u agrees with all our conditions' ,variable=check_var)
checkbtn.grid(row=5,columnspan=3)






# create button
def action():
    username=name_var.get()
    useremail=email_var.get()
    userage=age_var.get()
    usergender=gender_var.get()
    userradio=radio_var.get()
    usercheck=check_var.get()

    print(f'{username}    {useremail}    {userage}    {usergender}   {userradio}   {usercheck}')
    all=f'{username}    {useremail}    {userage}    {usergender}   {userradio}   {usercheck}'
    # with open('userinfofile.txt', 'a') as f:
    #     f.write(f'{all} \n')

    with open('filecsvpython.csv','a',newline='') as f:
        dict_writer=DictWriter(f , fieldnames=['firstname','email','age','gender','type','sbscribe'])
        if os.stat('filecsvpython.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'firstname':username,
            'email':useremail,
            'age':userage,
            'gender':usergender,
            'type':userradio,
            'sbscribe':usercheck
        })

    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)


    name_label.configure(foreground='red')
    name_label.configure(background='black')
    age_label.configure(foreground='red')
    age_label.configure(background='black')
    email_label.configure(foreground='red')
    email_label.configure(background='black')


button=ttk.Button(win,text='Submit',command=action)
button.grid(row=10,column=0,sticky=tk.W)





win.mainloop()