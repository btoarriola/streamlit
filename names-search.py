import streamlit as st
import pandas as pd

st.title("search names")
DATA_URL= 'dataset.csv'

@st.cache
def load_data_byname(name):
    data=pd.read_csv(DATA_URL)
    filtered_data_byname = data[data["name"].str.contains(name)]
    return filtered_data_byname

myname = st.text_input("nombre: ")
if(myname):
    filterbyname = load_data_byname(myname)
    count_now = filterbyname.shape[0]
    st.write(f"total names : {count_now}")
    st.dataframe(filterbyname)