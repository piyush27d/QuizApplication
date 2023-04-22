from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql



class showquiz:
    def __init__(self,root) :
          # super().__init__(self,root)
        self.root=root
        self.root.title("Quiz page")
        self.root.state("zoomed")
        self.QuNom=StringVar()


        self.opt1=StringVar()
        self.opt2=StringVar()
        self.opt3=StringVar()
        self.opt4=StringVar()
        self.ans=StringVar()

        global QuNo,Que,QueShow,rdo1,rdo2,rdo3,rdo4

        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=700,width=1400,x=0,y=0)

        QuNo= Label(self.root, text=self.QuNom, font=("times new roman", 13, "bold"))
        QuNo.place(x=30,y=50)    

        Que= Label(self.root, text="Question  :", font=("times new roman", 13, "bold"))
        Que.place(x=200,y=50) 
        QueShow= Label(self.root, text="", font=("times new roman", 13, "bold"))
        QueShow.place(x=200,y=50)       

        rdo1 = Radiobutton(self.root,variable=self.opt1, value="Option1", text="",font=("times new roman", 12))
        rdo1.place(x=80,y=200) 

        rdo2 = Radiobutton(self.root,variable=self.opt1, value="Option1", text="",font=("times new roman", 12))
        rdo2.place(x=80,y=300) 

        rdo3 = Radiobutton(self.root,variable=self.opt1, value="Option1", text="",font=("times new roman", 12))
        rdo3.place(x=80,y=400) 

        rdo4 = Radiobutton(self.root,variable=self.opt1, value="Option1", text="",font=("times new roman", 12))
        rdo4.place(x=80,y=500) 

        nxtBtn = Button(self.root,text="NEXT",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray")
        nxtBtn.place(x=100,y=600,height=40,width=140)

        prev_btn=Button(self.root,text="PREVIOUS",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray")
        prev_btn.place(x=350,y=600,height=40,width=140)

        save_btn=Button(self.root,text="SAVE",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray")
        save_btn.place(x=600,y=600,height=40,width=140)

        clr_btn=Button(self.root,text="CLEAR",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray")
        clr_btn.place(x=850,y=600,height=40,width=140)

        Submit_btn=Button(self.root,text="SUBMIT",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray")
        Submit_btn.place(x=1100,y=600,height=40,width=140)




    def connection(self):
        
        conn=pymysql.connect(host="localhost" ,user="root" ,password="root" ,database="db_quiz")
        cur=conn.cursor()
        cur.execute("select * from create_quiz_tb")
        row=cur.fetchall()
        one=list(map(lambda x:x[0],row))
        self.QuNom=one[0]
        print(self.QuNom )       
        """for i in row:
            print(i[0],i[1],i[2],i[3],i[4],i[5])"""

            
      


        

def show():
    root=Tk()
    obj=showquiz(root=root)
    obj.connection()
    root.mainloop()

if __name__=="__main__":
    show()         