from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk 
#import pymysql #pip install pymysql
class register:
     def __init__(self,root):
         self.root=root
         self.root.title("Registration Form")
         self.root.geometry("1350x700+0+0")
         # Background Image
         
         #self.bg=ImageTk.PhotoImage(file="c.jpg")
         #bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=-1.5,relheight=-1.5)
         
         #Left Side Image
         
         self.left=ImageTk.PhotoImage(file="2.png")
         left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
         
         #Register Here
         
         frame1=Frame(self.root,bg="#fff3e2")
         frame1.place(x=480,y=100,width=700,height=500)
         
         title=Label(frame1,text="Register Here",font=("time new Roman",20,"bold"),bg="#fff3e2",fg="#ea2c62").place(x=50,y=30)
        
         #---------------Row 1----------------------
         f_name=Label(frame1,text="First Name",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=50,y=100)
         self.txt_fname=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_fname.place(x=50,y=130,width=250)
         
         l_name=Label(frame1,text="Last Name",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=370,y=100)
         self.txt_lname=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_lname.place(x=370,y=130,width=250)
         #---------------Row 2----------------------
         
         contact=Label(frame1,text="Contact Number",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=50,y=170)
         self.txt_contact=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_contact.place(x=50,y=200,width=250)
        
         Email=Label(frame1,text="E-Mail Address",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=370,y=170)
         self.txt_Email=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_Email.place(x=370,y=200,width=250)
         #----------------Row 3---------------------
         
         address=Label(frame1,text="Address",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=50,y=240)
         self.txt_address=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_address.place(x=50,y=270,width=250)
         
         pin=Label(frame1,text="Pin code",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=370,y=240)
         self.txt_pin=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_pin.place(x=370,y=270,width=250)
         #----------------Row 4---------------------
         
         password=Label(frame1,text="Password",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=50,y=310)
         self.txt_password=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_password.place(x=50,y=340,width=250)
         
         cpass=Label(frame1,text="Confirm Password",font=("time new Roman",15,"bold"),bg="#fff3e2",fg="#706897").place(x=370,y=310)
         self.txt_cpass=Entry(frame1,font=("time new roman",15),bg="white")
         self.txt_cpass.place(x=370,y=340,width=250)
         #-----Terms----
         
         self.var_chk=IntVar()
         chk=Checkbutton(frame1,text="I agree the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="#fff3e2",font=("time new roman",12)).place(x=50,y=380)
         
         #self.btn_img=ImageTk.PhotoImage(file="image/Reg.png")
         #btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=50,y=420)
         
         #-------------------------------
         
         submit_btn=Button(frame1,text="Submit",bg="#61b15a",fg="white",font=("time new roman",20),bd=0,cursor="hand1",command=self.register_data).place(x=50,y=420)
         sign_btn=Button(frame1,text="Sign In",bg="#0e49b5",fg="white",font=("time new roman",20),bd=0,cursor="hand1",command=self.login_window).place(x=350,y=420)

     def login_window(self):
        self.root.destroy()
        import login     
     def register_data(self):
         
         if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_Email.get()=="" or self.txt_address.get()=="" or self.txt_contact.get()=="" or self.txt_pin.get()=="" or self.txt_password.get()=="" or self.txt_cpass.get()=="":
             messagebox.showerror("Error","All fields are requried",parent=self.root)
         elif self.txt_password.get()!=self.txt_cpass.get():
             messagebox.showerror("Error","Password MisMatch",parent=self.root)
         elif self.var_chk.get()==0:
            messagebox.showerror("Error","Plzzz...Agree  our terms and Condition....",parent=self.root)
         else:
             
             try:
                  con=pymysql.connect(host="localhost",user="root",password="",database="mypro")
                  cur=con.cursor()
                  cur.execute("insert into user (f_name,l_name,Email,address,contact,pin,password) values(%s,%s,%s,%s,%s,%s,%s)",
                              
                              (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_Email.get(),
                                self.txt_address.get(),
                                self.txt_contact.get(),
                                self.txt_pin.get(),
                                self.txt_password.get()
                                ))
                  con.commit()
                  con.close()
                  messagebox.showinfo("Success","Register Successfully",parent=self.root)   
             except Exception as es:
                  messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
             
             
            # messagebox.showinfo("Success","Register Successful",parent=self.root)
         
         
         
         
         
         
         # print(self.txt_fname.get(),
         #        self.txt_lname.get(),
         #        self.txt_Email.get(),
         #        self.txt_address.get(),
         #        self.txt_contact.get(),
         #        self.txt_pin.get(),
         #        self.txt_password.get(),
         #        self.txt_cpass.get())
              
        
         
              
              
root=Tk()
obj=register(root)
root.mainloop()