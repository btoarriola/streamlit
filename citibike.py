import pandas as pd
import streamlit as st
import numpy as np


st.title('Citibike')

DATE_COLUMN = 'started_at'
DATA_URL=('citibike-tripdata.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows ,index_col=0, encoding='latin-1')
    return data

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data = load_data(500)
st.subheader("Raw data")

sidebar = st.sidebar
st.sidebar.title('Heriberto Arriola Peztña ')
st.sidebar.text('zs2006737@estudiantes.uv.mx')
st.sidebar.markdown("___")
agree = sidebar.checkbox("Show raw data")
if agree:
    st.dataframe(data)
    st.sidebar.markdown("___")

if st.sidebar.checkbox('Recorridos por hora'):
    st.text('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
    st.sidebar.markdown("___")

hour_to_filter = sidebar.slider('hour', 0, 23, 5)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.text('Mapa de recorridos iniciados a las %s:00' % hour_to_filter)
st.map(filtered_data)

st.sidebar.image("Uv Anverso.png")