from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from Customerlist import*
from Checkin import*
from add_customer_details import*
from roomlist import*
import mysql.connector

print("Started")
con = mysql.connector.connect(host="127.0.0.1",user="root",password="Aline-12#",database="Hotel_man")
cur =con.cursor()
mycursor = con.cursor()
cursor = con.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Hotel__man")

cursor = con.cursor()
cursor.execute("USE Hotel__man")

mycursor.execute("CREATE TABLE cust (FNAME VARCHAR(20) PRIMARY KEY NOT NULL, LNAME VARCHAR(20) NOT NULL, PHNO int NOT NULL)")
mycursor.execute("CREATE TABLE issued_rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, issuedto VARCHAR(30) NOT NULL, status VARCHAR(30) NOT NULL)")
mycursor.execute("CREATE TABLE rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, RoomType VARCHAR(30) NOT NULL, status VARCHAR(30) NOT NULL)")
mycursor = con.cursor()



root = Tk()
root.title("Hotel Managment")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.25

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Shrey's Hotel", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Customer Details", bg='Black',fg='white',command =add_customer_details)
btn1.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)

btn2 = Button(root, text="Check In", bg='Black',fg='white',command=checkinn)
btn2.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)


btn3 = Button(root,text="Check Out",bg='black', fg='white',command=checkout)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Add Rooms",bg='black', fg='white',command = addrooms)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

root.mainloop()
