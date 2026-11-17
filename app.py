
import streamlit as st
import pandas as pd
import plotly_express as px
df= pd.read_csv('vehicles_us.csv')
st.header('Vehiculos US')
boton_uno = st.button('Construir histograma')
if boton_uno:
    st.write("Creacion histograma vehiculos vendidos")
    fig = px.histogram(df, x="price")
    st.plotly_chart(fig)
boton_dos = st.button('Construir grafico de dispersion')
if boton_dos:
    st.write("Creacion grafico de dispersion")
    fig = px.scatter(df, x="model_year", y="price", color="fuel")
    st.plotly_chart(fig)
    