import streamlit as st
import pandas as pd
import sqlite3
import re
import pickle
conn = sqlite3.connect('data.db')
c = conn.cursor()

st.set_page_config(page_title="Crop Recommendation", page_icon="fevicon.png", layout="centered", initial_sidebar_state="auto", menu_items=None)# Database Functions
#Database Functions

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
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
          f"""
          <style>
          .stApp {{
              background: url("https://removal.ai/wp-content/uploads/2021/09/black-background-03-unsplash.png");
              background-size: cover
          }}
          </style>
          """,
          unsafe_allow_html=True
      )
set_bg_hack_url()  

option = st.sidebar.selectbox("Select",["Home","Signup","Login","Contact Us"])


if (option == "Home"):
   st.markdown(
       """
       <h2 style="color:white">Welcome to Crop Recommendation</h2>
      <h1>    </h1>
      <p align="justify">
      <h5><b style="color:white">Indian economy is contributed heavily by agriculture. Most of the Indian farmers rely on their instincts to decide the crop to be sown at a particular time of year. They do not realize that the crop output is circumstantial, and depended heavily on the present-day weather and soil conditions. A single uninformed decision by the farmer can have undesirable consequences on the economic conditions of the region and also mental and financial impacts on the farmer himself. Applying systematic Machine Learning models will effectively help to alleviate this issue. The dataset used in the project is built by adding up the datasets of India's rainfall, climate, and Soil. Machine learning models will be used on the dataset to get the highest accuracy model to recommend a crop for the farm's location. This recommendation will help the farmers in India to make learned decisions about the crops. The recommendation will take into account the parameters like the farm's location, sowing season, soil properties, and climate.</b></h5>
      </p>
       """
       ,unsafe_allow_html=True)
    
    
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
                Email=st.text_input("Delete Email")
                st.button('Delete')
                delete_user(Email)
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result,columns=["FirstName","LastName","Mobile","City","Email","password","Cpassword"])
                st.dataframe(clean_db)
                
            elif login_user(Email,password):
                
                st.success("Logged In as {}".format(Email))
                N=st.slider("Enter Vaue of Nitrogen",0.0,140.0)
                P=st.slider("Enter Value of Phosphorus",5.0,145.0)
                K=st.slider("Enter Value of Potassium",5.0,205.0)
                TP=st.slider("Enter Value of Temperature",8.0,45.0)
                HD=st.slider("Enter Value of Humidity",14.0,100.0)
                PH=st.slider("Enter Value of PH",3.0,10.0)
                RF=st.slider("Enter Value of Rain Fall",20.0,300.0)
                Algo=st.selectbox("Algorithms:",["Support Vector Machine","Random Forest","K Nearest Neighbour","Decision Tree","Extra Tree","Naive Bayes"])
                a="Support Vector Machine" 
                b="Random Forest"
                c="K Nearest Neighbour"
                d="Decision Tree"                
                e="Extra Tree"
                f="Naive Bayes"
                
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
    st.text("pateljeel7016@gmail.com")
    st.text("6352859917")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("RAJPUT SAHITYARAJ")
    st.text("rajputsonu3055@gmail.com")
    st.text("9408351541")
