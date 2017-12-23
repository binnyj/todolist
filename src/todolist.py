import tkinter as tk
from tkinter import Tk, ttk, Label, Button, Entry, StringVar, END, W, E


class ToDoList:

    def __init__(self, master):
        self.master = master
        master.title("ToDo List")
        master.minsize(width=500, height=800)
        master.maxsize(width=500, height=800)


        # Create the Notebook - multiple tabs
        notebook = ttk.Notebook(master)
        # self.style = ttk.Style()
        # self.style.configure('p1', bg='white')

        #First page// this will eventually be our OverView page
        page1 = tk.Frame(notebook, bg='white')



        # Second page // this will eventually be our Next 7 Days page
        page2 = tk.Frame(notebook)

        notebook.add(page1, text='OverView')
        notebook.add(page2, text='Next 7 Days')

        notebook.pack(expand=1, fill="both")


        self.tasklist = ""
        self.tasknum = 0
        self.label_text = StringVar()
        self.label_text.set(self.tasklist)
        self.listlabel = Label(page1, textvariable=self.label_text)

        self.add_task_button = Button(page1, text="+ Add Task", command = lambda: self.update("add"))


        #LAYOUT OF PROGRAM
        self.listlabel.grid(row = 1, column = 1, columnspan = 2)

        self.add_task_button.grid(row = 2, column = 1)

    def update(self, method):
        if method == "add":
            self.tasklist = "Task " + str(self.tasknum)
            self.label_text.set(self.tasklist)
            self.tasknum += 1



root = Tk()
root.resizable(width=False, height=False)

todo_gui = ToDoList(root)
root.mainloop()
