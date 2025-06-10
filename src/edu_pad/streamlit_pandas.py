import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import os


def main():

    df = pd.read_csv("src/edu_piv/static/csv/data_extractor.csv")
    columnas = ["abrir","max","min","cerrar","cierre_ajustado","volumen","indicador"]
    df_2 = df[columnas]
    profile = ProfileReport(df_2, title="Dashboard Indicador Dolar")
    st.title("Análisis de Datos")
    st.components.v1.html(profile.to_html(), height=600, scrolling=True)




if __name__ == "__main__":
    main()