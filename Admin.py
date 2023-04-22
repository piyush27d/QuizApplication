from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import pymysql
from tkinter.messagebox import showinfo , askyesno
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
import re
import datetime as dt
import mysql.connector

class display:
    def __init__(self,root,id="" ):
        #super().__init__(self,root)
        self.root=root
        self.root.title("Admin page")
        self.root.state("zoomed")

        # variables
        self.ID_var=StringVar()
        self.topicName_var=StringVar()
        self.pass_var=StringVar()
        #self.id=StringVar()
        self.id=id
        self.que_var=StringVar()
        self.opt1_var=StringVar()
        self.opt2_var=StringVar()
        self.opt3_var=StringVar()
        self.opt4_var=StringVar()
        self.ans_var=StringVar()
        self.search_var=StringVar()
        self.totalNoQue=StringVar()

        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)


        #Fame1
        self.frame1=Frame(self.root,relief=RIDGE)
        self.frame1.place(x=50,y=50,width=1430,height=125)

        # Admin name
        admin_name = Label(self.frame1, text="Admin Name:", font=("arial", 16, "bold"))
        admin_name.grid(row=1, column=0, padx=10, pady=10, sticky=W)
               
        admin_name = Label(self.frame1, text=self.id, font=("arial", 16, "bold"))
        admin_name.grid(row=1, column=1, padx=10, pady=10, sticky=W)
       
               
        # search section
        srLbl=Label(self.frame1,text="Search by topic",font=("arial",14,"bold"))
        srLbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        srentry=Entry(self.frame1,textvariable=self.search_var,width=20,bd=5,font=("arial", 14))
        srentry.grid(row=2,column=1, padx=5, pady=10, sticky=W)
        
        srchBtn=Button(self.frame1,text="Search",command=self.search,font=("arial",14),width=10,height=1)
        srchBtn.grid(row=2,column=2, padx=5, pady=10, sticky=W)

        #back button
        
        back=Button(self.frame1,text="Back",font=("arial",15,"bold"),width=15,cursor="hand2",bg="white",activebackground="gray",command=self.back_fun).place(x=700,y=10,height=50,width=150)

        
        #Frame 2
        frame2=Frame(self.root,relief=RIDGE)
        frame2.place(x=50,y=200,width=700,height=240)
        
        scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.tv=ttk.Treeview(frame2,columns=(1,2,3),show="headings",height=10,xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
        scroll_x=ttk.Scrollbar(command=self.tv.xview)
        scroll_y=ttk.Scrollbar(command=self.tv.yview)    

        self.tv.heading(1,text="ID")                                                    #heading
        self.tv.heading(2,text="TOPIC NAME")
        self.tv.heading(3,text="NUMBER OF QUETION")
        
        self.tv["show"]="headings"
        self.tv.place(x=0,y=0,height=200,width=700)
        
        self.tv.column(1,width=25)
        self.tv.column(2,width=25)
        self.tv.column(3,width=25)
        #on double click data display on entry widget
        self.tv.bind("<Double 1>",self.getRows)

        #Frame 3
        frame3=Frame(self.root,relief=RIDGE)
        frame3.place(x=50,y=445,width=700,height=300)

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

        #password
        paswrd=Label(frame3,text="PASSWORD:",font=("times new roman", 13, "bold"))
        paswrd.grid(row=2, column=0, padx=30, pady=5, sticky=W) 
        q_Entry = ttk.Entry(frame3,textvariable=self.pass_var,show="*", font=("arial", 10), width=27)
        q_Entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        # total que
        totalQue = Label(frame3, text="TOTAL QUETION :", font=("times new roman", 13, "bold"))
        totalQue.grid(row=3, column=0, padx=30, pady=10, sticky=W)
        totalQue = ttk.Entry(frame3,textvariable=self.totalNoQue, font=("arial", 10), width=27)
        totalQue.grid(row=3, column=1, padx=5, pady=10, sticky=W)
       
       
        #create button
        crtBtn=Button(frame3,text="CREATE QUIZ",font=("arial",10,"bold"),width=20,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.create).grid(row=4,column=0, padx=15, pady=15, sticky=W)
        
        #Update button
        updtBtn=Button(frame3,text="UPDATE QUIZ",font=("arial",10,"bold"),width=20,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=4,column=1, padx=15, pady=15, sticky=W)
        
        #delete button
        dltBtn=Button(frame3,text="DELETE QUIZ",font=("arial",10,"bold"),width=20,cursor="hand2",bg="LIGHT BLUE",activebackground="gray").grid(row=4,column=2, padx=15, pady=15, sticky=W)


        # datetime
        # Create an instance of datetime module
        date=dt.datetime.now()
        # Format the date
        format_date=f"{date: %b %d %Y}"
        # Display the date in a a label widget
        label=Label(frame3, text=format_date, font=("arial", 15))   #"Calibri"
        label.grid(row=0,column=2, padx=0, pady=15, sticky=W)

       
        #frame 4
        frame4=Frame(self.root,relief=RIDGE)
        frame4.place(x=780,y=200,width=700,height=410)       

        self.variable=StringVar()
        self.variable.set("Q No.:")
        self.drop=OptionMenu(frame4,self.variable,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,command=self.getQno)
        self.drop.grid(row=0, column=0, padx=5, pady=1, sticky=W)

        #self.drop.bind("<Double 1>",self.getquestions)

        que = Label(frame4, text="Q:", font=("times new roman", 15, "bold"))
        que.grid(row=0, column=1, padx=3, pady=5, sticky=W)

        self.que_Entry = Text(frame4, font=("arial", 15), width=32,height=2)      # unknown option "-variable"
        self.que_Entry.get("1.0","end")
        
        self.que_Entry.grid(row=0, column=2, padx=5,pady=5, sticky=W)

        que = Label(frame4, text="Option1", font=("times new roman", 15, "bold"))
        que.grid(row=1, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt1_var, font=("arial", 15), width=15)
        que_Entry.grid(row=1, column=2, padx=5, pady=15, sticky=W)

        que = Label(frame4, text="Option2", font=("times new roman", 15, "bold"))
        que.grid(row=2, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt2_var, font=("arial", 15), width=15)
        que_Entry.grid(row=2, column=2, padx=5, pady=15, sticky=W)

        que = Label(frame4, text="Option3", font=("times new roman", 15, "bold"))
        que.grid(row=3, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt3_var, font=("arial", 15), width=15)
        que_Entry.grid(row=3, column=2, padx=5, pady=15, sticky=W)

        que = Label(frame4, text="Option4", font=("times new roman", 15, "bold"))
        que.grid(row=4, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.opt4_var, font=("arial", 15), width=15)
        que_Entry.grid(row=4, column=2, padx=5, pady=15, sticky=W)

        que = Label(frame4, text="Answer", font=("times new roman", 15, "bold"))
        que.grid(row=5, column=1, padx=3, pady=5, sticky=W)
        que_Entry = ttk.Entry(frame4,textvariable=self.ans_var, font=("arial", 15), width=15)
        que_Entry.grid(row=5, column=2, padx=5, pady=15, sticky=W)
           
        frame5=Frame(self.root,relief=RIDGE)
        frame5.place(x=780,y=610,width=700,height=130)
        #upt button
        ubtBtn=Button(frame5,text="UPDATE QUETION",bd=5,font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.edit).grid(row=0,column=0, padx=10, pady=15, sticky=W)
        
        #clear button
        clear=Button(frame5,text="CLEAR QUESTION",bd=5,font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.clear).grid(row=0,column=1, padx=10, pady=15, sticky=W)
        

        #save button
        SaveBtn=Button(frame5,text="SAVE QUESTION",bd=5,font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.save).grid(row=0,column=2, padx=10, pady=15, sticky=W)
        
        #delete button
        dltBtn=Button(frame5,text="DELETE QUESTION",bd=5,font=("arial",10,"bold"),width=15,cursor="hand2",bg="LIGHT BLUE",activebackground="gray",command=self.delete).grid(row=0,column=3, padx=10, pady=15, sticky=W)

        self.conn()

    # def getquestions(self,event):
    #     rowid=self.drop.identify_row(event.y) 
    #     item=self.drop.item(self.drop.focus())
    #     #print(item["values"][0])
    #     self.opt1_var.set(item["values"][0])
    #     self.opt2_var.set(item["values"][1])
    #     self.opt3_var.set(item["values"][2])
    #     self.opt4_var.set(item["values"][3])
    #     self.ans_var.set(item["value"][4])

    def back_fun(self):
        from main_page import display
        a=display(self.root)

    def search(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        
        getS=self.search_var.get()
        qry="Select ID,name1 from admin_tb where name1 LIKE '%"+getS+"%' "       
        cur.execute(qry)
        rows=cur.fetchall()
        # print("it works")
        self.searchrow(rows)

    def searchrow(self,rows):
        self.tv.delete(*self.tv.get_children())  
        for i in rows:
            self.tv.insert("","end",values=i)

    def save(self):  
        if(self.opt1_var.get()=="" or self.opt2_var.get()=="" or self.opt3_var.get()=="" or self.opt4_var.get()=="" or self.ans_var.get()==""):      
            # if self.que_var.get()=="":                
            #     messagebox.showerror("Error","Please enter Quetion",parent=self.root)
                
            if self.opt1_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 1",parent=self.root)

            elif self.opt2_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 2",parent=self.root)

            elif self.opt3_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 3",parent=self.root)

            elif self.opt4_var.get()=="":                
                messagebox.showerror("Error","Please enter Option 4",parent=self.root)

            elif self.ans_var.get()=="":                
                messagebox.showerror("Error","Please enter Answer",parent=self.root)

        else: 
           # print("sss")           
            try:
                con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
                cur=con.cursor()
                cur.execute("Insert into create_quiz_tb(ID,Question,Option1,Option2,Option3,Option4,Answer) values (%s,%s,%s,%s,%s,%s,%s)",({self.variable.get()},{self.que_Entry.get("1.0","end")},{self.opt1_var.get()},{self.opt2_var.get()},{self.opt3_var.get()},{self.opt4_var.get()},{self.ans_var.get()}))
                con.commit()
                messagebox.showinfo("info","Data filled successfully...!",parent=self.root)
            except:
                print(TypeError)
                # print("hh")

           



    """def validation(self):  
        try:      
            if self.ID_var.get()=="":                
                messagebox.showerror("Error","Please enter ID",parent=self.root)
                
            elif self.topicName_var.get()=="":                
                messagebox.showerror("Error","Please enter topic name",parent=self.root)

            elif self.pass_var.get()=="":                
                messagebox.showerror("Error","Please enter password",parent=self.root)

           

        except:            
            # messagebox.showinfo("Successful","Data filled successfully...!")
            pass"""
        

    def conn(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        
        cur.execute("Select * from admin_tb ")
        row=cur.fetchall()
        for i in row:
            self.tv.insert("","end",values=i)
    
    def getQno(self,a):
        
        
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        
        cur.execute("Select * from create_quiz_tb where ID=%s",(self.variable.get(),))
        
        # data = cur.fetchone()[1]
        # self.que_Entry.insert(END,f"{data}\n")

        row=cur.fetchone()
        # print(row)
       # que(text=row[0])
        try:
            self.que_Entry.delete("1.0","end")
            self.opt1_var.set("")
            self.opt2_var.set("")
            self.opt3_var.set("")
            self.opt4_var.set("")
            self.ans_var.set("")

            self.que_Entry.insert(END,row[1])
            self.opt1_var.set(row[2])
            self.opt2_var.set(row[3])
            self.opt3_var.set(row[4])
            self.opt4_var.set(row[5])
            self.ans_var.set(row[6])
        except:    
            self.que_Entry.delete("1.0","end")
            self.opt1_var.set("")
            self.opt2_var.set("")
            self.opt3_var.set("")
            self.opt4_var.set("")
            self.ans_var.set("")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="db_quiz")
        cur=conn.cursor()
        cur.execute("select ID,name1,TotalNumberQue  from admin_tb")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.tv.delete(* self.tv.get_children())
            for items in rows:
                self.tv.insert('',END,values=items)
            conn.commit()
        conn.close() 

    def save_tables(self,topicName_var):
        #a=list[topicName_var]
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="questins_tbl")
        cur=conn.cursor()
        cur.execute("create table if not exists "+topicName_var+'(ID varchar(20) primary key,Question varchar(1000),Option1 varchar(100),Option2 varchar(100),Option3 varchar(100),Option4 varchar(100),Answer varchar(100))')
        conn.commit()


           
       

    def getRows(self,event):
        rowid=self.tv.identify_row(event.y) 
        item=self.tv.item(self.tv.focus())
        #print(item["values"][0])
        self.ID_var.set(item["values"][0])
        self.topicName_var.set(item["values"][1])
        self.totalNoQue.set(item["values"][2])
        self.pass_var.set(item["values"][3])

    def create(self):
        if(self.ID_var.get()=="" or self.topicName_var.get()=="" or self.pass_var.get()=="" or self.totalNoQue.get()==""):
            if self.ID_var.get()=="":                
                messagebox.showerror("Error","Please enter ID",parent=self.root)

            elif self.topicName_var.get()=="":                
                messagebox.showerror("Error","Please enter TOPIC NAME",parent=self.root)

            elif self.pass_var.get()=="":                
                messagebox.showerror("Error","Please enter PASSWORD",parent=self.root)

            elif self.totalNoQue.get()=="":                
                messagebox.showerror("Error","Please enter TOTAL NUMBER OF QUETION",parent=self.root)
        else:
            con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
            cur=con.cursor()
            cur.execute("Insert into admin_tb(ID,name1,Password1,TotalNumberQue ) values (%s,%s,%s,%s)",({self.ID_var.get()},{self.topicName_var.get()},{self.pass_var.get()},{self.totalNoQue.get()}))
            con.commit()
            self.fetch_data()
            con.close()
            self.save_tables(self.topicName_var.get())
            messagebox.showinfo("Success","Record has been inserted")
            # self.conn()
            #print(cur.rowcount,"Record inserted")         
        


    def edit(self):

        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()
        UpdtQry="Update create_quiz_tb SET ID=%s,Question=%s,Option1=%s,Option2=%s,Option3=%s,Option4=%s,Answer=%s where ID=%s"
        value=({self.variable.get()},{self.que_Entry.get("1.0","end")},{self.opt1_var.get()},{self.opt2_var.get()},{self.opt3_var.get()},{self.opt4_var.get()},{self.ans_var.get()},{self.variable.get()})
        cur.execute(UpdtQry,value)
        con.commit()
        con.close()
        messagebox.showinfo("info","Data update successfully...!",parent=self.root)
        # self.conn()
        #print(cur.rowcount,"Record updated") 

    def clear(self):
        self.que_Entry.delete('1.0',"end")
        self.opt1_var.set('')
        self.opt2_var.set('')
        self.opt3_var.set('')
        self.opt4_var.set('')
        self.ans_var.set('')      
        self.delete(1,0,END)

    def dummy(self):
        print(type(self.que_Entry.get("1.0","end")))
    '''def save(self):
        try:
            con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
            cur=con.cursor()
            cur.execute("Insert into create_quiz_tb(ID,Question,Option1,Option2,Option3,Option4,Answer) values (%s,%s,%s,%s,%s,%s,%s)",({self.variable.get()},{self.que_Entry.get("1.0","end")},{self.opt1_var.get()},{self.opt2_var.get()},{self.opt3_var.get()},{self.opt4_var.get()},{self.ans_var.get()}))
            con.commit()
        except:
            print(TypeError)
            # print("hh")
    '''
    def delete(self):
        con=pymysql.connect(host="localhost",user='root',password='root',database='db_quiz')
        cur=con.cursor()  
        if messagebox.askyesno("Confirm delete","Are you want to delete this?"):
            DltQry="Delete from create_quiz_tb where ID=%s"
            value=[(self.variable.get())]
            cur.execute(DltQry,value)
            con.commit()
            # con.close()
            # self.conn()
            #print(cur.rowcount,"Record deleted")
    

        else:
            return True      
    

    
def second():
    root=Tk()
    obj=display(root=root)
    obj.conn()
    # obj.getRows("click")
    # obj.validation()
    root.mainloop()




if __name__=="__main__":
    second()
    



