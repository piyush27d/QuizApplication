from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pymysql
from tkinter.messagebox import showinfo
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
import re

class display:
    def __init__(self,root) :
        #super().__init__(self,root)
        self.root=root
        self.root.title("Admin page")
        self.root.state("zoomed")

        # variables
        self.ID_var=StringVar()
        self.topicName_var=StringVar()
        self.pass_var=StringVar()

        self.que_var=StringVar()
        self.opt1_var=StringVar()
        self.opt2_var=StringVar()
        self.opt3_var=StringVar()
        self.opt4_var=StringVar()
        self.ans_var=StringVar()

        self.search_var=StringVar()

        

        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)

        #Fame1
        self.frame1=Frame(self.root,relief=RIDGE)
        self.frame1.place(x=50,y=50,width=1430,height=125)

        # Admin name
        admin_name = Label(self.frame1, text="Admin Name:", font=("times new roman", 16, "bold"))
        admin_name.grid(row=1, column=1, padx=30, pady=10, sticky=W)

        self.name_frame=Frame(self.frame1,relief=RIDGE,bg="gray")
        self.name_frame.place(y=10,x=170,height=30,width=150)


        # # Admin email
        # email_name = Label(self.frame1, text="Email:", font=("times new roman", 16, "bold"))
        # email_name.grid(row=1, column=3, padx=30, pady=10, sticky=W)
        
        # #Upload image
        # uploadL = Label(self.frame1,font=("times new roman", 16, "bold"))  
        # uploadL.grid(row=2,column=1, padx=30, pady=10, sticky=W)
        
        # UpldBtn = Button(self.frame1, text='Upload Image',width=15,command = lambda:self.upload_file())
        # UpldBtn.grid(row=2,column=2, padx=5, pady=10, sticky=W)

        
        #Result button
        #crtBtn=Button(self.frame1,text="RESULT",font=("arial",10,"bold"),width=10,cursor="hand2",bg="white",activebackground="gray").grid(row=2,column=4, padx=10, pady=5, sticky=W)

        """# search section
        srLbl=Label(self.frame1,text="Search",font=("arial",10,"bold"))
        srLbl.grid(row=2,column=5,padx=10,pady=10,sticky=W)
        srentry=Entry(self.frame1,textvariable=self.search_var,width=30)
        srentry.grid(row=2,column=6, padx=5, pady=10, sticky=W)
        srchBtn=Button(self.frame1,text="Search",command=self.search)
        srchBtn.grid(row=2,column=7, padx=5, pady=10, sticky=W)"""

        
        #Frame 2
        frame2=Frame(self.root,relief=RIDGE)
        frame2.place(x=50,y=200,width=700,height=240)

        self.tv=ttk.Treeview(frame2,columns=(1,2,3,4,5,6),show="headings",height=10)    #headings

        self.tv.heading(1,text="ID")                                                    #heading
        self.tv.heading(2,text="QUIZ NAME")
        self.tv.heading(3,text="DATE OF CREATION")
        self.tv.heading(4,text="REGISTERED")
        self.tv.heading(5,text="PARTICIPATED")
        self.tv.heading(6,text="DATE OF QUIZ")

        self.tv["show"]="headings"
        self.tv.place(x=10,y=20,height=200,width=680)
        
        self.tv.column(1,width=5)
        self.tv.column(2,width=20)
        self.tv.column(3,width=25)
        self.tv.column(4,width=20)        
        self.tv.column(5,width=20)
        self.tv.column(6,width=20)
    
        

        #Frame 3
        frame3=Frame(self.root,relief=RIDGE)
        frame3.place(x=50,y=430,width=700,height=250)

        # ID
        id_name = Label(frame3, text="ID:", font=("times new roman", 13, "bold"))
        id_name.grid(row=0, column=0, padx=30, pady=10, sticky=W)
        id_Entry = ttk.Entry(frame3,textvariable=self.ID_var, font=("arial", 10), width=27)
        id_Entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # Quiz name
        topic = Label(frame3, text="TOPIC:", font=("times new roman", 13, "bold"))
        topic.grid(row=1, column=0, padx=30, pady=10, sticky=W)
        topic_Entry = ttk.Entry(frame3,textvariable=self.topicName_var, font=("arial", 10), width=27)
        topic_Entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        #dATE
        paswrd=Label(frame3,text="PASSWORD:",font=("times new roman", 13, "bold"))
        paswrd.grid(row=2, column=0, padx=30, pady=5, sticky=W) 
        q_Entry = ttk.Entry(frame3,textvariable=self.pass_var,show="*", font=("arial", 10), width=27)
        q_Entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

       
        #create button
        crtBtn=Button(frame3,text="CREATE QUIZ",font=("arial",10,"bold"),width=20,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=4,column=0, padx=15, pady=15, sticky=W)
        
        #Update button
        updtBtn=Button(frame3,text="UPDATE QUIZ",font=("arial",10,"bold"),width=20,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=4,column=1, padx=15, pady=15, sticky=W)
        
        #delete button
        dltBtn=Button(frame3,text="DELETE QUIZ",font=("arial",10,"bold"),width=20,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=4,column=2, padx=15, pady=15, sticky=W)




        #frame 4
        frame4=Frame(self.root,relief=RIDGE)
        frame4.place(x=780,y=200,width=700,height=350)

        self.variable=StringVar()
        self.variable.set("Que No.")
        drop=OptionMenu(frame4,self.variable,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,command=self.getQno)
        drop.grid(row=0, column=0, padx=5, pady=15, sticky=W)

        que = Label(frame4, text="Que:", font=("times new roman", 15, "bold"))
        que.grid(row=0, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.que_var, font=("arial", 15), width=45)
        que_Entry.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        que = Label(frame4, text="Option1", font=("times new roman", 15, "bold"))
        que.grid(row=1, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt1_var, font=("arial", 15), width=15)
        que_Entry.grid(row=1, column=2, padx=15, pady=15, sticky=W)

        que = Label(frame4, text="Option2", font=("times new roman", 15, "bold"))
        que.grid(row=2, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt2_var, font=("arial", 15), width=15)
        que_Entry.grid(row=2, column=2, padx=15, pady=15, sticky=W)

        que = Label(frame4, text="Option3", font=("times new roman", 15, "bold"))
        que.grid(row=3, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt3_var, font=("arial", 15), width=15)
        que_Entry.grid(row=3, column=2, padx=15, pady=15, sticky=W)

        que = Label(frame4, text="Option4", font=("times new roman", 15, "bold"))
        que.grid(row=4, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt4_var, font=("arial", 15), width=15)
        que_Entry.grid(row=4, column=2, padx=15, pady=15, sticky=W)

        que = Label(frame4, text="Answer", font=("times new roman", 15, "bold"))
        que.grid(row=5, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.ans_var, font=("arial", 15), width=15)
        que_Entry.grid(row=5, column=2, padx=15, pady=15, sticky=W)


        #frame5
        frame5=Frame(self.root,relief=RIDGE)
        frame5.place(x=780,y=550,width=700,height=130)

        updBtn=Button(frame5,text="UPDATE",font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=1,column=1,padx=5,pady=30,sticky=W)
        deleteBtn=Button(frame5,text="DELETE",font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=1,column=2,padx=5,pady=30,sticky=W)
        saveBtn=Button(frame5,text="SAVE",font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.save).grid(row=1,column=3,padx=5,pady=30,sticky=W)
        updBtn=Button(frame5,text="ADD QUE",font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=1,column=4,padx=5,pady=30,sticky=W)
        clrBtn=Button(frame5,text="CLEAR",font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.cLear).grid(row=1,column=5,padx=5,pady=30,sticky=W)

        

    #clear function
    def cLear(self):
        self.que_var.set('')
        self.opt1_var.set('')
        self.opt2_var.set('')
        self.opt3_var.set('')
        self.opt4_var.set('')
        self.ans_var.set('')      
        self.delete(1,0,END)

    def getQno(self,a):
        
        
        con=pymysql.connect(host="localhost",user='root',password='',database='db_quiz')
        cur=con.cursor()
        
        cur.execute("Select * from create_quiz_tb where ID=%s",(self.variable.get(),))
        row=cur.fetchone()
        # print(row)
        # que(text=row[0])
        # self.que_Entry.set(row)
        self.opt1_var.set(row[0])
        self.opt2_var.set(row[1])
        self.opt3_var.set(row[2])
        self.opt4_var.set(row[3])
        self.ans_var.set(row[4])
        


    """def search(self):
        con=pymysql.connect(host="localhost",user='root',password='',database='db_quiz')
        cur=con.cursor()
        
        srch=self.search_var.get()
        qry=f"Select ID,Name,DOM,Registered_candidate,Participated_cadidate,DOQ from admin_tb where ID "       
        value=[(self.ID_var.get())]
        cur.execute(qry,value)
        rows=cur.fetchall()
        print("it works")
        # update(rows)"""




    def validation(self):  
        try:      
            if self.ID_var.get()=="":                
                messagebox.showerror("Error","Please enter ID",parent=self.root)
                
            elif self.topicName_var.get()=="":                
                messagebox.showerror("Error","Please enter topic name",parent=self.root)

            elif self.pass_var.get()=="":                
                messagebox.showerror("Error","Please enter password",parent=self.root)

           

        except:            
            messagebox.showinfo("Successful","Data filled successfully...!")

    #for_Quetion
    def save(self):  
        try:      
            if self.que_var.get()=="":                
                messagebox.showerror("Error","Please enter Quetion",parent=self.root)
                
            elif self.opt1_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 1",parent=self.root)

            elif self.opt2_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 2",parent=self.root)

            elif self.opt3_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 3",parent=self.root)

            elif self.opt4_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 4",parent=self.root)

            elif self.ans_var.get()=="":                
                messagebox.showerror("Error","Please enter Answer",parent=self.root)

           

        except:            
            messagebox.showinfo("Data filled successfully...!",parent=self.root)

            
        

    """def conn(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        
        cur.execute("Select ID,Name,DOM,Registered_candidate,Participated_cadidate,DOQ from admin_tb ")
        row=cur.fetchall()
        for i in row:
            self.tv.insert("","end",values=i)
        
       
    """
    """def getRows(self,event):
        rowid=self.tv.identify_row(event.y) 
        item=self.tv.item(self.tv.focus())
        print(item["values"][0])"""

    """def create(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        cur.execute("Insert into admin_tb(ID,Name,DOM,Registered_candidate,Participated_cadidate,DOQ) values (%s,%s,%s,%s,%s,%s)",({self.ID_var.get()},{self.quizName_var.get()},{self.DOM_var.get()},{self.regist_var.get()},{self.participated_var.get()},{self.DOQ_var.get()}))
        con.commit()
        # con.close()
        # self.conn()
        #print(cur.rowcount,"Record inserted")          

    def update(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        UpdtQry="Update admin_tb SET ID=%s,Name=%s ,DOM=%s,Registered_candidate=%s,Participated_cadidate=%s,DOQ=%s where ID=%s"
        value=({self.ID_var.get()},{self.quizName_var.get()},{self.DOM_var.get()},{self.regist_var.get()},{self.participated_var.get()},{self.DOQ_var.get()},{self.ID_var.get()})
        cur.execute(UpdtQry,value)
        con.commit()
        # con.close()
        # self.conn()
        #print(cur.rowcount,"Record updated") 


    def delete(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()  
        DltQry="Delete from admin_tb where ID=%s"
        value=[(self.ID_var.get())]
        cur.execute(DltQry,value)
        con.commit()
        # con.close()
        # self.conn()
        print(cur.rowcount,"Record deleted")
  

    
    """
    '''def upload_file(self):
        
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]                # type of files to select 
        filename =filedialog.askopenfilename(multiple=True,filetypes=f_types)
        
        for f in filename:
            img=Image.open(f)               # read the image file
            img=img.resize((60,60))         # new width & height            
            img=ImageTk.PhotoImage(img)
            e1 =Label(self.frame1,text="img")
            e1.grid(row=2,column=1)
            e1.image = img                  # keep a reference! by attaching it to a widget attribute
            e1['image']=img                 # Show Image  
        '''    
def second():
    root=Tk()
    obj=display(root=root)
    #obj.conn()
    # obj.getRows("click")
    #obj.validation()
    root.mainloop()
    
if __name__=="__main__":
    second()
    