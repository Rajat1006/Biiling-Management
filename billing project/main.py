from tkinter import *
from tkinter import messagebox
import math,random,os
###############Bill app naam se class bnaai################
class Bill_app:
    def __init__(self,root):
        self.root=root   # root ko initialize krege
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="red")
        self.root.title("Billing software")
        bg_color="Blue"
        ##############-----pady se kya hoga ki jo title diya hai thoda sa down mai jaayegaa or groove se decoration aayegi----######
        ############====== title pr frame nhi lgaai just only label hi lgaaya=======##############
        title=Label(self.root,text="Billing Software",font=("times new roman",30,"bold"),pady=2,bg=bg_color,bd=12,relief=GROOVE)
        ##### ye jo (fill= X) likha is se ye saara jo decoration diya border or pady ka ye (x---axis) mai fill ho jaayeyaa 0 se start hoke ##########
        title.pack(fill=X)


        ##########+++++++++========Variables for the input fields =============+++++++++############

        ########==============Cosmetics variables=========############
        self.soap=IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()

        ########==============Grocery variables=========############
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        ########==============cold Drinks variable =========############
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumsup= IntVar()
        self.limca = IntVar()
        self.sprite= IntVar()

        ########==============Total product price and tax variables=========############
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price= StringVar()


        self.cosmetic_tax= StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax= StringVar()

        ########==============frame 1 mai customer variables=========############
        self.c_name = StringVar()
        self.c_phon = StringVar()

        #####==== ye baala bill no variable humne randomly bill no jo generate hoga uske liye bnaay hai
        self.c_bill_no = StringVar()
        x=random.randint(1000,9999)
        self.c_bill_no.set(str(x))

        ########=========ye waala variable jo bill no waali blank field hai search ke liye bnaay hai
        self.search_bill = StringVar()




        ############======customer ke liye frame bnaayege ab ====#########
        ####label type frame bnaayege################

        F1=LabelFrame(self.root,text="customer Details",font=("times new roman",15,"bold"),bd=7,fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        #########======relwidth ke saath billing project jo label lgaaya hai uske just neeche ek line aa jaayegii=======########

        cname_lbl=Label(F1,text="Customer Name",width=12,font=("times new roman",15,"bold"),fg="gold",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width="20",textvariable=self.c_name,font=("arial",10,"bold"),bd=7,relief=GROOVE).grid(row=0,column=1)



        cphn_lbl = Label(F1, text="Customer Phone",width=12, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width="20",textvariable=self.c_phon, font=("arial", 10, "bold"), bd=7, relief=GROOVE).grid(row=0, column=3)



        cbill_lbl = Label(F1, text="Bill No.",width=5,font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width="20",textvariable=self.search_bill, font=("arial", 10, "bold"), bd=7, relief=GROOVE).grid(row=0, column=5)

        bill_btn=Button(F1,text="search",command=self.find_bill,width=8,font=("times new roman", 11, "bold"),fg="black",bd=5,relief=GROOVE,pady=2).grid(row=0,column=6,padx=80,pady=10)



 ####################==========Cosmetic Frame=========########################

        F2 = LabelFrame(self.root, text="cosmetic", font=("times new roman", 15, "bold"), bd=7, fg="gold",bg=bg_color)
        F2.place(x=10, y=180,width=325,height=370)


        bath_lbl = Label(F2, text="Bath Soap",font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=0, column=0,sticky=W)
        bath_txt=Entry(F2,width="20",textvariable=self.soap,font=("arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)


        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=1,column=0,sticky=W)
        Face_cream_txt = Entry(F2, width="20",textvariable=self.face_cream, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10,pady=10)


        Face_wash_lbl = Label(F2, text="Face wash", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=2,column=0,sticky=W)
        Face_wash_txt = Entry(F2, width="20",textvariable=self.face_wash, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=2,column=1, padx=10,pady=10)


        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=3,column=0,sticky=W)
        Hair_s_txt = Entry(F2, width="20", textvariable=self.spray,font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)


        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=4,column=0,sticky=W)
        Hair_g_txt = Entry(F2, width="20",textvariable=self.gell, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)


        Body_lbl = Label(F2, text="Body Loshan", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=5,column=0,sticky=W)
        Body_txt = Entry(F2, width="20", textvariable=self.loshan,font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=5, column=1, padx=10,  pady=10)




