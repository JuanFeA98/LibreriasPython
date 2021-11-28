import pandas as pd
import numpy as np

import streamlit as st

st.title("Uber Pickups in NY")


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Función para cargar los datos
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return (data)

# Cargar los datos en la app
data_load_state = st.text('Loading data...')

data = load_data(1000)

data_load_state.text('Loading data...done!')

# Mostrar los datos en la app
st.subheader('Raw data')
st.write(data)

# Pintando graficos en la app
# Histograma
st.subheader('Number of pickups by hour')

hist_load_state = st.text('Drawing histogram...')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hist_load_state = st.text('Drawing histogram...done!')

# Mapa
st.subheader('Map of all pickups')

map_load_state = st.text('Drawing a map...')
st.map(data)
map_load_state = st.text('Drawing a map...done!')
