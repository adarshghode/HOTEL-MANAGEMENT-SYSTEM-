from tkinter import*
from PIL import Image, ImageTk

#for stylish entry (box)
from tkinter import ttk

#import sql for database
import mysql.connector

import random
from tkinter import messagebox

class client_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        ##############variables###########################
        #variable for sql database
        self.var_ref=StringVar() #int var used for calculation and string var used for fixed number
        x=random.randint(1000,9999) # will take random number
        self.var_ref.set(str(x))

        self.var_client_name=StringVar()
        self.var_name=StringVar()
        self.var_mother_name=StringVar()
        self.var_gender=StringVar()
        self.var_post_code=StringVar()
        self.var_mobile_no=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_no=StringVar()
        self.var_address=StringVar()


        ################# Title ##################
        lbl_title=Label(self.root,text="ADD CLIENT DETAILS",font=("Microsoft Sans Serif",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ################# Hotel Logo ###########
        img_logo=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_logo.jpg") 
        img_logo=img_logo.resize((100,40),Image.LANCZOS) 
        self.photo_img_logo=ImageTk.PhotoImage(img_logo)
        lblimg=Label(self.root,image=self.photo_img_logo,bd=0,relief=RIDGE) 
        lblimg.place(x=5,y=2,width=100,height=50)

        ############## Label Frame #############
        # previusly we used Label only, diff in label and lable frame is in lable frame we can use text
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Client Details", font= ("Microsoft Sans Serif", 12, "bold"), padx=2) # padx and pady is used for distance from x and y
        labelframeleft.place(x=5, y=50, width= 425, height=490)
        
        ############## labels and entrys #################
        # client ref
        lbl_client_ref = Label(labelframeleft, text="Client Ref", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_ref.grid(row=0, column=0, sticky= W)
        # entry box
        client_ref_entry = ttk.Entry(labelframeleft, width=29, textvariable= self.var_ref ,font= ("Arial", 13,), state='readonly') #text variable, we declared variable to save in this database
        client_ref_entry.grid(row=0, column=1)

        # client name
        lbl_client_name = Label(labelframeleft, text="Client Name", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_name.grid(row=1, column=0, sticky= W)
        client_name_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.var_name,font= ("Arial", 13,))
        client_name_entry.grid(row=1, column=1)

        # mother name
        lbl_client_mother_name = Label(labelframeleft, text="Mother Name", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_mother_name.grid(row=2, column=0, sticky= W)
        client_mother_name_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.var_mother_name,font= ("Arial", 13,))
        client_mother_name_entry.grid(row=2, column=1)

        # gender combobox, limited option to select
        lbl_client_gender = Label(labelframeleft, text="Gender", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_gender.grid(row=3, column=0, sticky= W)
        # combobox for gender
        client_gender_combobox = ttk.Combobox(labelframeleft, width=27, textvariable=self.var_gender, font= ("Arial", 13,), state="readonly") # readonly will give only option, can't write
        client_gender_combobox["value"]=("Male", "Female", "Other")
        client_gender_combobox.current(0)
        client_gender_combobox.grid(row=3, column=1)

        #post code
        lbl_client_post_code = Label(labelframeleft, text="Post Code", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_post_code.grid(row=4, column=0, sticky= W)
        client_post_code_entry = ttk.Entry(labelframeleft, textvariable=self.var_post_code , width=29, font= ("Arial", 13,))
        client_post_code_entry.grid(row=4, column=1)

        #mobile
        lbl_client_mobile = Label(labelframeleft, text="Mobile No.", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_mobile.grid(row=5, column=0, sticky= W)
        client_mobile_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.var_mobile_no ,font= ("Arial", 13,))
        client_mobile_entry.grid(row=5, column=1)

        #Email
        lbl_client_email = Label(labelframeleft, text="Client Email", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_email.grid(row=6, column=0, sticky= W)
        client_email_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.var_email ,font= ("Arial", 13,))
        client_email_entry.grid(row=6, column=1)

        #Nationality combobox
        lbl_client_nationality = Label(labelframeleft, text="Client Nationality", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_nationality.grid(row=7, column=0, sticky=W)
        client_nationality_combobox = ttk.Combobox(labelframeleft, width=29, textvariable=self.var_nationality ,font= ("Arial", 13,), state="readonly")
        client_nationality_combobox["value"] =  ( "Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria",
        "Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil",
        "Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Central African Republic","Chad","Chile","China","Colombia","Comoros",
        "Congo, Democratic Republic of the","Congo, Republic of the","Costa Rica","Côte d'Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica",
        "Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","Gambia",
        "Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland",
        "Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, North","Korea, South","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia",
        "Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia",
        "Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Macedonia",
        "Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis",
        "Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia",
        "Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania",
        "Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine")
        client_nationality_combobox.current(77)
        client_nationality_combobox.grid(row=7, column=1)

        #ID proof type combobox
        lbl_client_id_proof = Label(labelframeleft, text="Client ID proof.", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_id_proof.grid(row=8, column=0, sticky= W)
        client_id_proof_combobox = ttk.Combobox(labelframeleft, width=29, textvariable=self.var_id_proof ,font= ("Arial", 13,), state="readonly")
        client_id_proof_combobox['value'] = ['Aadhar Card', 'Driving Liscense', 'Voter ID', 'Passport', 'Pan Card']
        client_id_proof_combobox.current(0)
        client_id_proof_combobox.grid(row=8, column=1)

        #ID number
        lbl_client_id = Label(labelframeleft, text="Client ID no.", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_id.grid(row=9, column=0, sticky= W)
        client_id_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.var_id_no ,font= ("Arial", 13,))
        client_id_entry.grid(row=9, column=1)

        # Address
        lbl_client_address = Label(labelframeleft, text="Client Address", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_client_address.grid(row=10, column=0, sticky= W)
        client_address_entry = ttk.Entry(labelframeleft, width=29, textvariable=self.var_address ,font= ("Arial", 13,))
        client_address_entry.grid(row=10, column=1)

        #######################button###################
        client_btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        client_btn_frame.place(x=0, y=400, width=412, height=40)

        client_btn_add = Button(client_btn_frame, text="Add", font= ("Microsoft Sans Serif", 12, "bold"), command=self.add_data ,bg='black', fg='gold', width=9,)
        client_btn_add.grid(row=0, column=0, padx=1) # add data def passed here

        client_btn_update = Button(client_btn_frame, text="Update", command=self.update, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_update.grid(row=0, column=1, padx=1)

        client_btn_delete = Button(client_btn_frame, text="Delete", command=self.delete,font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_delete.grid(row=0, column=2, padx=1)

        client_btn_reset = Button(client_btn_frame, text="Reset", command=self.reset, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_reset.grid(row=0, column=3, padx=1)

        ####################  table frame search system #################
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Details and Search", font= ("Microsoft Sans Serif", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width= 860, height=490)

        client_search = Label(table_frame, text="Search By :", font= ("Microsoft Sans Serif", 12, "bold"), bg='red', fg='white')
        client_search.grid(row=0, column=0, padx=2, sticky=W)

        self.search_var=StringVar()
        client_search_option = ttk.Combobox(table_frame, textvariable=self.search_var, width=24, font= ("Arial", 13,), state="readonly")
        client_search_option['value'] = ('Mobile', 'Ref')
        client_search_option.current(0)
        client_search_option.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        client_search_number = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font= ("Arial", 13,))
        client_search_number.grid(row=0, column=2, padx=2)

        search_btn = Button(table_frame, text="Search", command=self.search, font= ("Arial", 12, 'bold'), bg='black', fg='gold',width=9)
        search_btn.grid(row=0, column=3, padx=1)

        showall_btn = Button(table_frame, command=self.fetch_data, text="Show All", font= ("Arial", 12, 'bold'), bg='black', fg='gold', width=9,)
        showall_btn.grid(row=0, column=4, padx=1)

        ############################# show data table #############################
        table_frame = Frame(table_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=860, height=350)

        # scroll bar
        # Declare scrollbar in frame
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL) # hori and verti will decide scrollbar on which axis
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # tree table, treeview used for grid system
        self.client_details_table = ttk.Treeview(table_frame, columns=("Ref", "Name", "Mother Name", "Gender", "Post Code", "Mobile No.", "Email", "Nationality", "ID Proof", "ID No.", "Address"), xscrollcommand= scroll_x, yscrollcommand= scroll_y)

        # positioning scrolbar
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # viewing scrollbar
        scroll_x.config(command=self.client_details_table.xview)
        scroll_y.config(command=self.client_details_table.yview)

        # showing columns
        # declare columns headings
        self.client_details_table.heading("Ref", text="Refer No.")
        self.client_details_table.heading("Name", text="Name")
        self.client_details_table.heading("Mother Name", text="Mother Name")
        self.client_details_table.heading("Gender", text="Gender")
        self.client_details_table.heading("Post Code", text="Post Code")
        self.client_details_table.heading("Mobile No.", text="Mobile No.")
        self.client_details_table.heading("Email", text="Email")
        self.client_details_table.heading("Nationality", text="Nationality")
        self.client_details_table.heading("ID Proof", text="ID Proof")
        self.client_details_table.heading("ID No.", text="ID No.")
        self.client_details_table.heading("Address", text="Address")
        # show columns
        self.client_details_table['show']='headings'
        
        #set width
        self.client_details_table.column("Ref", width=100)
        self.client_details_table.column("Name", width=100)
        self.client_details_table.column("Mother Name", width=100)
        self.client_details_table.column("Gender", width=100)
        self.client_details_table.column("Post Code", width=100)
        self.client_details_table.column("Mobile No.", width=100)
        self.client_details_table.column("Email", width=100)
        self.client_details_table.column("Nationality", width=100)
        self.client_details_table.column("ID Proof", width=100)
        self.client_details_table.column("ID No.", width=100)
        self.client_details_table.column("Address", width=100)

        # View columns
        self.client_details_table.pack(fill=BOTH, expand=1)

        # Binding the table in add client details section
        self.client_details_table.bind("<ButtonRelease-1>", self.get_cursor) # we declared this function later to add details in add section once we click on rows in screen table
        self.fetch_data() # we declared this function later

    #working on ADD button
    # here we will use mySQL Database
    def add_data(self):
        if self.var_mobile_no.get()=="" or self.var_mother_name.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root) # parent is used so error will be showd on client page only
        else:
            try:
                # making coonect with local sql database
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") # declared database which is already created

                # with curson we declare columns
                my_cursor = connection.cursor()
                my_cursor.execute("insert into client values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( #we use %s for how many columns and pass tuple to declare variable
                self.var_ref.get(),
                self.var_name.get(),
                self.var_mother_name.get(),
                self.var_gender.get(),
                self.var_post_code.get(),
                self.var_mobile_no.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_no.get(),
                self.var_address.get(),
                ))

                connection.commit()
                self.fetch_data() # we declared this function later
                connection.close() # need to close connection
                messagebox.showinfo("Success", "Client details has been added", parent=self.root) # parent root will show error in this section only

            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)
    
    # now to fetch data from database to show on table
    def fetch_data(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select * from client") #write sql querry from database
        rows=my_cursor.fetchall() # declare variable for fetched data
        if len(rows)!=0: # if there's a already a recorded data in database
            self.client_details_table.delete(*self.client_details_table.get_children()) # to delete column children
            for i in rows:
                self.client_details_table.insert("",END, values=i)

            connection.commit()
        connection.close()    

    # once we click on row showing on screen, it should be added in client detials
    def get_cursor(self, event=""):
        cursor_row=self.client_details_table.focus() #  need to focus cursor
        content=self.client_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_mother_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post_code.set(row[4]),
        self.var_mobile_no.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_no.set(row[9]),
        self.var_address.set(row[10])

    #working on UPDATE button
    # here we will use mySQL Database
    def update(self):
        if self.var_mobile_no.get()=="":
            messagebox.showerror("Error","Please enter mobile number", parent=self.root)
        else:
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
            my_cursor = connection.cursor()
            my_cursor.execute("update client set Name=%s,Mother_name=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,ID_proof=%s,ID_No=%s,Address=%s where Ref=%s", ( # will use where because it will change values according to mobile no of client 
                self.var_name.get(),
                self.var_mother_name.get(),
                self.var_gender.get(),
                self.var_post_code.get(),
                self.var_mobile_no.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_no.get(),
                self.var_address.get(),
                self.var_ref.get()    
            )) 
            connection.commit()
            self.fetch_data()
            connection.close() 
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent=self.root)
    
    #working on DELETE button
    # here we will use mySQL Database
    def delete(self):
        delete=messagebox.askyesno("Are you sure", " Do you want to delete this client details", parent=self.root)
        if delete>0: #clicking on yes, 
            # we have to declare connection everytime 
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
            my_cursor = connection.cursor()
            delete_querry = "delete from client where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(delete_querry, value)
            messagebox.showinfo("Deleted", "Customer details has been deleted successfully", parent=self.root)
        else:
            if not delete:
                return
        connection.commit()
        self.fetch_data()
        connection.close() 

    #working on RESET button
    # here we will use mySQL Database
    def reset(self):
        #self.var_ref.set(""),
        self.var_name.set(""),
        self.var_mother_name.set(""),
        #self.var_gender.set(""),
        self.var_post_code.set(""),
        self.var_mobile_no.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_no.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999) # will take random number
        self.var_ref.set(str(x))

    # search data in database
    def search(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select * from client where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.client_details_table.delete(*self.client_details_table.get_children())
            for i in rows:
                self.client_details_table.insert("",END,values=i)
            connection.commit()
        connection.close()





if __name__ == "__main__":
    root = Tk()
    obj = client_window(root)
    root.mainloop()