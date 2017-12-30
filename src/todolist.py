import tkinter as tk
from tkinter import *
from tkinter import ttk



class ToDoList:

    def __init__(self, master):

        self.taskListLabels = []
        self.taskList = []

        self.master = master
        master.title("ToDo List")
        master.minsize(width=500, height=700)
        master.maxsize(width=500, height=700)


        # Create the Notebook - multiple tabs
        self.notebook = ttk.Notebook(master)
        # self.style = ttk.Style()
        # self.style.configure('p1', bg='white')

        #First page// this will eventually be our OverView page
        self.page1 = tk.Frame(self.notebook, bg='white')


        # self.tasklisttext = ""
        self.tasknum = 0
        # self.label_text = StringVar()
        # self.label_text.set(self.tasklisttext)
        # self.listlabel = Label(self.page1, textvariable=self.label_text)

        self.add_task_button = Button(self.page1, text="+ Add Task", command = lambda: self.create())


        #LAYOUT OF PROGRAM // PAGE 1
        # self.listlabel.grid(row = 1, column = 1, columnspan = 2)

        self.add_task_button.place(relx=0.5, rely=.95, anchor=CENTER)



        # Second page // this will eventually be our Next 7 Days page
        self.page2 = tk.Frame(self.notebook)

        self.notebook.add(self.page1, text='OverView')
        self.notebook.add(self.page2, text='Next 7 Days')

        self.notebook.pack(expand=1, fill="both")


    def create(self):
        self.window = tk.Toplevel()
        self.taskName_label = Label(self.window, text = "Task Name")
        self.taskName_entry = Entry(self.window)
        self.dueDate_label = Label(self.window, text = "Due Date")
        self.dueDate_entry = Entry(self.window)
        self.estDuration_label = Label(self.window, text = "Estimated Duration")
        self.estDuration_entry = Entry(self.window)

        self.addbutton = Button(self.window, text="Add Task", command = lambda: self.add(self.taskName_entry.get(), self.dueDate_entry.get(), self.estDuration_entry.get()))

        self.taskName_label.grid(row = 0 , column = 0)
        self.taskName_entry.grid(row = 0, column = 1, columnspan = 3)

        self.dueDate_label.grid(row = 1, column = 0)
        self.dueDate_entry.grid(row = 1, column = 1, columnspan = 3)

        self.estDuration_label.grid(row = 2, column = 0)
        self.estDuration_entry.grid(row = 2, column = 1, columnspan = 3)

        self.addbutton.grid(row = 3, column = 1, columnspan = 2)



    def add(self, taskName, dueDate, duration):
        self.taskList.append((taskName, dueDate, duration))
        self.tasklisttext = "Task : " + str(taskName) + "\nDue Date : " + str(dueDate) + " Duration : " + str(duration) + "\n"

        self.label_text = StringVar()
        self.label_text.set(self.tasklisttext)

        self.listlabel = Label(self.page1, textvariable=self.label_text , borderwidth=2, relief="groove")
        self.listlabel.bind("<Button-1>", self.test)

        self.listlabel.grid(row = self.tasknum, column = 1, columnspan = 2)
        self.taskListLabels.append(self.listlabel)

        self.tasknum += 1
        self.window.destroy()

    def test(self, event):
        selected = event.widget
        selected.grid_forget()


root = Tk()
root.resizable(width=False, height=False)
todo_gui = ToDoList(root)
root.mainloop()
