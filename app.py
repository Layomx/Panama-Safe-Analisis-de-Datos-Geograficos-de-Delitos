import streamlit as st
import pandas as pd
import plotly.express as px
import src.web_config as wc
import src.data_loader as dl
import src.visualizations as vz

# Configuracion de la pagina web
wc.web_config()

# Titulo de la aplicacion / pagina web
st.title("Panama Safe - Análisis Geográfico de Delitos")
st.markdown("Panel interactivo sobre homicidios y feminicidios en Panamá")

# Carga de los datos
df = dl.load_data()

# Muestra del dataframe como prueba de la aplicacion
st.write("### Vista previa del conjunto de datos")
st.dataframe(df)

# Visualizaciones
st.markdown("## Visualizaciones")
st.plotly_chart(vz.grafico_tendencia_temporal(df), use_container_width=True)