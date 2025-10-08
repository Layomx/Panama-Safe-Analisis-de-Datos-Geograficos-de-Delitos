import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/dataset_unificado.csv')

# Titulo de la aplicacion / pagina web
st.title("Panama Safe - Análisis Geográfico de Delitos")
st.markdown("Panel interactivo sobre homicidios y feminicidios en Panamá")

# Muestra del dataframe como prueba de la aplicacion
st.write("### Vista previa del conjunto de datos")
st.dataframe(df)