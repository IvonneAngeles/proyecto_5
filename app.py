import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') #leer los datos
hist_button = st.button('Construir histograma') #crear un botón
grap_button = st.button('Construir gráfico de dispersión') #crear boton del gráfico
build_histogram = st.checkbox('Construir un histograma') #casilla de verificación 
build_graphic = st.checkbox('Construir un gráfico') #casilla de verificación  

st.header('Datos de los anuncios de venta de choches')

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Comparación entre precio y modelo')
            # crear un histograma
    fig = px.histogram(car_data, x="model", y="price")
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if grap_button:
    st.write('Comparación del año del modelo y los días listados')

    fig_2 = px.scatter(car_data, x="model_year", y="days_listed") #crear gráfico de dispersión 

    st.plotly_chart(fig_2, use_container_width=True)

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Comparación entre precio y modelo')
    st.plotly_chart(fig, use_container_width=True)