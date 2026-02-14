from tkinter import *
import random
import os
import sys
from tkinter import messagebox

def ensure_user_file():
    if not os.path.exists("users.txt"):
        with open("users.txt", "w") as f:
            pass


class Login_System:
    def __init__(self, master):
        self.master = master
        self.win = Toplevel(master)
        self.win.state('zoomed')
##        self.win.geometry("420x360+500+180")
        self.win.title("Login System")
        self.win.config(bg="#5B2C6F")
        self.win.protocol("WM_DELETE_WINDOW", self.close_app)

        self.username = StringVar()
        self.password = StringVar()

        Label(self.win, text="Welcome Back",
              font=("Arial Black", 40),
              bg="#5B2C6F", fg="white").pack(pady=20)

        Label(self.win, text="Enter Username",
              font=("Arial Black", 20),
              bg="#5B2C6F", fg="white").pack(pady=10)

        Entry(self.win, textvariable=self.username,
              font=("Arial", 18), bd=5).pack()

        Label(self.win, text="Enter Password",
              font=("Arial Black", 20),
              bg="#5B2C6F", fg="white").pack(pady=10)

        Entry(self.win, textvariable=self.password,
              font=("Arial", 18), bd=5, show="*").pack()

        Button(self.win, text="Login",
               font=("Arial Black", 18),
               width=12, pady=5,
               bg="#E5B4F3", fg="#6C3483",
               command=self.login).pack(pady=20)

        Button(self.win, text="New User? Sign Up",
               font=("Arial Black", 15),
               bg="#5B2C6F", fg="yellow",
               bd=0, command=self.open_signup).pack()

        Button(self.win, text="Forgot Password?",
               font=("Arial Black", 14),
               bg="#5B2C6F", fg="yellow",
               bd=0, command=self.forgot_password).pack(pady=5)

    def update_password(self):
            user = self.fp_user.get()
            new = self.fp_new.get()
            conf = self.fp_confirm.get()

            if user == "" or new == "" or conf == "":
                messagebox.showerror("Error", "All fields are required")
                return

            if new != conf:
                messagebox.showerror("Error", "Passwords do not match")
                return

            updated = False
            lines = []

            with open("users.txt", "r") as f:
                for line in f:
                    u, p = line.strip().split(",")
                    if u == user:
                        lines.append(f"{u},{new}\n")
                        updated = True
                    else:
                        lines.append(line)

            if not updated:
                messagebox.showerror("Error", "Username not found")
                return

            with open("users.txt", "w") as f:
                f.writelines(lines)

            messagebox.showinfo("Success", "Password updated successfully")
            self.fp_win.destroy()



    def close_app(self):
        self.master.destroy()

    # ---------- LOGIN ----------
    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        with open("users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == self.username.get() and p == self.password.get():
                    messagebox.showinfo("Success", "Login Successful")
                    self.win.destroy()
                    billing_win = Toplevel(self.master)
                    Bill_App(billing_win)
                    return

        messagebox.showerror("Error", "Invalid Username or Password")

    # ---------- OPEN SIGNUP ----------
    def open_signup(self):
        Signup_System(self.master)

    def forgot_password(self):
            self.fp_win = Toplevel(self.master)
            self.fp_win.title("Reset Password")
            self.fp_win.state('zoomed')
            self.fp_win.config(bg="#1A5276")

            self.fp_user = StringVar()
            self.fp_new = StringVar()
            self.fp_confirm = StringVar()

            Label(self.fp_win, text="Reset Password",
                  font=("Arial Black", 40),
                  bg="#1A5276", fg="white").pack(pady=30)

            Label(self.fp_win, text="Username",
                  font=("Arial Black", 20),
                  bg="#1A5276", fg="white").pack(pady=10)
            Entry(self.fp_win, textvariable=self.fp_user,
                  font=("Arial", 18), bd=5).pack()

            Label(self.fp_win, text="New Password",
                  font=("Arial Black", 20),
                  bg="#1A5276", fg="white").pack(pady=10)
            Entry(self.fp_win, textvariable=self.fp_new,
                  font=("Arial", 18), bd=5, show="*").pack()

            Label(self.fp_win, text="Confirm Password",
                  font=("Arial Black", 20),
                  bg="#1A5276", fg="white").pack(pady=10)
            Entry(self.fp_win, textvariable=self.fp_confirm,
                  font=("Arial", 18), bd=5, show="*").pack()

            Button(self.fp_win, text="Update Password",
                   font=("Arial Black", 18),
                   bg="#E5B4F3", fg="#6C3483",
                   width=15, command=self.update_password).pack(pady=25)


class Signup_System:
    def __init__(self, master):
        self.win = Toplevel(master)
        self.win.state('zoomed')

##        self.win.geometry("420x360+520+200")
        self.win.title("User Signup")
        self.win.config(bg="#2E86C1")

        self.new_user = StringVar()
        self.new_pass = StringVar()
        self.confirm_pass = StringVar()


        Label(self.win, text="Create New Account",
              font=("Arial Black", 40),
              bg="#2E86C1", fg="white").pack(pady=20)

        Label(self.win, text="Create Username",
              font=("Arial Black", 20),
              bg="#2E86C1", fg="white").pack(pady=8)

        Entry(self.win, textvariable=self.new_user,
              font=("Arial", 18), bd=5).pack()

        Label(self.win, text="Create New Password",
              font=("Arial Black", 20),
              bg="#2E86C1", fg="white").pack(pady=8)

        Entry(self.win, textvariable=self.new_pass,
              font=("Arial", 18), bd=5, show="*").pack()

        Label(self.win, text="Confirm Password",
              font=("Arial Black", 20),
              bg="#2E86C1", fg="white").pack(pady=8)

        Entry(self.win, textvariable=self.confirm_pass,
              font=("Arial", 18), bd=5, show="*").pack()


        Button(self.win, text="Register",
               font=("Arial Black", 15),
               width=12, pady=5,
               bg="#E5B4F3", fg="#6C3483",
               command=self.register).pack(pady=20)

    def register(self):
        if (self.new_user.get() == "" or
            self.new_pass.get() == "" or
            self.confirm_pass.get() == ""):
            messagebox.showerror("Error", "All fields are required")
            return

        if self.new_pass.get() != self.confirm_pass.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        with open("users.txt", "r") as f:
            for line in f:
                if line.startswith(self.new_user.get() + ","):
                    messagebox.showerror("Error", "Username already exists")
                    return

        with open("users.txt", "a") as f:
            f.write(f"{self.new_user.get()},{self.new_pass.get()}\n")

        messagebox.showinfo("Success", "Account Created Successfully")
        self.win.destroy()



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.state('zoomed')
##        self.root.geometry("100x80+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing Software")
        title=Label(self.root,text="SUPER MART",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.nutella=IntVar()
        self.noodles=IntVar()
        self.lays=IntVar()
        self.oreo=IntVar()
        self.muffin=IntVar()
        self.silk=IntVar()
        self.namkeen=IntVar()
        self.atta=IntVar()
        self.pasta=IntVar()
        self.rice=IntVar()
        self.oil=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.tea=IntVar()
        self.soap=IntVar()
        self.shampoo=IntVar()
        self.lotion=IntVar()
        self.cream=IntVar()
        self.foam=IntVar()
        self.mask=IntVar()
        self.sanitizer=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=20)
        details.place(x=0,y=70,height=110,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",15),bg="#A569BD",fg="white").grid(row=0,column=0,pady=15,padx=33)

        cust_entry=Entry(details,borderwidth=7,width=35,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",15),bg="#A569BD",fg="white").grid(row=0,column=2,padx=33)

        contact_entry=Entry(details,borderwidth=7,width=25,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",15),bg="#A569BD",fg="white").grid(row=0,column=4,padx=33)

        bill_entry=Entry(details,borderwidth=7,width=25,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================snacks label frame=================================================================
        snacks=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=8,y=190,height=450,width=350)

        item1=Label(snacks,text="Nutella Choco Spread",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=14)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.nutella).grid(row=0,column=1,padx=15)

        item2=Label(snacks,text="Noodles(1 Pack)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=14)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=15)

        item3=Label(snacks,text="Lays",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=14)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.lays).grid(row=2,column=1,padx=15)

        item4=Label(snacks,text="Oreo",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=14)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.oreo).grid(row=3,column=1,padx=15)

        item5=Label(snacks,text="Chocolate Muffin",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=14)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.muffin).grid(row=4,column=1,padx=15)

        item6=Label(snacks,text="Dairy Milk Silk",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=14)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=15)

        item7=Label(snacks,text="Namkeen",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=14)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.namkeen).grid(row=6,column=1,padx=15)
        #===================================GROCERY=====================================================================================
        grocery=LabelFrame(self.root,text="Grocery",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        grocery.place(x=370,y=190,height=450,width=350)

        item8=Label(grocery,text="Aashirvaad Atta(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=14)
        item8_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.atta).grid(row=0,column=1,padx=15)

        item9=Label(grocery,text="Pasta(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=14)
        item9_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=15)

        item10=Label(grocery,text="Basmathi Rice(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=14)
        item10_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.rice).grid(row=2,column=1,padx=15)

        item11=Label(grocery,text="Sunflower Oil(1ltr)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=14)
        item11_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.oil).grid(row=3,column=1,padx=15)

        item12=Label(grocery,text="Refined Sugar(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=14)
        item12_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.sugar).grid(row=4,column=1,padx=15)

        item13=Label(grocery,text="Daal(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=14)
        item13_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=15)

        item14=Label(grocery,text="Tea Powder(1kg)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=14)
        item14_entry=Entry(grocery,borderwidth=2,width=15,textvariable=self.tea).grid(row=6,column=1,padx=15)
        #========================================beauty and hygine===============================================================================
        hygine=LabelFrame(self.root,text="Beauty & Hygine",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=730,y=190,height=450,width=350)

        item15=Label(hygine,text="Bathing Soap",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=14)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.soap).grid(row=0,column=1,padx=15)

        item16=Label(hygine,text="Shampoo(1ltr)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=14)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.shampoo).grid(row=1,column=1,padx=15)

        item17=Label(hygine,text="Body Lotion(1ltr)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=14)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.lotion).grid(row=2,column=1,padx=15)

        item18=Label(hygine,text="Face Cream",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=14)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.cream).grid(row=3,column=1,padx=15)

        item19=Label(hygine,text="Shaving Foam",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=14)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.foam).grid(row=4,column=1,padx=15)

        item20=Label(hygine,text="Face Mask",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=14)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.mask).grid(row=5,column=1,padx=15)

        item21=Label(hygine,text="Hand Sanitizer(50ml)",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=14)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.sanitizer).grid(row=6,column=1,padx=15)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1090,y=190,width=365,height=450)

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery",font=("Arial Black",14),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=650,relwidth=1,height=180)

        total_snacks=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",12),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=9)

        total_grocery=Label(billing_menu,text="Total Grocery Price",font=("Arial Black",12),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=9)


        total_hygine=Label(billing_menu,text="Total Beauty & Hygine Price",font=("Arial Black",12),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=9)

        tax_snacks=Label(billing_menu,text="Snacks Tax",font=("Arial Black",12),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=9)

        tax_grocery=Label(billing_menu,text="Grocery Tax",font=("Arial Black",12),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_grocery_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=9)


        tax_hygine=Label(billing_menu,text="Beauty & Hygine Tax",font=("Arial Black",12),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=9)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=920,width=520,height=115)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",14),pady=10,
                            bg="#E5B4F3",fg="#6C3483",command=lambda:total(self))
        button_total.grid(row=0,column=0,padx=10,pady=15)

        button_save=Button(button_frame,text="Save Bill",font=("Arial Black",14),pady=10,
                           bg="#E5B4F3",fg="#6C3483",command=lambda:save_bill(self))
        button_save.grid(row=0,column=1,padx=10,pady=15)

        button_search=Button(button_frame,text="Search Bill",font=("Arial Black",14),pady=10,
                             bg="#E5B4F3",fg="#6C3483",command=lambda:search_bill(self))
        button_search.grid(row=0,column=2,padx=10, pady=15)

        button_clear=Button(button_frame,text="Clear",font=("Arial Black",14),pady=10,
                            bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self))
        button_clear.grid(row=0,column=3,padx=10, pady=15)

        button_exit=Button(button_frame,text="Exit",font=("Arial Black",14),pady=10,
                           bg="#E5B4F3",fg="#6C3483",command=lambda:exit1(self))
