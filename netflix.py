import pandas as pd
import streamlit as st
import codecs

name_link = 'movies.csv'

# Create the title for the web app
st.title("Netflix App - Heriberto Arriola Peztña")
st.write("s20006737")
sidebar = st.sidebar


#cache de 500
@st.cache
def load_data(nrows):
    doc = codecs.open('movies.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    return data
data = load_data(500)


#metodo de buscar por 
def load_data_bydirector(director):
    doc = codecs.open('movies.csv', 'rU', 'latin1')
    data=pd.read_csv(doc)
    filtered_data_bysex = data[data["director"]== director]
    return filtered_data_bysex

#metodo de buscar nombre
def load_data_byname(name):
    doc = codecs.open('movies.csv', 'rU', 'latin1')
    data=pd.read_csv(doc)
    name_lower = name.lower()
    filtered_data_byname = data[data["name"].str.contains(name_lower)]
    return filtered_data_byname


# checkbox de mostrar 
agree = sidebar.checkbox("Mostrar todos los filmes")

#buscar por nombre
myname = sidebar.text_input("nombre: ")
botonname = sidebar.button("Search by name ")

if(botonname):
    filterbyname = load_data_byname(myname)
    count_now = filterbyname.shape[0]
    st.write(f"total names : {count_now}")
    data=filterbyname

selected_sex= sidebar.selectbox("Select director", data['director'].unique())
botonseleccion = sidebar.button("Search by director ")

if (botonseleccion):
    filterbysex = load_data_bydirector(selected_sex)
    count_now = filterbysex.shape[0]
    st.write(f"total items : {count_now}")
    data=filterbysex



if agree:
  
  st.dataframe(data)