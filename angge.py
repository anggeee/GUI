from tkinter import *
from tkinter import messagebox

my_list = []

def create():
    name = "Name " + e1.get() + " " + e2.get() + " added successfully"
    messagebox.showinfo("Confirmation", name)

def read():
    my_list.append(name)
    messagebox.showinfo("Data" ,my_list)

frame = Tk()
Label(frame, text='Employee Number').grid(row=0, padx = 20, pady = 10)
Label(frame, text='Employee Name').grid(row=1, padx = 20, pady = 10)
e1 = Entry(frame)
e2 = Entry(frame)
e1.grid(row=0, column = 1, padx = 20, pady = 10)
e2.grid(row=1, column = 1,padx = 20, pady = 10)

#SHOW LIST DATA
Label(frame, text='Employee Number').grid(row=4 , padx = 20, pady = 10)
Label(frame, text='Employee Name').grid(row=4 ,  column= 2, padx = 20, pady = 10)

Label(frame, text = "sa").grid(row=5, padx = 20, pady = 10)
e3 = Entry(frame)

b1 = Button(frame, text = "ADD EMPLOYEE" ,  command = create)
b1.grid(row = 2, column = 1, padx = 20, pady = 10)

b2 = Button(frame, text = "SHOW LIST" ,  command = read)
b2.grid(row = 3, column = 1, padx = 20, pady = 10)

mainloop()
    
