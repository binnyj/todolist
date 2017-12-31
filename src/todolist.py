import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
from datetime import timedelta

class ToDoList:

    def __init__(self, master):

        self.taskList = []
        self.taskListLabels = []
        self.taskListLabels2 = []

        self.master = master
        master.title("ToDo List")
        master.minsize(width=500, height=700)
        master.maxsize(width=500, height=700)


        # Create the Notebook - multiple tabs
        self.notebook = ttk.Notebook(master)

        #First page// this will eventually be our OverView page
        self.page1 = tk.Frame(self.notebook, bg='white')
        self.tasknum = 0
        self.add_task_button = Button(self.page1, text="+ Add Task", command = lambda: self.create())


        #LAYOUT OF PAGE 1
        self.add_task_button.place(relx=0.5, rely=.95, anchor=CENTER)



        # Second page // this will eventually be our Next 7 Days page
        self.page2 = tk.Frame(self.notebook)

        # LAYOUT OF PAGE 2

        self.notebook.add(self.page1, text='OverView')
        self.notebook.add(self.page2, text='Next 7 Days')

        self.notebook.pack(expand=1, fill="both")




    def create(self):
        self.window = tk.Toplevel()
        self.taskName_label = Label(self.window, text = "Task Name")
        self.taskName_entry = Entry(self.window)
        self.dueDateDescription = Label(self.window, text = "Due Date Ex: 01/02/2017 month/day/year")
        self.dueDate_label = Label(self.window, text = "Due Date")
        self.dueDate_entry = Entry(self.window)
        self.estDescription = Label(self.window, text = "Enter # of days that assignment might take")
        self.estDuration_label = Label(self.window, text = "Estimated Duration")
        self.estDuration_entry = Entry(self.window)

        self.addbutton = Button(self.window, text="Add Task", command = lambda: self.add(self.taskName_entry.get(), self.dueDate_entry.get(), self.estDuration_entry.get()))

        self.taskName_label.grid(row = 0 , column = 0)
        self.taskName_entry.grid(row = 0, column = 1, columnspan = 3)

        self.dueDateDescription.grid(row = 1, column = 2)
        self.dueDate_label.grid(row = 2, column = 0)
        self.dueDate_entry.grid(row = 2, column = 1, columnspan = 3)

        self.estDescription.grid(row = 3, column = 2)
        self.estDuration_label.grid(row = 4, column = 0)
        self.estDuration_entry.grid(row = 4, column = 1, columnspan = 3)

        self.addbutton.grid(row = 5, column = 1, columnspan = 2)



    def add(self, taskName, dueDate, duration):
        d = dueDate.split("/")
        now = datetime.datetime.now().date()
        date = datetime.date(int(d[2]), int(d[0]), int(d[1]))
        zero = timedelta(days = 0)
        seven = timedelta(days = 7)

        tdDuration = timedelta(days = int(duration))


        self.taskList.append((taskName, date, duration))
        self.tasklisttext = "Task : " + str(taskName) + "\nDue Date : " + str(date) + " Duration : " + str(duration) + " days\n"

        self.label_text = StringVar()
        self.label_text.set(self.tasklisttext)

        self.listlabel = Label(self.page1, textvariable=self.label_text)
        self.listlabel.bind("<Button-1>", self.test)


        if (date - now <= zero):
            self.listlabel.config(bg = "red")
        elif (date - now < tdDuration):
            self.listlabel.config(bg = "yellow")
        elif (date - now >= tdDuration):
            self.listlabel.config(bg = "green")


        self.listlabel.grid(row = self.tasknum, column = 1, columnspan = 3, pady=10, padx = 80)
        self.taskListLabels.append(self.listlabel)

        self.tasknum += 1

        num = 0
        for i in self.taskList:

            if (i[1] - now <= seven):

                recentText = "Task : " + str(i[0]) + "\nDue Date : " + str(i[1]) + " Duration : " + str(i[2]) + " days\n"
                rlabel_text = StringVar()
                rlabel_text.set(recentText)
                recentTLabel = Label(self.page2, textvariable = rlabel_text)
                self.taskListLabels2.append(recentTLabel)

                if (i[1] - now <= zero):
                    recentTLabel.config(bg = "red")
                elif (i[1] - now < timedelta(days = int(i[2]))):
                    recentTLabel.config(bg = "yellow")
                elif (i[1] - now >= timedelta(days = int(i[2]))):
                    recentTLabel.config(bg = "green")

                recentTLabel.grid(row = num, column = 1, columnspan = 3, pady=10, padx = 80)
                num += 1




        self.window.destroy()

    def test(self, event):
        selected = event.widget
        selectedName = event.widget['text']
        selected.grid_forget()
        for i in self.taskList:
            if (selectedName == i[0]):
                self.taskList.remove(i)
            slist = self.page2.grid_slaves()
            for t in slist:
                if (selectedName == t['text']):
                    t.destroy()
                    self.taskListLabels2.remove(t)




root = Tk()
root.resizable(width=False, height=False)
todo_gui = ToDoList(root)
root.mainloop()
