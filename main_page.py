from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from new_registration_page import new_registration
#from Admin_page import admin
from create_admin import admin_page
import pymysql
from tkinter import messagebox

class display:
    def __init__(self,root) :
          # super().__init__(self,root)
        self.root=root
        self.root.title("User Registration page")
        self.root.state("zoomed")
        #self.root.geometry("1920x1080+0+0")

        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)

        self.email=StringVar()
        self.pwd=StringVar()
        self.id=StringVar()
        self.username=StringVar()


        logoImg=Image.open("logo.jpg")
        logoImg=logoImg.resize((100,100),Image.ANTIALIAS)
        self.LogoPhoto=ImageTk.PhotoImage(logoImg)

        title_frame=Frame(self.root,relief=RIDGE,bg="black")
        title_frame.place(x=40,y=30,width=1470,height=100)

        titleLbl=Label(title_frame,image=self.LogoPhoto,compound=LEFT)
        titleLbl.place(x=0,y=0)

        ttlHeading=Label(title_frame,text="Quiz Making Application",font=("Times new roman",20,"bold"),bg="black",fg="white")
        ttlHeading.place(x=110,y=30)

        frame1=Frame(self.root,height=500,width=700,background="white").place(x=40,y=250)
        textFrame=Frame(frame1,relief=RAISED,bd=2)
        text=Text(textFrame,height=25,width=165,font=("arial",13))
        txtEmbed=open("show.txt","r")
        lines=txtEmbed.read()
        txtEmbed.close()
        text.insert(END,lines)
        text.configure(state='disabled')
        text.place(x=0,y=0,height=500,width=700)
        textFrame.place(x=40,y=250,height=500,width=700)

        #hadder_name.place(x=1000,y=250)
       # ttk.Style().configure("TButton",padding=6,relief="flat",background="#0000")
      # frame1=Frame()

        #frame2 
        login   =Button(self.root,text="LOGIN",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray",command=self.login_fun)
        login.grid(row=0,column=1,padx=40,pady=160)
       
        register=Button(self.root,text="REGISTER",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray",command=self.register_fun)
        register.grid(row=0,column=2,padx=50,pady=160)
       
        create  =Button(self.root,text="CREATE NEW QUIZ",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray",command=self.create_fun)
        create.grid(row=0,column=3,padx=50,pady=160)
       
      #   result  =Button(self.root,text="RESULT",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray")
      #   result.grid(row=0,column=4,padx=50,pady=160)
      
      #   forstd   =Button(self.root,text="FOR STUDENT",font=("arial",13,"bold"),width=15,cursor="hand2",bg="white",activebackground="gray").grid(row=0,column=5,padx=50,pady=160)
      
        exit  =Button(self.root,text="EXIT",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray",command=self.exit_fun)
        exit.grid(row=0,column=6,padx=50,pady=160)
               
         
        self.frame2=Frame(self.root,height=500,width=700,background="white").place(x=800,y=250)

        stdtittle = Label(self.frame2, text="Student section", font=("times new roman",28, "bold"))
        stdtittle.place(x=1000,y=250)

        
        #id 
        id=Label(self.frame2,text="TOPIC:",font=("times new roman",16,"bold"))
        id.place(x=850,y=330)
        
        id_Entry=ttk.Entry(self.frame2,textvariable=self.id,font=("arial",15),width=22)
        id_Entry.place(x=950,y=330)

      
      #password
        pwd=Label(self.frame2,text="password:",font=("times new roman",16,"bold"))
        pwd.place(x=850,y=380)
        
        pwd_Entry=ttk.Entry(self.frame2,font=("arial",15),textvariable=self.pwd,width=22)
        pwd_Entry.place(x=950,y=380)

      #username
        user_name=Label(self.frame2,text="Username:",font=("times new roman",16,"bold"))
        user_name.place(x=850,y=430)
        
        userName_Entry=ttk.Entry(self.frame2,textvariable=self.username,font=("arial",15),width=22)
        userName_Entry.place(x=950,y=430)

      #email
        email=Label(self.frame2,text="Email:",font=("times new roman",16,"bold"))
        email.place(x=850,y=480)
        
        email_Entry=ttk.Entry(self.frame2,font=("arial",15),textvariable=self.email,width=22)
        email_Entry.place(x=950,y=480)

        Start_quiz  =Button(self.root,text="START QUIZ",font=("arial",15,"bold"),width=20,cursor="hand2",bg="white",activebackground="gray",bd=5,background="sky blue",command=self.start_quiz_fun)
        Start_quiz.place(x=1000,y=550)
         

    #Buttons

    def connection(self):
        conn=pymysql.connect(host="localhost",user="root",password="root",database="db_quiz")
        cur=conn.cursor()  
        cur.execute("Insert into stud_details(username,Email_id) values(%s,%s)",({self.username.get()},{self.email.get()})) 
        conn.commit()
    
    def login_fun(self):
       from login_page import loginPage
       loginPage(self.root)

    def register_fun(self):
       new_registration(self.root)
      
    def create_fun(self):
       admin_page(self.root)

   
    
    def start_quiz_fun(self):
         if( self.id.get()=="" or self.pwd.get()=="" or self.username.get()=="" or self.email.get()==""):      
            if self.id.get()=="":
                messagebox.showerror("Error","Please enter QUIZ ID",parent=self.root)  

            elif self.pwd.get()=="":
                messagebox.showerror("Error","Please enter PASSWORD",parent=self.root)    

            elif self.username.get()=="":
                messagebox.showerror("Error","Please enter USERNAME",parent=self.root)
                
            elif self.email.get()=="":
                messagebox.showerror("Error","Please enter EMAIL ID",parent=self.root)

         else:

            #self.connection()
            username = self.id.get()
            password = self.pwd.get()
                     
            conn=pymysql.connect(host="localhost",user="root",password="root",database="db_quiz")
            cur=conn.cursor() 

            cur.execute("SELECT Password1 FROM admin_tb WHERE name1=%s", (username,))
            result = cur.fetchone()
            # print(result)
            
            # Check if the entered password matches the one in the database
            if result and result[0] == password:
                  #print(result[0])
               # message_label.config(text="Login successful!")
                  self.connection()
                  messagebox.showinfo("login","Login sucessfully") 
                  from quizPg import display
                  a=display(self.root) 
            else:
                  #message_label.config(text="Incorrect username or password.")
                  messagebox.showerror("login","Login id or Password incorrect")  
    def exit_fun(self):
       exit(0)
      
def displaymain():
   root=Tk()   
   d=display(root)  
   root.mainloop()

       
       
if __name__=="__main__":
   displaymain()

