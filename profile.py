from tkinter import *
from tkinter import ttk
win=Tk()

win.title("profile")
win.geometry("1000x750")
win.configure(bg="blue")

Label(win,text="Profile",font="impack 50 bold",bg="black",fg="white").place(x=500,y=20)

Label(win,text="Full name").place(x=380,y=140)
Entry(win).place(x=480,y=140)

Label(win,text="althernet mobile no").place(x=380,y=200)
Entry(win).place(x=500,y=200)


Label(win,text="State").place(x=380,y=260)

state=['Uttar pradesh','Madhy pradesh','Rajsthan','Bihar','uttaragand','Haryana','Gujrat','Gua','Patna','Ambadabad']
cb1=ttk.Combobox(win,values=state,width=20)
cb1.grid(row=1,column=1,padx=480,pady=260)

Label(win,text="District").place(x=380,y=320)
Entry(win).place(x=480,y=320)

Label(win,text="Address").place(x=380,y=380)
Entry(win).place(x=480,y=380)

Label(win,text="Pin code").place(x=380,y=440)
Entry(win).place(x=480,y=440)


win.mainloop()
