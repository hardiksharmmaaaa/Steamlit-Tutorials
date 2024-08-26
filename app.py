import streamlit as st
import numpy as np 
import pandas as pd 

# adding the heading of the streamlit app 

st.title("Introduction to Streamlit")

#Displaying a Simple Text 
st.write("This is a simple Text")

df=pd.DataFrame({
    "FirstColumn":[1,2,3,4],
    "secondColumn":[5,6,7,8]
})

#Displaying the DataFrame
st.write("Here's The DataFrame")
st.write(df)

#Creating A line Chart 
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=["a","b","c"]
)

chart_data2=pd.DataFrame(
    np.random.randn(20,5),columns=["a","b","c","d","e"]
)
st.line_chart(chart_data)
st.bar_chart(chart_data2)