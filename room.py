from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class room_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        ########################### Variables ###############
        self.var_mobile_no=StringVar()
        self.var_check_in=StringVar()
        self.var_no_ofdays=StringVar()
        self.var_room_type=StringVar()
        self.var_room_available=StringVar()
        self.var_meal=StringVar()
        self.var_check_out=StringVar()
        self.var_paid_tax=StringVar()
        self.var_sub_total=StringVar()
        self.var_total=StringVar()

        ################# Title ##################
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Microsoft Sans Serif",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ################# Hotel Logo ###########
        img_logo=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_logo.jpg") 
        img_logo=img_logo.resize((100,40),Image.LANCZOS) 
        self.photo_img_logo=ImageTk.PhotoImage(img_logo)
        lblimg=Label(self.root,image=self.photo_img_logo,bd=0,relief=RIDGE) 
        lblimg.place(x=5,y=2,width=100,height=50)

        ############## Label Frame #############
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font= ("Microsoft Sans Serif", 12, "bold"), padx=2) 
        labelframeleft.place(x=5, y=50, width= 425, height=490)

        ############## labels and entrys #################
        # client contact
        lbl_client_contact = Label(labelframeleft, text="Client Contact", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_contact.grid(row=0, column=0, sticky= W) # sticky is used so it can be in west side
        client_ref_entry = ttk.Entry(labelframeleft, width=20, textvariable=self.var_mobile_no, font= ("Arial", 13,))
        client_ref_entry.grid(row=0, column=1, sticky= W)

        # Fetch button
        fethc_btn = Button(labelframeleft, text="Fetch", command=self.fetch_mobile_no, font= ("Microsoft Sans Serif", 10, "bold"), bg='black', fg='gold', width=9,)
        fethc_btn.grid(row=0, column=1, padx=1, sticky=E)

        # Check in date
        lbl_client_check_in = Label(labelframeleft, text="Check In Date", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_check_in.grid(row=1, column=0, sticky= W)
        client_check_in = ttk.Entry(labelframeleft, width=29, textvariable=self.var_check_in, font= ("Arial", 13,))
        client_check_in.grid(row=1, column=1)

        # No of days
        lbl_noofdays = Label(labelframeleft, text="No. Of days", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_noofdays.grid(row=2, column=0, sticky= W)
        noofdays = ttk.Entry(labelframeleft, width=29, textvariable=self.var_no_ofdays, font= ("Arial", 13,))
        noofdays.grid(row=2, column=1)

        # Room type
        lbl_room_type = Label(labelframeleft, text="Room type", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_room_type.grid(row=3, column=0, sticky= W)

        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select Room_type from details") 
        rows_3=my_cursor.fetchall() 

        room_type_combobox = ttk.Combobox(labelframeleft, width=27, textvariable=self.var_room_type ,font= ("Arial", 13,), state="readonly")
        room_type_combobox["value"]=rows_3
        room_type_combobox.current(0)
        room_type_combobox.grid(row=3,column=1)

        # Availble Room
        lbl_availble_rooms = Label(labelframeleft, text="Availble Rooms", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_availble_rooms.grid(row=4, column=0, sticky= W)
        
        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select Room_No from details") 
        rows_2=my_cursor.fetchall() 

        availble_rooms_combobox = ttk.Combobox(labelframeleft, width=27, textvariable=self.var_room_available ,font= ("Arial", 13,), state="readonly")
        availble_rooms_combobox["value"]=rows_2
        availble_rooms_combobox.current(0)
        availble_rooms_combobox.grid(row=4,column=1)

        # Meal
        lbl_meal = Label(labelframeleft, text="Meal", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_meal.grid(row=5, column=0, sticky= W)
        meal_cb = ttk.Combobox(labelframeleft, width=27, textvariable=self.var_meal, font= ("Arial", 13,), state="readonly")
        meal_cb['values'] = ("Lunch", "Break Fast", "Dinner")
        meal_cb.current(2)
        meal_cb.grid(row=5, column=1)

        # Check out date
        lbl_client_check_out = Label(labelframeleft, text="Check Out", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_check_out.grid(row=6, column=0, sticky= W)
        check_out = ttk.Entry(labelframeleft, width=29, textvariable=self.var_check_out, font= ("Arial", 13,))
        check_out.grid(row=6, column=1)

        # Paid tax
        lbl_paid_tax = Label(labelframeleft, text="Paid Tax", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_paid_tax.grid(row=7, column=0, sticky= W)
        paid_tax = ttk.Entry(labelframeleft, width=29, textvariable=self.var_paid_tax, font= ("Arial", 13,))
        paid_tax.grid(row=7, column=1)

        # Sub Total
        lbl_actual_total = Label(labelframeleft, text="Sub Total", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_actual_total.grid(row=8, column=0, sticky= W)
        actual_total = ttk.Entry(labelframeleft, width=29, textvariable=self.var_sub_total, font= ("Arial", 13,))
        actual_total.grid(row=8, column=1)

        # Total cost
        lbl_total_cost = Label(labelframeleft, text="Total Cost", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_total_cost.grid(row=9, column=0, sticky= W)
        total_cost = ttk.Entry(labelframeleft, width=29, textvariable=self.var_total, font= ("Arial", 13,))
        total_cost.grid(row=9, column=1)

        # Bill button
        bill_btn = Button(labelframeleft, text="Bill", command=self.bill, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        bill_btn.grid(row=10, column=0, padx=1, sticky=W)


        #######################button###################
        room_btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        room_btn_frame.place(x=0, y=400, width=412, height=40)

        client_btn_add = Button(room_btn_frame, text="Add", command=self.add_data, font= ("Microsoft Sans Serif", 12, "bold"),bg='black', fg='gold', width=9,)
        client_btn_add.grid(row=0, column=0, padx=1) # add data def passed here

        client_btn_update = Button(room_btn_frame, text="Update", command=self.update, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_update.grid(row=0, column=1, padx=1)

        client_btn_delete = Button(room_btn_frame, text="Delete", command=self.delete, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_delete.grid(row=0, column=2, padx=1)

        client_btn_reset = Button(room_btn_frame, text="Reset", command=self.reset, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_reset.grid(row=0, column=3, padx=1)

        ####################  table frame search system #################
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Details and Search", font= ("Microsoft Sans Serif", 12, "bold"), padx=2)
        table_frame.place(x=435, y=280, width= 860, height=260)

        client_search = Label(table_frame, text="Search By :", font= ("Microsoft Sans Serif", 12, "bold"), bg='red', fg='white')
        client_search.grid(row=0, column=0, padx=2, sticky=W)

        self.search_var=StringVar()
        client_search_option = ttk.Combobox(table_frame, textvariable=self.search_var, width=24, font= ("Arial", 13,), state="readonly")
        client_search_option['value'] = ('Mobile', 'Room')
        client_search_option.current(0)
        client_search_option.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        client_search_number = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font= ("Arial", 13,))
        client_search_number.grid(row=0, column=2, padx=2)

        search_btn = Button(table_frame, text="Search", command=self.search, font= ("Arial", 12, 'bold'), bg='black', fg='gold',width=9)
        search_btn.grid(row=0, column=3, padx=1)

        showall_btn = Button(table_frame, text="Show All", command=self.fetch_data, font= ("Arial", 12, 'bold'), bg='black', fg='gold', width=9,)
        showall_btn.grid(row=0, column=4, padx=1)

        ############# hotel bed image #############
        img_bed=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_bedroom.jpg") 
        img_bed=img_bed.resize((500,200),Image.LANCZOS) 
        self.photo_img_bed=ImageTk.PhotoImage(img_bed)
        lblimg=Label(self.root,image=self.photo_img_bed,bd=4,relief=RIDGE) 
        lblimg.place(x=760,y=55,width=500,height=200)

        ############################# show data table #############################
        table_frame = Frame(table_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=860, height=180)

        # scroll bar
        # Declare scrollbar in frame
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL) # hori and verti will decide scrollbar on which axis
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # tree table, treeview used for grid system
        self.room_table = ttk.Treeview(table_frame, columns=("Mobile No", "Check In", "No ofdays", "Room type", "Room", "Meal", "Check Out"), xscrollcommand= scroll_x, yscrollcommand= scroll_y)

        # positioning scrolbar
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # viewing scrollbar
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # showing columns
        # declare columns headings
        self.room_table.heading("Mobile No", text="Mobile No")
        self.room_table.heading("Check In", text="Check In")
        self.room_table.heading("No ofdays", text="No ofdays")
        self.room_table.heading("Room type", text="Room type")
        self.room_table.heading("Room", text="Room")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("Check Out", text="Check Out")
        
        # show columns
        self.room_table['show']='headings'
        
        #set width
        self.room_table.column("Mobile No", width=100)
        self.room_table.column("Check In", width=100)
        self.room_table.column("No ofdays", width=100)
        self.room_table.column("Room type", width=100)
        self.room_table.column("Room", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("Check Out", width=100)

        # View columns
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor) # we declared this function later to add details in add section once we click on rows in screen table
        self.fetch_data()

    ################ Fetching data from sql client database #########################
    def fetch_mobile_no(self):
        if self.var_mobile_no.get() == '':
            messagebox.showerror('Error', 'Please enter Mobile Number', parent=self.root)    
        else:
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
            my_cursor = connection.cursor()
            querry = ("select Name from management.client where Mobile=%s")
            value=(self.var_mobile_no.get(),)
            my_cursor.execute(querry, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number not found", parent= self.root)
            else:
                connection.commit()
                connection.close()

                # showing data from database
                showdataframe= Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showdataframe.place(x=450, y=55, width=300, height=180)

                ########## Showing Name ################
                lblname= Label(showdataframe, text='Name: ', font=("arial", 12, 'bold'))
                lblname.grid(row=0, column=0)
                lblname_show_name = Label(showdataframe, text=row, font=("arial", 12, 'bold'))
                lblname_show_name.grid(row=0, column=1)

                ############### Showing gender #################
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                querry = ("select Gender from management.client where Mobile=%s")
                value=(self.var_mobile_no.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblgender= Label(showdataframe, text='Gender : ', font=("arial", 12, 'bold'))
                lblgender.grid(row=1, column=0)
                lblgender_show = Label(showdataframe, text=row, font=("arial", 12, 'bold'))
                lblgender_show.grid(row=1, column=1)

                ############### Showing email #################
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                querry = ("select Email from management.client where Mobile=%s")
                value=(self.var_mobile_no.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblemail= Label(showdataframe, text='Email : ', font=("arial", 12, 'bold'))
                lblemail.grid(row=2, column=0)
                lblemail_show = Label(showdataframe, text=row, font=("arial", 12, 'bold'))
                lblemail_show.grid(row=2, column=1)

                ############### Showimg Nationality #################
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                querry = ("select Nationality from management.client where Mobile=%s")
                value=(self.var_mobile_no.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblnation= Label(showdataframe, text='Nationality : ', font=("arial", 12, 'bold'))
                lblnation.grid(row=3, column=0)
                lblnation_show = Label(showdataframe, text=row, font=("arial", 12, 'bold'))
                lblnation_show.grid(row=3, column=1)

                ############### Showimg Address #################
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                querry = ("select Address from management.client where Mobile=%s")
                value=(self.var_mobile_no.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblnation= Label(showdataframe, text='Address : ', font=("arial", 12, 'bold'))
                lblnation.grid(row=4, column=0)
                lblnation_show = Label(showdataframe, text=row, font=("arial", 12, 'bold'))
                lblnation_show.grid(row=4, column=1)

                ############### Showimg Address #################
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                querry = ("select Address from management.client where Mobile=%s")
                value=(self.var_mobile_no.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lbladdress= Label(showdataframe, text='Address : ', font=("arial", 12, 'bold'))
                lbladdress.grid(row=4, column=0)
                lbladdress_show = Label(showdataframe, text=row, font=("arial", 12, 'bold'))
                lbladdress_show.grid(row=4, column=1)


    def bill(self):
        # setting date and time
        in_date=self.var_check_in.get()
        out_date=self.var_check_out.get()
        in_date=datetime.strptime(in_date, "%d/%m/%Y")
        out_date=datetime.strptime(out_date, "%d/%m/%Y")
        self.var_no_ofdays.set(abs(out_date-in_date).days)

        if (self.var_room_type.get() == 'Single' and self.var_meal.get() == 'Break Fast'):
            r1=float(1000)
            m1=float(500)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)
        
        elif (self.var_room_type.get() == 'Double' and self.var_meal.get() == 'Break Fast'):
            r1=float(2000)
            m1=float(500)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)

        elif (self.var_room_type.get() == 'Luxury' and self.var_meal.get() == 'Break Fast'):
            r1=float(3000)
            m1=float(500)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)
        
        elif (self.var_room_type.get() == 'Single' and self.var_meal.get() == 'Lunch'):
            r1=float(1000)
            m1=float(1000)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)
        
        elif (self.var_room_type.get() == 'Double' and self.var_meal.get() == 'Lunch'):
            r1=float(2000)
            m1=float(1000)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)
        
        elif (self.var_room_type.get() == 'Luxury' and self.var_meal.get() == 'Lunch'):
            r1=float(3000)
            m1=float(1000)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)
        
        elif (self.var_room_type.get() == 'Single' and self.var_meal.get() == 'Dinner'):
            r1=float(1000)
            m1=float(1500)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)

        elif (self.var_room_type.get() == 'Double' and self.var_meal.get() == 'Dinner'):
            r1=float(2000)
            m1=float(1500)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)
        
        elif (self.var_room_type.get() == 'Luxury' and self.var_meal.get() == 'Dinner'):
            r1=float(3000)
            m1=float(1500)
            r1_sum_m1= float(r1 + m1)
            d1=float(self.var_no_ofdays.get())
            st= float(r1_sum_m1*d1)
            tax = float(st*0.18)
            tax_str= "Rs. "+ str("%.2f"%(tax))
            st_str = "Rs. " + str("%.2f"%(st))
            tc= float(st + tax)
            tc_str = "Rs. " + str("%.2f"%(tc))
            self.var_paid_tax.set(tax_str) 
            self.var_sub_total.set(st_str)
            self.var_total.set(tc_str)





    

    # Add Function
    def add_data(self):
        if self.var_mobile_no.get()=="" or self.var_check_in.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root) # parent is used so error will be showd on client page only
        else:
            try:
                # making coonect with local sql database
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                self.var_mobile_no.get(),
                self.var_check_in.get(),
                self.var_no_ofdays.get(),
                self.var_room_type.get(),
                self.var_room_available.get(),
                self.var_meal.get(),
                self.var_check_out.get(),
                ))

                connection.commit()
                self.fetch_data() # we declared this function later
                connection.close() # need to close connection
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)
    
    # now to fetch data from database to show on table
    def fetch_data(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select * from room") 
        rows_1=my_cursor.fetchall() 
        if len(rows_1)!=0:
            self.room_table.delete(*self.room_table.get_children()) 
            for i in rows_1:
                self.room_table.insert("",END, values=i)

            connection.commit()
        connection.close()
    
    # once we click on row showing on screen, it should be added in room details
    def get_cursor(self, event=""):
        cursor_row=self.room_table.focus() #  need to focus cursor
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_mobile_no.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_no_ofdays.set(row[2])
        self.var_room_type.set(row[3]),
        self.var_room_available.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_check_out.set(row[6])

    
    # UPDATE Function
    def update(self):
        if self.var_mobile_no.get()=="" or self.var_check_in.get()=="":
            messagebox.showerror("Error","Please enter correct mobile number or check In date", parent=self.root)
        else:
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
            my_cursor = connection.cursor()
            my_cursor.execute("update room set check_in=%s,no_Ofdays=%s,room_type=%s,Room=%s,Meal=%s,check_out=%s where Mobile=%s", ( # will use where because it will change values according to mobile no of client 
                self.var_check_in.get(),
                self.var_no_ofdays.get(),
                self.var_room_type.get(),
                self.var_room_available.get(),
                self.var_meal.get(),
                self.var_check_out.get(),
                self.var_mobile_no.get() 
            )) 
            connection.commit()
            self.fetch_data()
            connection.close() 
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent=self.root)
    

    # DELETE Function
    def delete(self):
        delete=messagebox.askyesno("Are you sure", " Do you want to delete this client booking details", parent=self.root)
        if delete>0: #clicking on yes, 
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
            my_cursor = connection.cursor()
            delete_querry = "delete from room where Mobile=%s"
            value=(self.var_mobile_no.get(),)
            my_cursor.execute(delete_querry, value)
            messagebox.showinfo("Deleted", "Customer details has been deleted successfully", parent=self.root)
        else:
            if not delete:
                return
        connection.commit()
        self.fetch_data()
        connection.close()
    
    # RESET Function
    def reset(self):
        self.var_mobile_no.set(""),
        self.var_check_in.set(""),
        self.var_no_ofdays.set("")
        # self.var_room_type.set(""),
        self.var_room_available.set(""),
        # self.var_meal.set(""),
        self.var_check_out.set("")
        self.var_paid_tax.set("")
        self.var_sub_total.set("")
        self.var_total.set("")

    # Search in room table
    def search(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    








if __name__ == "__main__":
    root = Tk()
    obj = room_window(root)
    root.mainloop()