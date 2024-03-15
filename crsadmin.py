import streamlit as st
import pandas as pd
import sqlite3
import re

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Database Functions

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(FirstName TEXT,LastName TEXT,Mobile TEXT,City TEXT,Email TEXT,password TEXT,Cpassword TEXT)')
def add_userdata(FirstName,LastName,Mobile,City,Email,password,Cpassword):
    c.execute('INSERT INTO usertable(FirstName,LastName,Mobile,City,Email,password,Cpassword) VALUES (?,?,?,?,?,?,?)',(FirstName,LastName,Mobile,City,Email,password,Cpassword))
    conn.commit()
def login_user(Email,password):
    c.execute('SELECT * FROM usertable WHERE Email =? AND password = ?',(Email,password))
    data = c.fetchall()
    return data
def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data
def delete_user(Email):
    c.execute("DELETE FROM usertable WHERE Email="+"'"+Email+"'")
    conn.commit()
    

option = st.sidebar.selectbox("Select",["Home","Signup","Login","Contact Us"])

if (option == "Home"):
    st.title("CROP RECOMMENDATION SYSTEM")
    
if (option == "Signup"):
    FName = st.text_input("Enter First Name")
    LName = st.text_input("Enter Last Name")    
    Mnumber = st.text_input("Enter Mobile Number")
    Email = st.text_input("Enter your Email ID")
    City = st.text_input("Enter city")
    Pass = st.text_input("Enter Password",type='password')
    Cpass = st.text_input("Confirm Password",type='password')
    if st.button("Submit"):
        st.success("You have successfully Signed Up")
        pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if Pass==Cpass:
            if (pattern.match(Mnumber)):
                if re.fullmatch(regex, Email):
                    create_usertable()
                    add_userdata(FName,LName,Mnumber,City,Email,Pass,Cpass)
                else:
                    st.error("Email is Wrong")
            else:
                st.error("Mobile is Wrong")
        else:
            st.error("Password not match")
        
    
if (option == "Login"):
    Email=st.sidebar.text_input("Email")
    password=st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("LOGIN"):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, Email):
            if login_user(Email,password):
                st.success("Logged In as {}".format(Email))
                Email1=st.text_input("Delete Email")
                if st.button('Delete'):
                    delete_user(Email1)
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result,columns=["FirstName","LastName","Mobile","City","Email","password","Cpassword"])
                st.dataframe(clean_db)
                
            else:
                st.error("Wrong Details")
        else:
            st.error("Email Wrong")
        

if (option == "Contact Us"):
    st.text("JEEL K. PATEL")
    st.text("RAJPUT SAHITYARAJ")
    st.text("xyz@gmail.com")
    st.text("6252152425")