import tkinter as tk
from tkinter import ttk

root = tk.Tk()   

root.title("Student details")

buttons_frame = ttk.LabelFrame(root, text=' Student Details ')
buttons_frame.grid(column=0, row=7)

ttk.Label(buttons_frame, text="Enter Student's Name:").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Enter Student's Age:").grid(column=0, row=1)
ttk.Label(buttons_frame, text="Enter Student's Phone Number:").grid(column=0, row=2)
ttk.Label(buttons_frame, text="Enter Student's Marks:").grid(column=0, row=3)

name = tk.StringVar()
name_entered = ttk.Entry(buttons_frame, width=24, textvariable=name)
name_entered.grid(column=1, row=0)

age = tk.StringVar()
age_entered = ttk.Entry(buttons_frame, width=24, textvariable=age)
age_entered.grid(column=1, row=1)

phone_number= tk.StringVar()
phone_number_entered = ttk.Entry(buttons_frame, width=24, textvariable=phone_number)
phone_number_entered.grid(column=1, row=2)

marks= tk.StringVar()
marks_entered = ttk.Entry(buttons_frame, width=24, textvariable=marks)
marks_entered.grid(column=1, row=3)


table_frame = ttk.LabelFrame(root, text=' Table ')
table_frame.grid(column=0, row=8)

tv = ttk.Treeview(table_frame, columns=(1,2,3,4), show="headings", height="5")
tv.pack()
tv.heading(1, text="Student's Name")
tv.heading(2, text="Student's Age")
tv.heading(3, text="Student's Phone Number")
tv.heading(4, text="Student's Marks")

def action():
    tv.insert('', 'end', values=(name.get(), age.get(),phone_number.get(),marks.get()))
    name_entered.delete(0, 'end')
    age_entered.delete(0, 'end')
    phone_number_entered.delete(0, 'end')
    marks_entered.delete(0, 'end')

action = ttk.Button(buttons_frame, text="Insert Details", command=action)   
action.grid(column=2, row=0)

root.mainloop()
