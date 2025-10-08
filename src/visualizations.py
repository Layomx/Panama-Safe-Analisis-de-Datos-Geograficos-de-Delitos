# Archivo especifico para las visualizaciones del proyecto
import pandas as pd 
import plotly.express as px

# Agregare algunas de prueba (Elvis Adames)
def grafico_tendencia_temporal(df):
    """Genera un gráfico de tendencia temporal de los delitos."""
    
    # columna periodo (año-mes)
    df['periodo'] = df['año'].astype(str) + '-' + df['mes'].astype(str).str.zfill(2)
    
    # Agrupacion por periodo y sexo
    df_temp = df.groupby(['periodo', 'sexo', 'año', 'mes']).size().reset_index(name='cantidad')
    
    # Ordenamiento por año y mes
    df_temp = df_temp.sort_values(['año', 'mes'])
    
    # Mapeo de colores
    color_discrete_map = {
        'Masculino': 'blue',
        'Femenino': 'red',
        'No disponible': 'green'
    }
    
    fig = px.line(
        df_temp,
        x='periodo',
        y='cantidad',
        color='sexo',
        title='Tendencia Temporal de Delitos por Sexo',
        labels= {'periodo': 'Periodo (Año-Mes)', 'cantidad': 'Número de Delitos', 'sexo': 'Sexo'},
        color_discrete_map= color_discrete_map
    )
    
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
        xaxis=dict(tickangle=45)
    )
    
    return fig