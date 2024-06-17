import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Datos de los anuncios de venta de choches')
        
car_data = pd.read_csv('vehicles_us.csv') #leer los datos
hist_button = st.button('Construir histograma') #crear un botón
grap_button = st.button('Construir gráfico de dispersión') #crear boton del gráfico
general_data = st.checkbox('Datos generales') #casilla de verificación 

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

if general_data: # si la casilla de verificación está seleccionada
    st.table(car_data.head(100))