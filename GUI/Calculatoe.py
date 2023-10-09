from tkinter import*
import math

st = ""

root = Tk()
root.title("Simple Calculator")
root.geometry()

def add(num):
    global st
    st = st + str(num)
    st1.set(st)

def action():
    global st
    try:
        g = t1.get()
        y = eval(g)
        st1.set(y)
        st = "" + str(y)
    except:
        st1.set("Error")
        st=""

def sroot():
    global st
    try:
        g = t1.get()
        y = math.sqrt(eval(g))

        st1.set(y)
        st = "" + str(y)
    except:
        st1.set("Error")
        st=""

def dclear():
    global st
    st = st[:-1]
    st1.set(st)

def clear():
    global st
    st1.set("")
    st=""

def buttons():
    b = Button(root,text="1",bg="white",height=3,width=10,command=lambda : add(1))
    b.grid(column=0,row=4)
    b = Button(root,text="2",bg="white",height=3,width=10,command=lambda : add(2))
    b.grid(column=1,row=4)
    b = Button(root,text="3",bg="white",height=3,width=10,command=lambda : add(3))
    b.grid(column=2,row=4)
    b = Button(root,text="4",bg="white",height=3,width=10,command=lambda : add(4))
    b.grid(column=0,row=3)
    b = Button(root,text="5",bg="white",height=3,width=10,command=lambda : add(5))
    b.grid(column=1,row=3)
    b = Button(root,text="6",bg="white",height=3,width=10,command=lambda : add(6))
    b.grid(column=2,row=3)
    b = Button(root,text="7",bg="white",height=3,width=10,command=lambda : add(7))
    b.grid(column=0,row=2)
    b = Button(root,text="8",bg="white",height=3,width=10,command=lambda : add(8))
    b.grid(column=1,row=2)
    b = Button(root,text="9",bg="white",height=3,width=10,command=lambda : add(9))
    b.grid(column=2,row=2)

    b = Button(root,text="/",bg="white",height=3,width=10,command=lambda : add('/'))
    b.grid(column=3,row=1)
    b = Button(root,text="*",bg="white",height=3,width=10,command=lambda : add('*'))
    b.grid(column=3,row=2)
    b = Button(root,text="-",bg="white",height=3,width=10,command=lambda : add('-'))
    b.grid(column=3,row=3)
    b = Button(root,text="+",bg="white",height=3,width=10,command=lambda : add('+'))
    b.grid(column=3,row=4)
    b = Button(root,text=".",bg="white",height=3,width=10,command=lambda : add('.'))
    b.grid(column=2,row=5)
    b = Button(root,text="0",bg="white",height=3,width=10,command=lambda : add('0'))
    b.grid(column=1,row=5)
    b = Button(root,text="00",bg="white",height=3,width=10,command=lambda : add("00"))
    b.grid(column=0,row=5)
    b = Button(root,text="=",bg="green",height=3,width=10,command=action)
    b.grid(column=3,row=5)
    b = Button(root,text="Clear",bg="red",height=3,width=10,command=clear)
    b.grid(column=2,row=1)

    b = Button(root,text="√",bg="white",height=3,width=10,command=sroot)
    b.grid(column=0,row=1)
    b = Button(root,text="<-",bg="white",height=3,width=10,command=dclear)
    b.grid(column=1,row=1)


st1 = StringVar()

t1 = Entry(root,width=15,font=('Arial',20),textvariable=st1)
t1.grid(columnspan=5, ipadx=50)

buttons()

root.mainloop()
