from tkinter import *
import tkinter.messagebox as m
tasks=[]

#CREATING A WINDOW
root=Tk()
root.geometry("740x580")
root.title("TO-DO-LIST")
root.resizable(False,False)

#CREATING FUNCTIONS FOR THE GUI

def update_listbox():   #Function for clear the current list box 
    clear_listbox()
    for task in tasks:
        list.insert(END,task)

def clear_listbox():   #Function for clearing the list box
    list.delete(0,END)


def add_task():  #Function for add task in list box
    task=ent.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        m.showwarning("ALERT","Please,Add any task!")  #Show alert if entry widget is empty
        ent.delete(0,END)
    ent.delete(0,END)


def clear():
    task=list.get("active")   #Function for delete tasks from the list box
    if task in tasks:
        tasks.remove(task)
    else:
        m.showwarning("ALERT","Please,Select a task to delete")   #Show alert if list box is empty
    update_listbox()

def clear_all(): #Function to delete all tasks in the list box
    tasks.clear()
    update_listbox()


#CREATING LABELS
label1=Label(root,text="TO-DO-LIST",font=("algerian 30 bold"),bg="grey",padx=10,pady=10,relief=SOLID)
label1.place(x=10,y=0,height=40,width=715)

label2=Label(root,text="Add-tasks",font=("algerian 20 bold"),bg="lightblue",padx=10,pady=10,relief=RIDGE)
label2.place(x=10,y=55,height=30)

label3=Label(root,text="Tasks",font=("algerian 20 bold"),bg="lightblue",padx=10,pady=10,relief=RIDGE)
label3.place(x=10,y=180,height=30)


#CREATING ENTRY BOX
ent=Entry(root,font=("calibre 20 bold"),bg="white",relief=SOLID)
ent.place(x=10,y=90,height=70,width=540)


#CREATING BUTTONS

#Button for add a task in list box
b1=Button(root,text="ADD",font=("algerian 20 bold"),bg="lightblue",relief=SUNKEN,command=add_task)
b1.place(x=560,y=90,height=70,width=165)

#Button for remove selected item from the list box
b2=Button(root,text="CLEAR",font=("algerian 20 bold"),bg="lightblue",relief=SUNKEN,command=clear)
b2.place(x=560,y=215,height=70,width=165)

#Button for clear the listbox
b3=Button(root,text="CLEAR-ALL",font=("algerian 20 bold"),bg="lightblue",relief=SUNKEN,command=clear_all)
b3.place(x=560,y=295,height=70,width=165)

#Button for exiting the GUI
b4=Button(root,text="EXIT",font=("algerian 20 bold"),bg="lightblue",relief=SUNKEN,command=quit)
b4.place(x=560,y=375,height=70,width=165)

#CREATING LISTBOX
list=Listbox(root,font=("calibre 20 bold"),bg="white",relief=SOLID)
list.place(x=10,y=215,height=350,width=540)

root.mainloop()
