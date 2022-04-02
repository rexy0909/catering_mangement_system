from tkinter import PhotoImage
import tkinter as tk

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

root = tk.Tk()
root.title("Catering Dashboard")
root.config(bg="white")
root.geometry("1300x700+0+0")

btnState = False


navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")


def switch():
    global btnState
    if btnState is True:
    
        for x in range(300):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        
        brandLabel.config(bg="white", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="white")
        btnState = False
    else:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

       
        for x in range(-50, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()
        btnState = True

topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)


homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")


brandLabel = tk.Label(root, text="Catering \n Mangement System", font="System 30", bg="white", fg="green")
brandLabel.place(x=100, y=250)


navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)


navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)


y = 80

options = ["Profile", "Menu","My Order","Settings", "Help", "About", "Feedback","Log out",]

for i in range(7):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="white", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

root.mainloop()