from tkinter import*

root = Tk()
root.title("Simple Calculator")
root.geometry("300x100")

def action():
    try:
        g = t1.get()
        st1.set((eval(g)))
    except:
        st1.set("Error")

def clear():
    st1.set("")

st1 = StringVar()

l = Label(root,text="Enter an Expression",fg="green")
l.pack()
t1 = Entry(root,width=40,textvariable=st1)
t1.pack()

b = Button(root,text="=",bg="green",width=10,command=action)
b.pack()
b = Button(root,text="Clear",bg="red",width=10,command=clear)
b.pack()

root.mainloop()
