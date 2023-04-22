from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import re
import pymysql
import pyttsx3   #Install pyttsx3 for text to speech 


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("New registration")
        self.root.geometry("1400x700+0+0")

       
        # variables
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.gender_var=StringVar()
        self.country_var=StringVar()
        self.id_var=StringVar()
        self.idNo_var=StringVar()
        self.password_var=StringVar()
        self.confirm_var=StringVar()
        self.check_var=IntVar()
       
        # Image
        self.bg=ImageTk.PhotoImage(file="D:/New_project/photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bgLbl.place(x=0,y=0,height=700,width=1400)
 
        #hadder frame
        hadder_frame = Frame(self.root, bd=1, relief=RIDGE)
        hadder_frame.place(x=450, y=40, width=550, height=70)

        hadder_name = Label(hadder_frame, text="New registration", font=("times new roman",28, "bold"))
        hadder_name.grid(row=0, column=0, padx=150, pady=10, sticky=W)

        # main frame
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=585)
        
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


        
        #category type
        userId_Type=Label(main_frame,text="Category:",font=("times new roman",16,"bold"))
        userId_Type.grid(row=5,column=0,padx=30,pady=10,sticky=W)

        self.combo_idType=ttk.Combobox(main_frame,textvariable=self.id_var,font=("arial",15),justify="center",state="readonly",width=21)
        self.combo_idType["values"]=("Select your Category", "Student", "professor", "facaulty")
        self.combo_idType.grid(row=5,column=1,padx=5,pady=10)
        self.combo_idType.current(0)

       
        # Password
        user_Pass=Label(main_frame,text="Password:",font=("times new roman",16,"bold"))
        user_Pass.grid(row=7,column=0,padx=30,pady=10,sticky=W)

        Pass_Entry=ttk.Entry(main_frame,textvariable=self.password_var,font=("arial",15),width=22)
        Pass_Entry.grid(row=7,column=1,padx=5,pady=10,sticky=W)

        #bind and validation register
        vali_pass=self.root.register(self.checkPassword)
        Pass_Entry.config(validate="key",validatecommand=(vali_pass,"%P"))


        # conform password
        user_confPs=Label(main_frame,text="Confirm Password:",font=("times new roman",16,"bold"))
        user_confPs.grid(row=8,column=0,padx=30,pady=10,sticky=W)

        CP_Entry=ttk.Entry(main_frame,textvariable=self.confirm_var,font=("arial",15),width=22)
        CP_Entry.grid(row=8,column=1,padx=5,pady=10,sticky=W)

        
        #button Frame
        

        saveBtn=Button(main_frame,text="Submit",font=("arial",10,"bold"),width=15,cursor="hand2",bg="white",command=self.validation)
        saveBtn.place(x=300,y=450,height=50,width=150)

      
        self.root.mainloop()

    def verify_data(self):
            data=f"Name:{self.name_var.get()} \nEmail Id:{self.email_var.get()} \nContact number:{self.contact_var.get()} \nGender:{self.gender_var.get()} \nCountry:{self.country_var.get()} \nID Proof:{self.id_var.get()} \nID No.:{self.idNo_var.get()} \nPassword:{self.password_var.get()} \n"
            messagebox.showinfo("Details",data)    

    def clear(self):
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.gender_var.set("no")
        self.country_var.set("Select country")
        self.id_var.set("Select your ID")
        self.idNo_var.set("")
        self.password_var.set("")
        self.confirm_var.set("")
        self.check_var(0)

    
    
    def checkornot(self):
        if self.check_var.get()==0:
            self.chk_lbl.config(text="Please agree Terms and conditions",fg="red")
           
        else:
            self.chk_lbl.config(text="Checked",fg="green")
           
            

    #call back function
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=="":
            return True
        else:
            messagebox.showerror("Invalid","Not allowed")
            return False

    def checkContact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror("Invalid","Invalid Entry")
            return False
        
    def checkPassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])",self.password):
                return True
            else:
                messagebox.showinfo("Invalid","Enter valid password  ")
                return False
        else:
            messagebox.showerror("Invalid","Length try to execeed")
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
                self.engine.say("Please enter your name")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please enter your name",parent=self.root)
                
            elif self.email_var.get()=="":
                self.engine.say("Please enter your email id")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please enter your email id",parent=self.root)


            elif self.gender_var.get()=="":
                self.engine.say("Please select gender")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please select gender",parent=self.root)    

            elif self.country_var.get()=="":
                self.engine.say("Please select country")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please select country",parent=self.root)    

            elif self.id_var.get()=="":
                self.engine.say("Please enter select id")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please select id",parent=self.root)   

            elif self.idNo_var.get()=="":
                self.engine.say("Please enter id Number")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please Enter id No.",parent=self.root)
            
            elif len(self.idNo_var.get())!=14:
                self.engine.say("Please enter 14 digit")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please enter 14 digit",parent=self.root)    
        
            elif self.password_var.get()=="":
                self.engine.say("Please enter your password")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please enter password",parent=self.root)   

            elif self.confirm_var.get()=="":
                self.engine.say("Please enter confirm password")
                self.engine.runAndWait()
                messagebox.showerror("Error","Please confirm password",parent=self.root)    

            elif self.password_var.get() !=  self.confirm_var.get():
                self.engine.say("Password and confirm password must be same")
                self.engine.runAndWait()
                messagebox.showerror("Error","Password and confirm password are not matching",parent=self.root)    
        
            
            elif self.email_var.get()!=None and self.password_var.get()!=None:
                x=self.checkemail(self.email_var.get())
                y=self.checkPassword(self.password_var.get())

        except:
          
            messagebox.showinfo("Successfully",f"Your registration successfully completed.Username is={self.name_var.get()} and password is ={self.password_var.get()}",parent=self.root)
              
    def connect(self):
        con=pymysql.connect(host="localhost",user='root',password='',database='hotel_managementdb')
        cur=con.cursor()
        cur.execute("Insert into userinfo(Name,Email,Contact_No,Gender,Country,ID_Proof,ID_No,Password) values (%s,%s,%s,%s,%s,%s,%s,%s)",({self.name_var.get()},{self.email_var.get()},{self.contact_var.get()},{self.gender_var.get()},{self.country_var.get()},{self.id_var.get()},{self.idNo_var.get()},{self.password_var.get()}))
        con.commit()
        print(cur.rowcount,"Record inserted")

        


def second():
    root=Tk()
    obj=Register(root=root)
    obj.connect()
    root.mainloop()
 
if __name__=="__main__":
    second()