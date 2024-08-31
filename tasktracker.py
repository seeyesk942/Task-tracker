#importing packages 
from  tkinter import * 
import tkinter.messagebox
#function to enter the task in the Listbox
def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add)
    button_temp.pack()
    root1.mainloop()
    
def deletetask():
    # Selects the selected item and then deletes it
    selected = listbox_task.curselection()
    if selected:  # Check if an item is selected
        listbox_task.delete(selected[0])
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to delete")

def markcompleted():
    marked = listbox_task.curselection()
    if marked:  # Check if an item is selected
        temp = marked[0]
        # Store the text of the selected item in a string
        temp_marked = listbox_task.get(marked)
        # Update it
        temp_marked = temp_marked + " ✔"
        # Delete it then insert it
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to mark as completed")


def edittask():
    selected = listbox_task.curselection()
    if selected:
        current_text = listbox_task.get(selected[0])
        def save():
            new_text = entry_edit.get(1.0, "end-1c")
            listbox_task.delete(selected[0])
            listbox_task.insert(selected[0], new_text)
            root_edit.destroy()
        root_edit = Tk()
        root_edit.title("Edit task")
        entry_edit = Text(root_edit, width=40, height=4)
        entry_edit.insert(END, current_text)
        entry_edit.pack()
        button_save = Button(root_edit, text="Save", command=save)
        button_save.pack()
        root_edit.mainloop()
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to edit")

def clearalltasks():
    if tkinter.messagebox.askokcancel("Clear All", "Are you sure you want to clear all tasks?"):
        listbox_task.delete(0, END)

import pickle

def savetasks():
    tasks = listbox_task.get(0, END)
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)
    tkinter.messagebox.showinfo("Save tasks", "Tasks saved successfully!")

def loadtasks():
    try:
        with open("tasks.pkl", "rb") as f:
            tasks = pickle.load(f)
        listbox_task.delete(0, END)
        for task in tasks:
            listbox_task.insert(END, task)
    except FileNotFoundError:
        tkinter.messagebox.showwarning("Load tasks", "No saved tasks found.")

def movetaskup():
    selected = listbox_task.curselection()
    if selected:
        index = selected[0]
        if index > 0:
            text = listbox_task.get(index)
            listbox_task.delete(index)
            listbox_task.insert(index - 1, text)
            listbox_task.select_set(index - 1)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to move")

def movetaskdown():
    selected = listbox_task.curselection()
    if selected:
        index = selected[0]
        if index < listbox_task.size() - 1:
            text = listbox_task.get(index)
            listbox_task.delete(index)
            listbox_task.insert(index + 1, text)
            listbox_task.select_set(index + 1)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Please select a task to move")

# def searchtask():
#     search_term = entry_search.get(1.0, "end-1c")
#     listbox_task.selection_clear(0, END)
#     for i in range(listbox_task.size()):
#         if search_term.lower() in listbox_task.get(i).lower():
#             listbox_task.selection_set(i)


#creating the initial window
window=Tk()
#giving a title
window.title("TASK TRACKER")


#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="black",fg="white",height=15,width=50,font = "Helvetica")  
listbox_task.pack(side=tkinter.LEFT)

#Scrolldown in case the total list exceeds the size of the given window 
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


#Button widget 
entry_button=Button(window,text="Add task",width=50,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete selected task",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as completed",width=50,command=markcompleted)
mark_button.pack(pady=3)

mark_button=Button(window,text="edittask",width=50,command=edittask)
mark_button.pack(pady=3)

mark_button=Button(window,text="clearalltasks",width=50,command=clearalltasks)
mark_button.pack(pady=3)

mark_button=Button(window,text="savetasks",width=50,command=savetasks)
mark_button.pack(pady=3)

mark_button=Button(window,text="loadtasks",width=50,command=loadtasks)
mark_button.pack(pady=3)

mark_button=Button(window,text="movetaskup",width=50,command=movetaskup)
mark_button.pack(pady=3)

mark_button=Button(window,text="movetaskdown",width=50,command=movetaskdown)
mark_button.pack(pady=3)

window.mainloop()


