import streamlit as st

def web_config():
    # Configuración basica de la pagina
    st.set_page_config(
        page_title="Panama Safe - Análisis de Delitos",
        page_icon="🇵🇦"
    )

    # CSS personalizado en busca de un estilo gubernamental
    st.markdown("""
    <style>
        /* Header gubernamental */
        .main-header {
            background: linear-gradient(90deg, #005293 0%, #003d6b 100%);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .main-header h1 {
            color: white;
            text-align: center;
            margin: 0;
            font-size: 2.2em;
            font-weight: 600;
        }
        
        .main-header p {
            color: #E8EDF3;
            text-align: center;
            margin: 5px 0 0 0;
            font-size: 1.1em;
        }
        
        /* Estilo para métricas */
        [data-testid="stMetricValue"] {
            font-size: 1.8em;
            color: #005293;
            font-weight: 600;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #F0F4F8;
        }
        
        /* Botones */
        .stButton>button {
            background-color: #005293;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: 500;
        }
        
        .stButton>button:hover {
            background-color: #003d6b;
            border: none;
        }
        
        /* Headers de secciones */
        h2 {
            color: #005293;
            border-bottom: 3px solid #C8102E;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        
        /* Footer gubernamental */
        .gov-footer {
            background-color: #F0F4F8;
            padding: 20px;
            border-radius: 10px;
            margin-top: 40px;
            text-align: center;
            border-top: 3px solid #005293;
        }
    </style>
    """, unsafe_allow_html=True)