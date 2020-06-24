from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from PIL import Image
import importlib

class Login_System:
    def __init__(self,root):
        #print("Hello")
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x750+0+0")

        #====All Images ===
        bg_icon = Image.open("images/bg.jpg")
        bg_icon = bg_icon.resize((1350, 650), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.bg_icon = ImageTk.PhotoImage(bg_icon)
        #self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")

        user_icon = Image.open("images/man_user.png")
        user_icon = user_icon.resize((30, 30), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.user_icon = ImageTk.PhotoImage(user_icon)
        #self.user_icon=PhotoImage(file="images/man_user.png")

        pass_icon = Image.open("images/password.png")
        pass_icon = pass_icon.resize((30, 30), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.pass_icon=ImageTk.PhotoImage(pass_icon)
        #self.pass_icon=PhotoImage(file="images/password.png")            

        logo_icon = Image.open("images/user.png")
        logo_icon = logo_icon.resize((100, 100), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        self.logo_icon=ImageTk.PhotoImage(logo_icon)
        
        #self.logo_icon=PhotoImage(file="images/user.png")
        #====variable====
        self.uname=StringVar()
        self.pass_=StringVar()
        bg_lbl = Label(self.root,image=self.bg_icon)
        bg_lbl.pack()
        title = Label(self.root,text="Login System", font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)                

        Login_Frame = Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl = Label(Login_Frame, image = self.logo_icon,bd=10).grid(row=0,columnspan=2,pady=20)

        lbluser = Label(Login_Frame,text="UserName", image = self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg ="white" ).grid(row=1,column=0,padx=20,pady=10)
        txtuser = Entry(Login_Frame,bd = 5,textvariable=self.uname ,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20,pady=10)

        lblpass = Label(Login_Frame,text="Password", image = self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg ="white" ).grid(row=2,column=0,padx=20,pady=10)
        txtpass = Entry(Login_Frame,bd = 5,textvariable=self.pass_ ,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20,pady=10)

        btn_log = Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red",command=self.login).grid(row=3,column=1,pady=10)
        
    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All Fields are requires!!")
        elif self.uname.get()=="suraj" and self.pass_.get()=="123456":
            messagebox.showinfo("Successfull",f"Welcome {self.uname.get()}")
            #pm = __import__('Employee_Attendence_System')
            #exec(open('Employee_Attendence_System.py').read())
        else:
            messagebox.showerror("Error","Invalid USername or Password")
            
            
root = Tk()
obj=Login_System(root)
#obj.login()
#root.resizable(height=False,width=False)
root.mainloop()
