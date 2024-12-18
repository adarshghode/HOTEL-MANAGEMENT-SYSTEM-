from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class details_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        ################# Title ##################999*
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("Microsoft Sans Serif",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        ################# Hotel Logo ###########
        img_logo=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_logo.jpg") 
        img_logo=img_logo.resize((100,40),Image.LANCZOS) 
        self.photo_img_logo=ImageTk.PhotoImage(img_logo)
        lblimg=Label(self.root,image=self.photo_img_logo,bd=0,relief=RIDGE) 
        lblimg.place(x=5,y=2,width=100,height=50)

        ############## Label Frame #############
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font= ("Microsoft Sans Serif", 12, "bold"), padx=2) 
        labelframeleft.place(x=5, y=50, width= 540, height=350)

        # Floor
        self.var_floor=StringVar()
        lbl_floor = Label(labelframeleft, text="Floor", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_floor.grid(row=0, column=0, sticky= W)
        floor_entry = ttk.Entry(labelframeleft, textvariable=self.var_floor, width=20, font= ("Arial", 13,))
        floor_entry.grid(row=0, column=1, sticky= W)

        # Room Number
        self.var_room_no=StringVar()
        lbl_room_no = Label(labelframeleft, text="Room Number", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_room_no.grid(row=1, column=0, sticky= W)
        room_no_entry = ttk.Entry(labelframeleft, width=20, textvariable=self.var_room_no, font= ("Arial", 13,))
        room_no_entry.grid(row=1, column=1, sticky= W)

        # Room type
        self.var_room_type=StringVar()
        lbl_room_type = Label(labelframeleft, text="Room type", font= ("Microsoft Sans Serif", 12, "bold"), padx=2, pady= 6)
        lbl_room_type.grid(row=2, column=0, sticky= W)

        room_type_combobox = ttk.Combobox(labelframeleft, textvariable=self.var_room_type ,font= ("Arial", 13,), state="readonly")
        room_type_combobox["value"]=("Single", "Double", "Luxury")
        room_type_combobox.current(0)
        room_type_combobox.grid(row=2, column=1, sticky= W)
        


        #######################button###################
        room_btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        room_btn_frame.place(x=0, y=200, width=412, height=40)

        client_btn_add = Button(room_btn_frame, text="Add", command=self.add_data, font= ("Microsoft Sans Serif", 12, "bold"),bg='black', fg='gold', width=9,)
        client_btn_add.grid(row=0, column=0, padx=1)

        client_btn_update = Button(room_btn_frame, text="Update", command= self.update, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_update.grid(row=0, column=1, padx=1)

        client_btn_delete = Button(room_btn_frame, text="Delete", command=self.delete, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_delete.grid(row=0, column=2, padx=1)

        client_btn_reset = Button(room_btn_frame, text="Reset", command=self.reset, font= ("Microsoft Sans Serif", 12, "bold"), bg='black', fg='gold', width=9,)
        client_btn_reset.grid(row=0, column=3, padx=1)


        ####################  table frame search system #################
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show room Details", font= ("Microsoft Sans Serif", 12, "bold"), padx=2)
        table_frame.place(x=600, y=55, width= 600, height=350)

        # scroll bar
        # Declare scrollbar in frame
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(table_frame, columns=("Floor", "Room Number", "Room type"), xscrollcommand= scroll_x, yscrollcommand= scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # showing columns
        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("Room Number", text="Room Number")
        self.room_table.heading("Room type", text="Room type")
        
        # show columns
        self.room_table['show']='headings'
        
        #set width
        self.room_table.column("Floor", width=100)
        self.room_table.column("Room Number", width=100)
        self.room_table.column("Room type", width=100)

        # View columns
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
    
    # Add Function
    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root) # parent is used so error will be showd on client page only
        else:
            try:
                # making coonect with local sql database
                connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management")
                my_cursor = connection.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                self.var_floor.get(),
                self.var_room_no.get(),
                self.var_room_type.get(),
                ))

                connection.commit()
                self.fetch_data() # we declared this function later
                connection.close() # need to close connection
                messagebox.showinfo("Success", "New Room Added successfully", parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)
    
    # now to fetch data from database to show on table
    def fetch_data(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
        my_cursor = connection.cursor()
        my_cursor.execute("select * from details") 
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

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2])

    # Update function
    def update(self):
        if self.var_floor.get()=="" or self.var_room_no.get()=="":
            messagebox.showerror("Error","Please enter correct Floor or room number", parent=self.root)
        else:
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
            my_cursor = connection.cursor()
            my_cursor.execute("update details set Floor=%s,Room_type=%s where Room_No=%s", (
                self.var_floor.get(),
                self.var_room_type.get(),
                self.var_room_no.get(),
            )) 
            connection.commit()
            self.fetch_data()
            connection.close() 
            messagebox.showinfo("Update", "Room details has been updated successfully", parent=self.root)

    # DELETE Function
    def delete(self):
        delete=messagebox.askyesno("Are you sure", " Do you want to delete this room booking details", parent=self.root)
        if delete>0: #clicking on yes, 
            connection = mysql.connector.connect(host = "localhost", username = "root", password="Ad@12022000", database="management") 
            my_cursor = connection.cursor()
            delete_querry = "delete from details where Room_No=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(delete_querry, value)
            messagebox.showinfo("Deleted", "Room details has been deleted successfully", parent=self.root)
        else:
            if not delete:
                return
        connection.commit()
        self.fetch_data()
        connection.close()
    
    # RESET Function
    def reset(self):
        self.var_floor.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set("")




if __name__ == "__main__":
    root = Tk()
    obj = details_window(root)
    root.mainloop()