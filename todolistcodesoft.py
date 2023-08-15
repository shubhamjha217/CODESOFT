import tkinter as tk
from tkinter import *

window=Tk()
window.title("TO-DO-LIST")
window.geometry("600x600")
window.config(bg='lightblue')

task_list=[]

def add_task():
    task_text = task_entry.get() 
    if task_text:
        listbox.insert(tk.END, task_text) 
        task_entry.delete(0, tk.END)

def delete_selected_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)



Image_icon=PhotoImage(file="task.png")
window.iconphoto(False,Image_icon)

TopImage=PhotoImage(file="topbar.png")
Label(window,image=TopImage).pack()

dockImage=PhotoImage(file="dock.png")
Label(window,image=dockImage,bg="black").place(x=400,y=20)

noteImage=PhotoImage(file="task.png")
Label(window,image=noteImage,bg="pink").place(x=155,y=20)

heading=Label(window,text="TASKS",font="arial 20 bold",fg="black",bg="yellow")
heading.place(x=250,y=20)

frame=Frame(window,width=400,height=50,bg='black')
frame.place(x=100,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="add",font="arial 20 bold",width=6,bg="green",fg="white",bd=0,command=add_task)
button.place(x=300,y=0)

frame1=Frame(window,bd=3,width=500,height=280,bg="grey")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="white",fg="black",cursor="hand2",selectbackground="blue")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon=PhotoImage(file="delete.png")
Button(window,image=Delete_icon,bd=0,command=delete_selected_task).pack(side="bottom",pady=13)

window.mainloop()

