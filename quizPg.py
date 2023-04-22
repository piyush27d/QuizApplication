

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkinter import messagebox




class display:

    def __init__(self,root) :
          # super().__init__(self,root)
        self.root=root
        self.root.title("Quiz page")
        self.root.state("zoomed")
        self.out_of=0
        self.option_var=StringVar()
        self.op1=StringVar()
        self.op2=StringVar()
        self.op3=StringVar()
        self.op4=StringVar()
        self.count=0
        

        self.db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_quiz")

        self.question_num=StringVar()

        self.question_text=StringVar()
        self.queNO=StringVar()
        self.row=StringVar()
        global userAns
        correctAns=StringVar()
        userAns=StringVar()

      # Create a cursor object to interact with the database
        cursor = self.db.cursor()        
        self.question_num = 1

        cursor.execute("select ID from create_quiz_tb")
        self.UserName_rows=cursor.fetchall()
        self.out_of=len(self.UserName_rows)

        query = "SELECT * FROM create_quiz_tb WHERE ID = %s"
        cursor.execute(query, (self.question_num,))   

        row = cursor.fetchone()
        # quNO_db.config(text=self.queNO)
        self.queNO=row[0]
        self.question_text=row[1]
        self.op1=row[2]
        self.op2=row[3]
        self.op3=row[4]
        self.op4=row[5]
        

        # Define function to check answer and move to next question
        def next_question(answer):
          
          print(self.out_of)
          print()

          
          if self.out_of>=(self.question_num +1):
            
            self.ans()
            self.question_num += 1
            print(self.question_num )
            
            
            query = "SELECT * FROM create_quiz_tb WHERE ID = %s"
            cursor.execute(query, (self.question_num,))

            self.row = cursor.fetchone()

            quNO_db.config(text=self.row[0])
            que_db.config(text=self.row[1])
            self.rdo1.config(text=self.row[2])
            self.rdo2.config(text=self.row[3])
            self.rdo3.config(text=self.row[4])
            self.rdo4.config(text=self.row[5]) 

            self.op1=self.row[2]
            self.op2=self.row[3]
            self.op3=self.row[4]
            self.op4=self.row[5]
            
            self.rdo1.config(value=self.row[2])
            self.rdo2.config(value=self.row[3])
            self.rdo3.config(value=self.row[4])
            self.rdo4.config(value=self.row[5]) 

            # self.op1.set(str=self.row[2])
            # self.op2.set(str=self.row[3])
            # self.op3.set(str=self.row[4])
            # self.op4.set(str=self.row[5])
            

            # self.rdo1.config(variable=self.option_var)
            # self.rdo2.config(variable=self.option_var)
            # self.rdo3.config(variable=self.option_var)
            # self.rdo4.config(variable=self.option_var)
            # return self.op1,self.op2,self.op3,self.op4
          
          else:
             #count=self.count.get()
             
             self.ans()
             data=f"your score is: {self.count} out of:{self.out_of}"
             messagebox.showinfo("info",data)
             exit(0)
        
                  
              
        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg)
        bgLbl.place(height=900,width=1600,x=0,y=0)
        
        quNO=Label(self.root,text="Que No: ",font=("Times new roman",20,"bold"),bg="white",fg="black")
        quNO.place(x=110,y=100)

        quNO_db=Label(self.root,text=self.queNO,font=("Times new roman",20,"bold"),bg="white",fg="black")
        quNO_db.place(x=230,y=100,height=40,width=50)

        que_db=Label(self.root,text=self.question_text,font=("Times new roman",20,"bold"),bg="white",fg="black")
        que_db.place(x=300,y=100,height=90,width=1000)

        
      #   #option frame
        option_Frame=Frame(self.root)
        option_Frame.place(x=300,y=200,width=280,height=400)
        self.rdo1=Radiobutton(option_Frame,variable=self.option_var,value=self.op1,text=self.op1,font=("times new roman",15))
        self.rdo1.grid(row=0,column=0,padx=10,pady=25,sticky=W)
        
        self.rdo2=Radiobutton(option_Frame,variable=self.option_var,value=self.op2,text=self.op2,font=("times new roman",15))
        self.rdo2.grid(row=1,column=0,padx=10,pady=25,sticky=W)

        self.rdo3=Radiobutton(option_Frame,variable=self.option_var,value=self.op3,text=self.op3,font=("times new roman",15))
        self.rdo3.grid(row=2,column=0,padx=10,pady=25,sticky=W)

        self.rdo4=Radiobutton(option_Frame,variable=self.option_var,value=self.op4,text=self.op4,font=("times new roman",15),)
        self.rdo4.grid(row=3,column=0,padx=10,pady=25,sticky=W)
        
        self.option_var.set("No")
        
      
      #
        nxtBtn = Button(self.root,text="NEXT",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray",command=lambda answer=correctAns: next_question(answer))
        nxtBtn.place(x=350,y=610,height=40,width=140)
      
        clr_btn=Button(self.root,text="CLEAR",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray",command=self.clear_fun)
        clr_btn.place(x=750,y=610,height=40,width=140)
      #submit
        Submit_btn=Button(self.root,text="SUBMIT",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray")
        Submit_btn.place(x=1100,y=610,height=40,width=140)
    
    def clear_fun(self):
        self.option_var.set("no")

    def back_fun(self):
        # from main_page import display
        a=display(self.root)

    def next_fun(self):
       pass

    def ans(self):
       
        
        cursor = self.db.cursor() 

        
       

        query = "SELECT Answer FROM create_quiz_tb WHERE ID = %s"
        cursor.execute(query, (self.question_num,))
        correctAns = cursor.fetchone()

        userAns=self.option_var.get()
        print(correctAns[0])
        print(self.option_var.get())
        if userAns==correctAns[0]:
            print("correct")
            
            self.count=self.count+1
            
        else:
            print("Wrong")
        print(self.option_var.set("None" ) )  
        self.option_var.set("no")
        

def displaymain():
   root=Tk()
   d=display(root)   
   #d.connection()   
   
   root.mainloop()




if __name__=="__main__":
   displaymain()