##        button_exit.grid(row=0,column=4,padx=10)
##        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=20)
##        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=20,pady=6)
##        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=20,pady=6)
     #   intro(self)
     


def total(self):
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.nu=self.nutella.get()*120
    self.no=self.noodles.get()*40
    self.la=self.lays.get()*10
    self.ore=self.oreo.get()*20
    self.mu=self.muffin.get()*30
    self.si=self.silk.get()*60
    self.na=self.namkeen.get()*15
    total_snacks_price=(
                self.nu+
                self.no+
                self.la+
                self.ore+
                self.mu+
                self.si+
                self.na)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

    self.at=self.atta.get()*42
    self.pa=self.pasta.get()*120
    self.oi=self.oil.get()*113
    self.ri=self.rice.get()*160
    self.su=self.sugar.get()*55
    self.te=self.tea.get()*480
    self.da=self.dal.get()*76
    total_grocery_price=(
        self.at+
        self.pa+
        self.oi+
        self.ri+
        self.su+
        self.te+
        self.da)

    self.total_gro.set(str(total_grocery_price)+" Rs")
    self.b.set(str(round(total_grocery_price*0.01,3))+" Rs")

    self.so=self.soap.get()*30
    self.sh=self.shampoo.get()*180
    self.cr=self.cream.get()*130
    self.lo=self.lotion.get()*500
    self.fo=self.foam.get()*85
    self.ma=self.mask.get()*100
    self.sa=self.sanitizer.get()*20

    total_hygine_price=(
        self.so+
        self.sh+
        self.cr+
        self.lo+
        self.fo+
        self.ma+
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")
    self.total_all_bill=(total_snacks_price+
                total_grocery_price+
                total_hygine_price+
                (round(total_grocery_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n=======================================\n")
    self.txtarea.insert(END,"\nProduct\t\t  Qty\t\t Price\n")
    self.txtarea.insert(END,"\n=======================================\n")
def billarea(self):
    intro(self)
    if self.nutella.get()!=0:
        self.txtarea.insert(END,f"Nutella\t\t   {self.nutella.get()}\t\t  {self.nu}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t   {self.noodles.get()}\t\t  {self.no}\n")
    if self.lays.get()!=0:
        self.txtarea.insert(END,f"Lays\t\t   {self.lays.get()}\t\t  {self.la}\n")
    if self.oreo.get()!=0:
        self.txtarea.insert(END,f"Oreo\t\t   {self.oreo.get()}\t\t  {self.ore}\n")
    if self.muffin.get()!=0:
        self.txtarea.insert(END,f"Muffins\t\t   {self.muffin.get()}\t\t  {self.mu}\n")
    if self.silk.get()!=0:
        self.txtarea.insert(END,f"Silk\t\t   {self.silk.get()}\t\t  {self.si}\n")
    if self.namkeen.get()!=0:
        self.txtarea.insert(END,f"Namkeen\t\t   {self.namkeen.get()}\t\t  {self.na}\n")
    if self.atta.get()!=0:
        self.txtarea.insert(END,f"Atta\t\t   {self.atta.get()}\t\t  {self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t   {self.pasta.get()}\t\t  {self.pa}\n")
    if self.rice.get()!=0:
        self.txtarea.insert(END,f"Rice\t\t   {self.rice.get()}\t\t  {self.ri}\n")
    if self.oil.get()!=0:
        self.txtarea.insert(END,f"Oil\t\t   {self.oil.get()}\t\t  {self.oi}\n")
    if self.sugar.get()!=0:
        self.txtarea.insert(END,f"Sugar\t\t   {self.sugar.get()}\t\t  {self.su}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t   {self.dal.get()}\t\t  {self.da}\n")
    if self.tea.get()!=0:
        self.txtarea.insert(END,f"Tea\t\t   {self.tea.get()}\t\t  {self.te}\n")
    if self.soap.get()!=0:
        self.txtarea.insert(END,f"Soap\t\t   {self.soap.get()}\t\t  {self.so}\n")
    if self.shampoo.get()!=0:
        self.txtarea.insert(END,f"Shampoo\t\t   {self.shampoo.get()}\t\t  {self.sh}\n")
    if self.lotion.get()!=0:
        self.txtarea.insert(END,f"Lotion\t\t   {self.lotion.get()}\t\t  {self.lo}\n")
    if self.cream.get()!=0:
        self.txtarea.insert(END,f"Cream\t\t   {self.cream.get()}\t\t  {self.cr}\n")
    if self.foam.get()!=0:
        self.txtarea.insert(END,f"Foam\t\t   {self.foam.get()}\t\t  {self.fo}\n")
    if self.mask.get()!=0:
        self.txtarea.insert(END,f"Mask\t\t   {self.mask.get()}\t\t  {self.ma}\n")
    if self.sanitizer.get()!=0:
        self.txtarea.insert(END,f"Sanitizer\t\t   {self.sanitizer.get()}\t\t  {self.sa}\n")

    self.txtarea.insert(END,f"---------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"---------------------------------------\n")
def save_bill(self):
    if self.txtarea.get(1.0, END).strip() == "":
        messagebox.showerror("Error", "No bill generated to save!")
        return

    try:
        os.makedirs("bills", exist_ok=True)
        file_path = f"bills/BillNumber_{self.bill_no.get()}.txt"
        with open(file_path, "w") as f:
            f.write(self.txtarea.get(1.0, END))
        messagebox.showinfo("Saved", f"Bill No BillNumber_{self.bill_no.get()} saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong\n{e}")

def search_bill(self):
    bill_no = self.bill_no.get()

    if bill_no == "":
        messagebox.showerror("Error", "Enter Bill Number to search")
        return

    file_path = f"bills/BillNumber_{bill_no}.txt"

    if os.path.exists(file_path):
        self.txtarea.delete(1.0, END)
        with open(file_path, "r") as f:
            self.txtarea.insert(END, f.read())
    else:
        messagebox.showerror("Not Found", "Bill not found!")


def clear(self):
        self.txtarea.delete(1.0,END)
        self.nutella.set(0)
        self.noodles.set(0)
        self.lays.set(0)
        self.oreo.set(0)
        self.muffin.set(0)
        self.silk.set(0)
        self.namkeen.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.sugar.set(0)
        self.dal.set(0)
        self.tea.set(0)
        self.soap.set(0)
        self.shampoo.set(0)
        self.lotion.set(0)
        self.cream.set(0)
        self.foam.set(0)
        self.mask.set(0)
        self.sanitizer.set(0)
        self.total_sna.set(0)
        self.total_gro.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root = Tk()
root.withdraw()
ensure_user_file()   
Login_System(root)
root.mainloop()



