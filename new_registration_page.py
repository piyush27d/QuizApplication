from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

from tkinter import filedialog
from tkinter.filedialog import askopenfile
import re
import pymysql
import mysql.connector
import fileinput



class new_registration:
    def __init__(self,root):
        self.root=root
        self.root.title("New registration")
        self.root.state("zoomed")   


        # variables
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.id_var=StringVar()
        self.password_var=StringVar()
        self.confirm_var=StringVar()
        self.check_var=StringVar()
        self.Img_var=StringVar()
        self.file=StringVar()
       
        # Image
        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)
 
        #hadder frame
        hadder_frame = Frame(self.root, bd=1, relief=RIDGE)
        hadder_frame.place(x=450, y=60, width=550, height=70)

        hadder_name = Label(hadder_frame, text="New registration", font=("times new roman",28, "bold"))
        hadder_name.grid(row=0, column=0, padx=150, pady=10, sticky=W)

        # main frame
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=130,width=550,height=585)
        
        # Username
        user_name=Label(main_frame,text="Username:",font=("times new roman",16,"bold"))
        user_name.grid(row=0,column=0,padx=30,pady=10,sticky=W)
        
        user_Entry=ttk.Entry(main_frame,textvariable=self.name_var,font=("arial",15),width=22)
        user_Entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        #Email
        user_email=Label(main_frame,text="Email Id:",font=("times new roman",16,"bold"))
        user_email.grid(row=1,column=0,padx=30,pady=10,sticky=W)

        email_Entry=ttk.Entry(main_frame,textvariable=self.email_var,font=("arial",15),width=22)
        email_Entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        # Gender
        user_Gender=Label(main_frame,text="Gender:",font=("times new roman",16,"bold"))
        user_Gender.grid(row=3,column=0,padx=30,pady=10,sticky=W)

        #Gender frame
        gen_Frame=Frame(main_frame)
        gen_Frame.place(x=229,y=100,width=280,height=35)

        rdoM=Radiobutton(gen_Frame,variable=self.gender_var,value="Male",text="Male",font=("times new roman",15)) #variable=self.gender.var
        rdoM.grid(row=0,column=0,padx=10,pady=0,sticky=W)
        self.gender_var.set("no")
        rdoF=Radiobutton(gen_Frame,variable=self.gender_var,value="Female",text="Female",font=("times new roman",15))
        rdoF.grid(row=0,column=1,padx=10,pady=0,sticky=W)

      
       
        # Password
        user_Pass=Label(main_frame,text="Password:",font=("times new roman",16,"bold"))
        user_Pass.grid(row=7,column=0,padx=30,pady=10,sticky=W)

        Pass_Entry=ttk.Entry(main_frame,textvariable=self.password_var,font=("arial",15),width=22)
        Pass_Entry.grid(row=7,column=1,padx=5,pady=10,sticky=W)

        # #bind and validation register
        # vali_pass=self.root.register(self.checkPassword())
        # Pass_Entry.config(validate="key",validatecommand=(vali_pass,"%P"))


        # conform password
        user_confPs=Label(main_frame,text="Confirm Password:",font=("times new roman",16,"bold"))
        user_confPs.grid(row=8,column=0,padx=30,pady=10,sticky=W)

        CP_Entry=ttk.Entry(main_frame,textvariable=self.confirm_var,font=("arial",15),width=22)
        CP_Entry.grid(row=8,column=1,padx=5,pady=10,sticky=W)

        #Back
        back=Button(main_frame,text="Back",bd=5,font=("arial",15,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.back_fun)
        back.place(x=45,y=450,height=50,width=150)
        
        #button Frame       
        saveBtn=Button(main_frame,text="Submit",bd=5,font=("arial",15,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",command=self.validation)
        saveBtn.place(x=200,y=450,height=50,width=150)


    #clear button
        clear=Button(main_frame,text="CLEAR ",bd=5,font=("arial",15,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.clear)
        clear.place(x=355,y=450,height=50,width=150)      
    


        self.frame1=main_frame

        
    def clear(self):
        
    
       
        self.name_var.set('')
        self.email_var.set("")
        self.gender_var.set("no")
        self.password_var.set("")
        self.confirm_var.set("")
        

    def back_fun(self):
        from main_page import display
        a=display(self.root)

    def verify_data(self):
            data=f"Name:{self.name_var.get()} \nEmail Id:{self.email_var.get()} \nGender:{self.gender_var.get()} \nID Proof:{self.id_var.get()} \nPassword:{self.password_var.get()} \n image:{self.imag.get()}"
            messagebox.showinfo("Details",data)    
   

    #call back function
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=="":
            return True
        else:
            messagebox.showerror("Invalid","Not allowed")
            return False

    
   
        
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email):
                return True
            else:
                messagebox.showwarning("Alert","Invalied email enter valied Email Id")
                return False
            
        else:
            messagebox.showinfo("Invalid","Email length is too small")


    # validation
    def validation(self):  
        try:      
            if self.name_var.get()=="":
                messagebox.showerror("Error","Please enter your name",parent=self.root)
                
            elif self.email_var.get()=="":
                messagebox.showerror("Error","Please enter your email id",parent=self.root)

            elif self.gender_var.get()=="":
                messagebox.showerror("Error","Please select gender",parent=self.root)    

            elif self.password_var.get()=="":
                messagebox.showerror("Error","Please enter password",parent=self.root)   

            elif self.confirm_var.get()=="":
                messagebox.showerror("Error","Please confirm password",parent=self.root)    

            elif self.password_var.get() !=  self.confirm_var.get():
                messagebox.showerror("Error","Password and confirm password are not matching",parent=self.root)    

            # elif self.file.get()=="":
            #     messagebox.showerror("Error","Please upload image",parent=self.root)    

            
            elif self.email_var.get()!=None and self.password_var.get()!=None:
                x=self.checkemail(self.email_var.get())
                y=self.checkPassword(self.password_var.get())

        except:
            
            messagebox.showinfo("Successfully",f"Your registration successfully completed.",parent=self.root)
            self.connection()
            #self.insertBLOB(self.file)
            from login_page import loginPage
            loginPage(self.root)

    def connection(self):
        conn=pymysql.connect(host="localhost",user="root",password="root",database="db_quiz")
        cur=conn.cursor()  
        cur.execute("Insert into registration_tb (USERNAME,EMAIL,GENDER,PASSWORD,RECHACK_PASS) values(%s,%s,%s,%s,%s)",({self.name_var.get()},{self.email_var.get()},{self.gender_var.get()},{self.password_var.get()},{self.confirm_var.get()})) 
        conn.commit()

def new_reg():
    root = Tk()
    obj = new_registration(root=root)
    #obj.connection()
    root.mainloop()

if __name__=="__main__":
    new_reg()