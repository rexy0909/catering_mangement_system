import email
from msilib.schema import File
from tkinter import *
import os
from click import command
import mysql.connector as mysql
from PIL import Image,ImageTk

from tkinter.messagebox import *


class Login():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x700+0+0")
        self.root.title("catring mangement System")
        self.bg=ImageTk.PhotoImage(file="earth.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        self.middle=ImageTk.PhotoImage(file="foode.png")
        middle=Label(self.root,image=self.middle).place(x=0,y=0,width=800,height=800)
       
        self.Right=ImageTk.PhotoImage(file="log.jpg")
        Right=Label(self.root,image=self.Right).place(x=900,y=150,width=300,height=400)
        
        #========variavles===========
        self.username=StringVar()
        self.passworde=StringVar()
        
        self.create_elements()
        
        self.root.mainloop()
        
    def create_elements(self):
        
        
        
        self.welcome = Label(self.root, text="WELCOME", font=('colonna mt', 24, 'bold'))
        self.welcome.place(x=970, y=165)


        self.username = Label(self.root, text="Username:", font=('times new roman', 16, 'bold'))
        self.username.place(x=920, y=250)

        self.entry_username = Entry(self.root,textvariable=self.username, font=('times new roman', 14))
        self.entry_username.place(x=920, y=282 ,height=25 ,width=200 )

        self.password = Label(self.root, text="Password:", font=('times new roman', 16, 'bold'))
        self.password.place(x=920, y=310)

        self.entry_password = Entry(self.root, textvariable=self.passworde, font=('Verdana', 14))
        self.entry_password.place(x=920, y=342, height=25 ,width=200)

        self.login_button = Button(self.root,text="Login", height=1, width=8,command=self.login_user)
        self.login_button.place(x=920, y=385) 
        
        self.newuser = Label(self.root, text="New user?", font=('times new roman', 12))
        self.newuser.place(x=1040, y=385)
        
        self.forgetten = Button(self.root, text="Forgot Password", font=('times new roman', 10),command=self.forget_password)
        self.forgetten.place(x=920, y=415)

        self.register_button = Button(self.root, text="Sign Up", height=1, width=8, command=self.destroy_login)
        self.register_button.place(x=1040, y=415)

    def forget_password(self):
        self.root2=Toplevel()
        self.root2.mainloop()    


    def destroy_login(self):
        self.root.destroy()
        register = Register()
    def loding(self):
        posx = self.root.winfo_screenwidth()/2
        posy = self.root.winfo_screenheight()/2
        frameCnt = 25
        frames = [PhotoImage(file="preloading.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]

        def dest():
            self.root.destroy()

        def update(ind):

            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label.configure(image=frame)
            self.root.after(100, update, ind)
        label = Label(self.root)
        label.place(x=posx, y=posy-100)
        self.root.after(0, update, 0)
        self.root.after(3000,dest)
        self.root.mainloop() 
    def dashboad(self):
        self.root.file="navbar.py"
        
        


        self.root.mainloop()      

    def login_user(self):
        username = self.entry_username.get()
        userpassword = self.entry_password.get()

        if(username == "" or userpassword == ""):
            showinfo("Oops!","Your information can't be empty!")
            return

        mydb = mysql.connect(
          host="localhost",
          user="root",
          password="",
          database = "catering"
        )

        mycursor = mydb.cursor()
        sql = "select * from register where username=%s and password=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        if result:
            showinfo("Success","You're logged in!")
            self.loding()
            self.dashboad()
        else:
            showinfo("Failed","You've entered wrong credentials!")
    

class Register():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1300x700+0+0")
        self.root.title("Register Cantering Mangement System")
        self.bg=ImageTk.PhotoImage(file="foode.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.create_elements()
        self.root.mainloop()

    def create_elements(self):
  
       #================VARIABLES=================
        self.username=StringVar()
        self.password=StringVar()
        self.name=StringVar()
        self.mobile=StringVar()
        self.email=StringVar()
        self.nationality=StringVar()
        self.address=StringVar()
        self.state=StringVar()
        self.pincode=StringVar()
       

        #================================================================================           
        self.Left=ImageTk.PhotoImage(file="back.jpg")
        Left=Label(self.root,image=self.Left).place(x=10,y=3,width=460,height=630)

        self.registration = Label(self.root, text="Register Here", font=('algerian', 18, 'bold'))
        self.registration.place(x=135, y=12)
        
        self.username =Label(self.root, text="Username:", font=('times new roman', 12))
        self.username.place(x=50, y=50)

        self.entry_username = Entry(self.root,textvariable=self.username, font=('times new roman', 12))
        self.entry_username.place(x=160, y=50, height=25, width=200)

        self.password = Label(self.root, text="Password:", font=('times new roman', 12))
        self.password.place(x=50, y=90)

        self.entry_password = Entry(self.root,textvariable=self.password, font=('times nw roman', 12))
        self.entry_password.place(x=160, y=90, height=25, width=200)

        self.name = Label(self.root, text="Name:", font=('times new roman', 12))
        self.name.place(x=50, y=130)

        self.entry_name = Entry(self.root,textvariable=self.name, font=('times new roman', 12))
        self.entry_name.place(x=160, y=130, height=25, width=200)

        self.mobile = Label(self.root, text="Mobile no. -", font=('times new roman', 12))
        self.mobile.place(x=50, y=170)

        self.entry_mobile = Entry(self.root,textvariable=self.mobile, font=('times new roman', 12))
        self.entry_mobile.place(x=160, y=170, height=25, width=200)
        
        self.email = Label(self.root, text="Email ID: ", font=('times new roman', 12))
        self.email.place(x=50, y=210)

        self.entry_email = Entry(self.root,textvariable=self.email, font=('times new roman', 12))
        self.entry_email.place(x=160, y=210, height=25, width=200)
        
        self.nationality = Label(self.root, text="Nationality:", font=('times new roman', 12))
        self.nationality.place(x=50, y=250)

        self.entry_nationality = Entry(self.root,textvariable=self.nationality, font=('times new roman', 12))
        self.entry_nationality.place(x=160, y=250, height=25, width=200)
        
        self.address = Label(self.root, text="Address:", font=('times new roman', 12))
        self.address.place(x=50, y=290)

        self.entry_address = Entry(self.root,textvariable=self.address, font=('times new roman', 12))
        self.entry_address.place(x=160, y=290, height=25, width=200)

        self.state = Label(self.root, text="State:", font=('times new roman', 12))
        self.state.place(x=50, y=330)

        self.entry_state = Entry(self.root,textvariable=self.state, font=('times new roman', 12))
        self.entry_state.place(x=160, y=330, height=25, width=200)

        self.pincode = Label(self.root, text="Pincode:", font=('times new roman', 12))
        self.pincode.place(x=50, y=370)

        self.entry_pincode = Entry(self.root,textvariable=self.pincode, font=('times new roman', 12))
        self.entry_pincode.place(x=160, y=370, height=25, width=200)
        
        self.register_button = Button(self.root, text="Sign Up", font=('times new roman', 12,'bold'), height=1, width=8, command=self.register_user)
        self.register_button.place(x=160, y=425)
        
        self.existing_user = Label(self.root, text="Existing User - ", font=('times new roman', 12))
        self.existing_user.place(x=55, y=500)

        self.login_button = Button(self.root, text="Login", height=1, width=8, command=self.destroy_register)
        self.login_button.place(x=155, y=500)

    def destroy_register(self):
        self.root.destroy()
        login = Login()

    def register_user(self): 
        username = self.entry_username.get()
        userpassword = self.entry_password.get()
        name = self.entry_name.get()
        mobile=self.entry_mobile.get()
        email=self.entry_email.get()
        nationality=self.entry_nationality.get()
        address=self.entry_address.get()
        state=self.entry_state.get()
        pincode=self.entry_pincode.get()



        if(username == "" or userpassword == "" or name == "" or mobile== "" or email == "" or nationality == "" 
           or address == "" or state =="" or pincode==""):
            showinfo("Oops!","Your information can't be empty!")
            return

        mydb = mysql.connect(
          host="localhost",
          user="root",
          password="",
          database = "catering"
        )

        mycursor = mydb.cursor()

        mycursor.execute("select count(*) from register")
        result = mycursor.fetchone()
        old_count = result[0]

        sql = "INSERT INTO register (username, password, name,mobile,email,nationality,address,state,pincode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (username, userpassword, name,mobile,email,nationality,address,state,pincode)
        mycursor.execute(sql, val)
        mydb.commit()
        
        mycursor.execute("select count(*) from register")
        result = mycursor.fetchone()
        new_count = result[0]

        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_mobile.delete(0,END)
        self.entry_email.delete(0,END)
        self.entry_nationality.delete(0,END)
        self.entry_address.delete(0,END)
        self.entry_state.delete(0,END)
        self.entry_pincode.delete(0,END)


        if(old_count + 1 == new_count):
            showinfo("Success","Your information is saved successfully!")
        else:
            showinfo("Failed","Your information couldn't save successfully!")


if __name__ == '__main__':
    login = Login()