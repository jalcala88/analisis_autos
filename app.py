import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

fig = px.histogram(car_data, x="odometer") # Crear histograma
        
st.title("Histograma Vehiculos")
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
build_histogram = st.checkbox("Construir un histograma")

if build_histogram: # al hacer clic en el botón
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


fig1 = px.scatter(car_data, x="odometer", y="price") # Crear diagrama dispersion
        
st.title("Diagrama de Dispersion")
st.write('Creación de un diagrama de dispersión para datos de anuncios de venta de coches')
build_disper = st.checkbox("Crear diagrama de dispersión")

if build_disper: # al hacer clic en el botón   
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)
