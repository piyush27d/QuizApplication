from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from login_page import loginPage
from new_registration_page import new_registration
import re

class admin_page:
    def __init__(self,root):
        self.root=root
        self.root.title("ADMIN PAGE")
        self.root.state("zoomed")

        # Image
        self.bg2 = ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl = Label(self.root, image=self.bg2, relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)

        # main frame
        main_frame = Frame(self.root, bd=1, relief=RIDGE)
        main_frame.place(x=450, y=170, width=550, height=400)

        label1 = Label(main_frame, text="Create new Quiz", font=("times new roman", 30, "bold"))
        label1.grid(row=1, column=0, padx=100, pady=50, sticky=W)

        login = Button(main_frame, text="Login", font=("arial", 15, "bold"),bd=5, width=15, cursor="hand2", bg="sky blue",
                        activebackground="gray",command=self.login_fun)
        login.grid(row=2, column=0, padx=40, pady=0)

        label2 = Label(main_frame, text="Already have account", font=("times new roman", 15, "bold"))
        label2.grid(row=3, column=0, padx=160, pady=0, sticky=W)

        register = Button(main_frame, text="Register", font=("arial", 15, "bold"),bd=5, width=15, cursor="hand2", bg="sky blue",
                        activebackground="gray",command=self.register_fun)
        register.grid(row=4, column=0, padx=40, pady=50)

    def login_fun(self):
       loginPage(self.root)

    def register_fun(self):
       new_registration(self.root)

def second():
    root=Tk()
    obj=admin_page(root=root)
    root.mainloop()
 
if __name__=="__main__":
    second()
   