from tkinter import *

root = Tk()
root.title("F to C Converter")

def action():
    try:
        r=t.get()
        a=eval(r)
        a= (a-32)/9*5
        st.set((a))
    except:
        st.set("Error")

def clear():
    st1.set("")
    st.set("")

st =StringVar()
st1 =StringVar()


root.geometry("300x200")

l = Label(root,text="fahrenheit :")
l.grid(column=0,row=0)
t = Entry(root,width=37,textvariable=st1)
t.grid(column=1,row=0,)

l = Label(root,text="celsius :")
l.grid(column=0,row=1)
t1 = Entry(root,width=37,textvariable=st)
t1.grid(column=1,row=1)

b = Button(root,text="Convert",fg="green",command=action)
b.grid(column=1,row=2)
b = Button(root,text="clear",fg="red",command=clear)
b.grid(column=0,row=2)

root.mainloop()

