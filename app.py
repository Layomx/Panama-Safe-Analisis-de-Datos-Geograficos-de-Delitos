import streamlit as st
import pandas as pd
import plotly.express as px
import src.web_config as wc
import src.data_loader as dl
import src.visualizations as vz
import src.utils as ut

# Configuracion de la pagina web
wc.web_config()

# Titulo de la aplicacion / pagina web
st.title("Panama Safe - Análisis Geográfico de Delitos")
st.markdown("### Panel interactivo sobre homicidios y feminicidios en Panamá")
st.markdown("---")

# Carga de los datos
df = dl.load_data()

# Barra lateral con filtros
st.sidebar.header("Filtros de Análisis")
st.sidebar.markdown("Selecciona los criterios para filtrar los datos:")

# Filtro de Año
años_disponibles = sorted(df['año'].dropna().unique())
años_seleccionadas = st.sidebar.multiselect(
    "Año(s)",
    options = años_disponibles,
    default = años_disponibles
)

# Filtro de Provincia
provincias_disponibles = sorted(df['provincia'].astype(str).unique())
provincias_seleccionadas = st.sidebar.multiselect(
    "Provincia(s)",
    options = provincias_disponibles, 
    default= provincias_disponibles
)

# Filtro de Rango de Edad
edades_disponibles = sorted(df['rango_de_edad'].unique())
edades_seleccionadas = st.sidebar.multiselect(
    "Edad(es)",
    options = edades_disponibles,
    default = edades_disponibles
)

# Filtro de Tip de Arma
armas_disponibles = sorted(df['tipo_de_arma_utilizada'].unique())
armas_seleccionadas = st.sidebar.multiselect(
    "Tipo(s) de Arma",
    options = armas_disponibles,
    default = armas_disponibles
)

st.sidebar.markdown("---")
st.sidebar.info("**Tip**: Los gráficos se actualizan automáticamente al cambiar los filtros.")

# Aplicar filtros al DataFrame (CON MANEJO DE FILTROS VACÍOS)
df_filtrado = df.copy()

# Filtrar por año (si se seleccionó algún año)
if años_seleccionadas:
    df_filtrado = df_filtrado[df_filtrado['año'].isin(años_seleccionadas)]

# Filtrar por provincia (si se seleccionó alguna provincia)
if provincias_seleccionadas:
    df_filtrado = df_filtrado[df_filtrado['provincia'].astype(str).isin(provincias_seleccionadas)]

# Filtrar por edad (si se seleccionó algún rango de edad)
if edades_seleccionadas:
    df_filtrado = df_filtrado[df_filtrado['rango_de_edad'].isin(edades_seleccionadas)]

# Filtrar por arma (si se seleccionó algún tipo de arma)
if armas_seleccionadas:
    df_filtrado = df_filtrado[df_filtrado['tipo_de_arma_utilizada'].isin(armas_seleccionadas)]

# Verificacion de datos despues de aplicar filtros
if df_filtrado.empty:
    st.warning("No hay datos disponibles para los filtros seleccionados. Por favor, ajusta los filtros.")
    # Mostrar datos sin filtrar como fallback
    df_filtrado = df

# Muestra del dataframe como prueba de la aplicacion
st.write("### Vista previa del conjunto de datos")
st.dataframe(df_filtrado)
st.markdown("---")

# Visualizaciones
st.markdown("## Visualizaciones")
st.plotly_chart(vz.grafico_tendencia_temporal(df_filtrado), use_container_width=True)