###################=================Grocery frame================###################


        F3 = LabelFrame(self.root, text="Grocery", font=("times new roman", 15, "bold"), bd=7, fg="gold",bg=bg_color)
        F3.place(x=355, y=180, width=325, height=370)



        g1_lbl = Label(F3, text="Rice",font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=0, column=0,sticky=W)
        g1_txt = Entry(F3, width="20",textvariable=self.rice ,font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)


        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=1, column=0,sticky=W)
        g2_txt = Entry(F3, width="20",textvariable=self.food_oil, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)


        g3_lbl = Label(F3, text="Dal", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=2, column=0,sticky=W)
        g3_txt = Entry(F3, width="20",textvariable=self.daal, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)


        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=3, column=0,sticky=W)
        g4_txt = Entry(F3, width="20",textvariable=self.wheat, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)



        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=4,column=0,sticky=W)
        g5_txt = Entry(F3, width="20",textvariable=self.sugar, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)


        g6_lbl = Label(F3, text="Tea",font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid( row=5,column=0,sticky=W)
        g6_txt = Entry(F3, width="20",textvariable=self.tea, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)



        #################=========COLD DRINKS FRAME===========###############

        F4 = LabelFrame(self.root, text="Grocery", font=("times new roman", 15, "bold"), bd=7, fg="gold", bg=bg_color)
        F4.place(x=700, y=180, width=325, height=370)



        c1_lbl = Label(F4, text="Mazza", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=0, column=0,sticky=W)
        c1_txt = Entry(F4,width="20",textvariable=self.maza, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)


        c2_lbl = Label(F4, text="Cock", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=1,column=0, sticky=W)
        c2_txt = Entry(F4, width="20", textvariable=self.cock,font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)


        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=2,column=0,sticky=W)
        c3_txt = Entry(F4, width="20",textvariable=self.frooti, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10,pady=10)


        c4_lbl = Label(F4, text="Thums Up", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=3, column=0,sticky=W)
        c4_txt = Entry(F4, width="20",textvariable=self.thumsup, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)


        c5_lbl = Label(F4, text="Limca", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=4, column=0,sticky=W)
        c5_txt = Entry(F4, width="20",textvariable=self.limca, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)



        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color).grid(row=5,column=0,sticky=W)
        c6_txt = Entry(F4, width="20",textvariable=self.sprite, font=("arial", 10, "bold"), bd=7, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)


 #################=========Bill Area FRAME===========###############

        F5 =Frame(self.root,bd=7,relief=GROOVE)
        F5.place(x=1040, y=180, width=310, height=370)

        bill_title_label=Label(F5,text="Bill Area",font=("arial",15, "bold"),bd=7,relief=GROOVE).pack(fill=X)

        #####======ab yha pr bill area mai ek scroll bar chahiye=======##########
        #####========sbse pehle to ek variable mai stor ekr diya scroll barr ko orient vertical kr diya  =========##########

        scrol_y=Scrollbar(F5,orient=VERTICAL)


        #########==========Text field lgaai frame mai but isko self ke saath ek variable mai stroe kiya ==========#############
        #####======yscrollcommand lgaa ke jo scroll bar stotre kri hai usko set kr diya TEXT field mai =======##########
        #####======self isliye lgaaya bcz globally through out the page chahiye bcz baad mai data iss se fetch bhi krna hai or isme changes bhi krni hai
        ############++++++ ab scroll bar to lga di but is case mai ab data bhi to scroll hona chahiye  iske liye scroll ko configure krna hoga and is text area ko is se relate krna hoga =+++++++++##############



        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=BOTH)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack()



        ##############================Button frame ==========#####################


        F6 = LabelFrame(self.root, text="Billig Menu", font=("times new roman", 15, "bold"), bd=7, fg="gold",bg=bg_color)

        F6.place(x=0, y=560, relwidth=1,height=135)

        m1_lbl = Label(F6, text=" Total Cosmetic Price", font=("times new roman", 12, "bold"), fg="gold",bg=bg_color).grid(row=0, column=0, padx=20, pady=1,sticky=W)

        m1_txt = Entry(F6, width="20", textvariable=self.cosmetic_price,font=("arial", 8, "bold"), bd=5, relief=GROOVE).grid(row=0, column=1,padx=10,pady=1)



        m2_lbl = Label(F6, text="Total Grocery Price", font=("times new roman", 12, "bold"), fg="gold",bg=bg_color).grid(row=1, column=0, padx=20, pady=1,sticky=W)

        m2_txt = Entry(F6, width="20",textvariable=self.grocery_price, font=("arial", 8, "bold"), bd=5, relief=GROOVE).grid(row=1, column=1,padx=10,pady=1)



        m3_lbl = Label(F6, text=" Total Cold Drinks price",  font=("times new roman", 12, "bold"), fg="gold",bg=bg_color).grid(row=3, column=0, padx=20, pady=1,sticky=W)

        m3_txt = Entry(F6, width="20",textvariable=self.cold_drink_price, font=("arial", 8, "bold"), bd=5, relief=GROOVE).grid(row=3, column=1,padx=10,pady=1)






        b1_lbl = Label(F6, text="Cosmetic Tax", font=("times new roman", 12, "bold"), fg="gold",bg=bg_color).grid(row=0, column=2, padx=20, pady=1, sticky=W)

        b1_txt = Entry(F6, width="20",textvariable=self.cosmetic_tax, font=("arial", 8, "bold"), bd=5, relief=GROOVE).grid(row=0, column=3, padx=10,pady=1)


        b2_lbl = Label(F6, text="Grocery Tax", font=("times new roman", 12, "bold"), fg="gold", bg=bg_color).grid(row=1, column=2, padx=20, pady=1, sticky=W)

        b2_txt = Entry(F6, width="20",textvariable=self.grocery_tax, font=("arial", 8, "bold"), bd=5, relief=GROOVE).grid(row=1, column=3, padx=10, pady=1)


        b3_lbl = Label(F6, text="Cold Drinks tax", font=("times new roman", 12, "bold"), fg="gold",bg=bg_color).grid(row=3, column=2, padx=20, pady=1, sticky=W)

        b3_txt = Entry(F6, width="20",textvariable=self.cold_drink_tax, font=("arial", 8, "bold"), bd=5, relief=GROOVE).grid(row=3, column=3, padx=10, pady=1)


        btn_F=Frame(F6,bg=bg_color,bd=7,relief=SUNKEN)
        btn_F.place(x=640,height=100,width=690)

        total_btn = Button(btn_F,text="Total",width=12,bg="cadetblue",font=("times new roman", 12, "bold"),fg="white",bd=7,padx=15,pady=5,command=self.total).grid(row=0,column=0,padx=5,pady=20)
        GBill_btn = Button(btn_F, text="Genrate Bill",width=12, bg="cadetblue",font=("times new roman", 12, "bold"),fg="white", bd=7, padx=15, pady=5,command=self.bill_area).grid(row=0, column=1, padx=5, pady=20)
        Clear_btn = Button(btn_F,command= self.clear_data,text="Clear",width=12 ,bg="cadetblue",font=("times new roman", 12, "bold"), fg="white", bd=7, padx=15, pady=5).grid(row=0, column=2, padx=5, pady=20)
        Exit_btn = Button(btn_F,command=self.Exit_app, text="Exit", width=12, bg="cadetblue",font=("times new roman", 12, "bold"), fg="white", bd=7, padx=15, pady=5).grid(row=0,column=3, padx=5, pady=20)
        self.welcome_bill()


