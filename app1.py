import sklearn
import streamlit as st
import pandas as pd
import sqlite3
import re
import pickle
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
        pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if Pass==Cpass:
            if (pattern.match(Mnumber)):
                if re.fullmatch(regex, Email):
                    create_usertable()
                    add_userdata(FName,LName,Mnumber,City,Email,Pass,Cpass)
                    st.success("Signup Success")
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
            if Email=="admin5911@gmail.com" and password=="5911":
                Email1=st.text_input("Delete Email")
                st.button('Delete')
                delete_user(Email1)
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result,columns=["FirstName","LastName","Mobile","City","Email","password","Cpassword"])
                st.dataframe(clean_db)
                
            elif login_user(Email,password):
                
                st.success("Logged In as {}".format(Email))
                N=st.slider("Enter Vaue of N",0.0,140.0)
                P=st.slider("Enter Value of P",5.0,145.0)
                K=st.slider("Enter Value of K",5.0,205.0)
                TP=st.slider("Enter Value of TP",8.0,45.0)
                HD=st.slider("Enter Value of HD",14.0,100.0)
                PH=st.slider("Enter Value of PH",3.0,10.0)
                RF=st.slider("Enter Value of RF",20.0,300.0)
                Algo=st.selectbox("Algorithms:",["SVM","RF","KNN","DT","ET","NB"])
                a="SVM" 
                b="RF"
                c="KNN"
                d="DT"                
                e="ET"
                f="NB"
                
                if st.button("Predict"):
                    if Algo==a:
                        data=[float(N),float(P),float(K),float(TP),float(HD),float(PH),float(RF)]
                        model=pickle.load(open("model-svm-crop.pkl","rb"))
                        st.success(model.predict([data])[0])
                    elif Algo==b:
                        data=[float(N),float(P),float(K),float(TP),float(HD),float(PH),float(RF)]
                        model=pickle.load(open("model-rf-crop.pkl","rb"))
                        st.success(model.predict([data])[0])
                    elif Algo==c:
                        data=[float(N),float(P),float(K),float(TP),float(HD),float(PH),float(RF)]
                        model=pickle.load(open("model-KNN-crop.pkl","rb"))
                        st.success(model.predict([data])[0])
                    elif Algo==d:
                        data=[float(N),float(P),float(K),float(TP),float(HD),float(PH),float(RF)]
                        model=pickle.load(open("model-dt-crop.pkl","rb"))
                        st.success(model.predict([data])[0])
                    elif Algo==e:
                        data=[float(N),float(P),float(K),float(TP),float(HD),float(PH),float(RF)]
                        model=pickle.load(open("model-et-crop.pkl","rb"))
                        st.success(model.predict([data])[0])
                    elif Algo==f:
                        data=[float(N),float(P),float(K),float(TP),float(HD),float(PH),float(RF)]
                        model=pickle.load(open("model-nb-crop.pkl","rb"))
                        st.success(model.predict([data])[0])
                    
            else:
                st.error("Wrong Details")
        else:
            st.error("Email Wrong")
        

if (option == "Contact Us"):
    st.text("JEEL K. PATEL")
    st.text("RAJPUT SAHITYARAJ")
    st.text("xyz@gmail.com")
    st.text("6352859917")
    
    
