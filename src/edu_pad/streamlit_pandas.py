import streamlit as st
import pandas as pd
# from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import os




def main():

    df = pd.read_csv("src/edu_piv/static/data/data_extractor.csv")
    columnas = ["abrir","max","min","cerrar","cierre_ajustado","volumen","indicador"]
    df_2 = df[columnas]
    profile = ProfileReport(df_2, title="Dashboard Indicador Dolar")
    st.title("Análisis de Datos")
    #st.write(profile.to_html(),unsafe_allow
    st.components.v1.html(profile.to_html(), height=600, scrolling=True)





    # df = pd.read_csv("src/edu_pad/static/csv/data_extractor.csv")
    # pr = df.profile_report()
    # st_profile_report(pr)


if __name__ == "__main__":
    # st.set_page_config(page_title="Dashborad Fianciero", page_icon="🎈", layout="wide")
    main()