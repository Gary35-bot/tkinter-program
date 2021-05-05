from tkinter import *


def add_numbers():
    res = int(e1.get())+int(e2.get())
    myText.set(res) # sum of the 2 numbers enterd

# Delete entries
def delete():
    e1.delete(0, END)
    e2.delete(0, END)

# Enter the numbers you wanted you plus in a sum
root = Tk()
myText = StringVar()
Label(root, text="Enter first number ").grid(row=0, sticky=W)
Label(root, text="Enter second number ").grid(row=1, sticky=W)
Label(root, text="Result of addition").grid(row=3, sticky=W)
result = Label(root, text="", textvariable=myText).grid(row=3, column=1, sticky=W)

e1 = Entry(root)
e2 = Entry(root)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
# button for add, clear and exit
b = Button(root, text="Add", command=add_numbers)
b1 = Button(root, text="clear", command=delete)
b2 = Button(root, text="Exit", command=root.destroy)
# sets rows perfectly
b.grid(row=5, column=1, sticky=W+E+N+S, padx=5, pady=5)
b1.grid(row=5, column=2, sticky=W+E+N+S, padx=5, pady=5)
b2.grid(row=5, column=3, sticky=W+E+N+S, padx=5, pady=5)
mainloop()