###########========= Functionality for the Total button ===========###########
#########====== jaise hi mai total button pr click kru mere total cosmetic price mai total aa jaaye
    def total(self):
        ##################======COSMETIC=====+#############

        self.c_s_p= (self.soap.get()*40)
        self.c_fc_p=(self.face_cream.get()*120)
        self.c_fw_p=(self.face_wash.get()*60)
        self.c_hs_p=(self.spray.get()*50)
        self.c_hg_p=(self.gell.get()*50)
        self.c_bl_p= (self.loshan.get()*40)


        self.total_cosmetic_price=(float
                                (self.c_s_p)+
                                (self.c_fc_p)+
                                (self.c_fw_p)+
                                (self.c_hs_p)+
                                (self.c_hg_p)+
                                (self.c_bl_p)
                                )
        self.cosmetic_price.set("Rs"+" "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs"+" "+str(self.c_tax))     ##########===round isliye likha bcz ki jb calculation hogi tb answer bhut saare aa skte hai decimal ke baad hume 2 hi no chahiye so round function lgaaya


        ###################=========GROCERY=========############

        self.g_r_p =(self.rice.get() * 40)
        self.g_f_p=(self.food_oil.get() * 120)
        self.g_d_p =(self.daal.get() * 60)
        self.g_w_p =(self.wheat.get() * 50)
        self.g_s_p =(self.sugar.get() * 50)
        self.g_t_p =(self.tea.get() * 40)

        self.total_grocery_price = (float
                                    (self.g_r_p)+
                                    (self.g_f_p)+
                                    (self.g_d_p)+
                                    (self.g_w_p)+
                                    (self.g_s_p)+
                                    (self.g_s_p)+
                                    (self.g_t_p)
                                     )
        self.grocery_price.set("Rs"+" "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.01),2)
        self.grocery_tax.set("Rs"+" "+str(self.g_tax))



        #################==========Cold Drinks=========############

        self.d_m_p =(self.maza.get() * 40)
        self.d_c_p =(self.cock.get() * 120)
        self.d_f_p =(self.frooti.get() * 60)
        self.d_t_p =(self.thumsup.get() * 50)
        self.d_l_p =(self.limca.get() * 50)
        self.d_s_p =(self.sprite.get() * 40)



        self.total_drinks_price = (float
                                   (self.d_m_p)+
                                   (self.d_c_p)+
                                   (self.d_f_p)+
                                   (self.d_t_p)+
                                   (self.d_l_p)+
                                   (self.d_s_p)
                                    )

        self.cold_drink_price.set("Rs"+" "+ str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_tax.set("Rs"+" "+str(self.d_tax))





        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_drinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax)




    def welcome_bill(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\tWelcome to our Resturant \n")
        self.textarea.insert(END,f"\nBill No.      :{self.c_bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone No.     :{self.c_phon.get()}")
        self.textarea.insert(END,f"\n==================================")
        self.textarea.insert(END,f"\tProduct\t\tQty\tPrice")
        self.textarea.insert(END, f"\n==================================")



    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showinfo("error","koi detail hai customer di ta bhr lo unoo")
        elif self.cosmetic_price.get()=="Rs 0.0" and self.grocery_price.get()=="Rs 0.0" and self.cosmetic_price.get()=="Rs 0.0":
            messagebox.showinfo("kiddrr","Khreed to le kuch pehle")
        else:
            self.welcome_bill()
            ############=====Cosmetic=======########
            if self.soap.get() != 0:
                self.textarea.insert(END, f"\nBath Soap\t\t {self.soap.get()} \t {self.c_s_p}")
            if self.face_cream.get() != 0:
                self.textarea.insert(END, f"\nFace Cream\t\t {self.face_cream.get()} \t {self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.textarea.insert(END, f"\nFace wash\t\t {self.face_wash.get()} \t {self.c_fw_p}")
            if self.spray.get() != 0:
                self.textarea.insert(END, f"\nHair Spray\t\t {self.spray.get()} \t {self.c_hs_p}")
            if self.gell.get() != 0:
                self.textarea.insert(END, f"\nHair Gel\t\t {self.gell.get()} \t {self.c_hg_p}")
            if self.loshan.get() != 0:
                self.textarea.insert(END, f"\nBody Loashan\t\t {self.loshan.get()} \t {self.c_bl_p}")

                ############=====Grocery=======########

            if self.rice.get() != 0:
                self.textarea.insert(END, f"\nRice\t\t {self.rice.get()} \t {self.g_r_p}")
            if self.food_oil.get() != 0:
                self.textarea.insert(END, f"\nFood oil\t\t {self.food_oil.get()} \t {self.g_f_p}")
            if self.daal.get() != 0:
                self.textarea.insert(END, f"\nDaal\t\t {self.daal.get()} \t {self.g_d_p}")
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\nWheat\t\t {self.wheat.get()} \t {self.g_w_p}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\nsugar\t\t {self.sugar.get()} \t {self.g_s_p}")
            if self.tea.get() != 0:
                self.textarea.insert(END, f"\nTea\t\t {self.tea.get()} \t {self.g_t_p}")

                ############=====Cold Drinks=======########

            if self.maza.get() != 0:
                self.textarea.insert(END, f"\nMaaza\t\t {self.maza.get()} \t {self.d_m_p}")
            if self.cock.get() != 0:
                self.textarea.insert(END, f"\nCoke\t\t {self.cock.get()} \t {self.d_c_p}")
            if self.frooti.get() != 0:
                self.textarea.insert(END, f"\nFrooti\t\t {self.frooti.get()} \t {self.d_f_p}")
            if self.thumsup.get() != 0:
                self.textarea.insert(END, f"\nThums Up\t\t {self.thumsup.get()} \t {self.d_t_p}")
            if self.limca.get() != 0:
                self.textarea.insert(END, f"\nLimca\t\t {self.limca.get()} \t {self.d_l_p}")
            if self.sprite.get() != 0:
                self.textarea.insert(END, f"\nSprite\t\t {self.sprite.get()} \t {self.d_s_p}")

            self.textarea.insert(END, f"\n----------------------------------")
            if self.cosmetic_tax.get() != "Rs 0.0":
                self.textarea.insert(END, f"\nCosmetic tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs 0.0":
                self.textarea.insert(END, f"\nGrocery  tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs 0.0":
                self.textarea.insert(END, f"\nCold Drinks tax\t\t\t{self.cold_drink_tax.get()}")

            self.textarea.insert(END, f"\n----------------------------------")
            self.textarea.insert(END, f"\nTotal\t\t\tRs {str(self.Total_bill)}")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save Bill?")
        if op > 0:
            self.bill_data = self.textarea.get("1.0", END)
            f1 = open("bills/" + str(self.c_bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no.{self.c_bill_no.get()} Saved successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i} ", "r")
                self.textarea.delete('1.0', END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
        # ===================variables================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

        # =====================grocery================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

        # =====================Cold drinks============
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

        # ==========total product price & tax variables====
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

        # ===========Customer============
            self.c_name.set("")
            self.c_phon.set("")
            self.c_bill_no.set("")
            x = random.randint(1000, 9999)
            self.c_bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

            #self.save_bill()
    # def save_bill(self):
    #     a=messagebox.askyesno("save bill","Izzazt ho to save kr de")
    #     if a>0:
    #
    #     else:
    #         return



root=Tk()
########Bill app kak object bnaa liya or isme root jo window usko pass kr diya
obj=Bill_app(root)
root.mainloop()















