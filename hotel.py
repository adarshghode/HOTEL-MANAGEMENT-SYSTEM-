from tkinter import*
# for image import
from PIL import Image, ImageTk

# import client py file for cust button
from client import client_window

# import room py file for room button
from room import room_window

from detail import details_window


# Create class
class HotelManagementSystem:
    # Need to call construction
    def __init__(self, root):
        # Initialize root
        self.root = root
        # set title
        self.root.title("Hotel Managmemt System")
        # set geometry
        self.root.geometry("1550x800+0+0") #width x height + x-axis + y-axis


        # set Images
        # 1ST Image
        img1=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_image.jpeg") # r is used to recognize backward slash
        # resize image
        img1=img1.resize((1350,140),Image.LANCZOS) # antialias will convert high level image to low level
        #convert image with toolkit
        self.photoimg1=ImageTk.PhotoImage(img1)
        # showing image on windows with Label
        # set label
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE) # bd is border and relief is border style
        # show label
        lblimg.place(x=180,y=0,width=1350,height=140) # place will place the image in GUI

        #2nd Image
        img2=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_logo.jpg") 
        img2=img2.resize((180,140),Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE) 
        lblimg.place(x=0,y=0,width=180,height=140)

        ##############Title##############
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("Microsoft Sans Serif",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        ############ Frame, action will be performed herem##############
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        ##########Menu#############
        lbl_menu=Label(main_frame,text="MENU",font=("Microsoft Sans Serif",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230) # this will be in main_frame so need to set x y according to it and heigh will decided as per font size

        ###############menu frame##############
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=200)

        ###############button frame#############
        # here client_detail functio is pass, so if you click on client you will get on client windows. for this we will use command
        cust_btn = Button(btn_frame, text="CLIENT", command= self.client_details, width=20,font=("Microsoft Sans Serif",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2" ) # width is provided here instead of placed or grid option as above
        # use grid instead of placed
        cust_btn.grid(row=0,column=0, pady=1) # in grid we just provide row and column

        room_btn = Button(btn_frame, text="ROOM", command=self.room_details, width=20,font=("Microsoft Sans Serif",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2" )
        room_btn.grid(row=1,column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS",width=20, command=self.details, font=("Microsoft Sans Serif",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2" )
        details_btn.grid(row=2,column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT",width=20,font=("Microsoft Sans Serif",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2" )
        report_btn.grid(row=3,column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",width=20,font=("Microsoft Sans Serif",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2" )
        logout_btn.grid(row=4,column=0, pady=1)

        ###############3rd image on right side#################
        img3=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_1.jpg") 
        img3=img3.resize((1310,590),Image.LANCZOS) 
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE) 
        lblimg.place(x=225,y=0,width=1310,height=590)

        #############4th hotel bed image#############
        img4=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_bedroom.jpg") 
        img4=img4.resize((230,210),Image.LANCZOS) 
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE) 
        lblimg.place(x=0,y=225,width=230,height=210)

        ###########5th hotel food image###############
        img5=Image.open(r"C:\Career\Data Science project\Hotel management system\Images\hotel_food.jpg") 
        img5=img5.resize((230,210),Image.LANCZOS) 
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE) 
        lblimg.place(x=0,y=420,width=230,height=190)

    # Function to recall client
    def client_details(self):
        # need to open client window on main window
        self.new_window=Toplevel(self.root)
        # now pass client class in client windows
        self.app = client_window(self.new_window)

    # Function to recall room
    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app = room_window(self.new_window)

    # Function to recall details
    def details(self):
        self.new_window=Toplevel(self.root)
        self.app = details_window(self.new_window)






# call object in main function
if __name__ == "__main__":
    root=Tk() # give a toolkit to root

    # call object of class
    obj = HotelManagementSystem(root) # passed root

    # close the mainloop
    root.mainloop()