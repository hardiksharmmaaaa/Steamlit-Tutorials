import streamlit as st 
import pandas as pd
#components of Streamlit 

st.title("Streamlit input Text")

name=st.text_input("Enter Your Name! ")
age=st.slider("Enter your age:",0,100,25)
st.write(f"your Age is {age}")

options=["Python","c++","Java","JavaScript","Kotlin"]
choice=st.selectbox("Choose your Favourite Language",options)
st.write(f"You choose {choice}")
if name:
    st.write(f"Hello,{name}")
    
#Creating a upload Button 
uploaded_file=st.file_uploader("Choose a CSV File",type="CSV")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)    
    st.write(df)