import streamlit as st
st.title("Welcome to zuni clothing brand")
st.header("Discover Your Style")
st.subheader("Shop the Latest Trends")

import pandas as pd
name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
adr = st.text_area("Enter Your Address : ")
classdata = st.selectbox("Enter Your Class : " ,(1,2,3,4,5,6,7,8))

button = st.button("Done")
if button :
    st.markdown(f""""
    Name : {name}
    Father : {fname}
    Address : {adr}
    Class : {classdata}""")
