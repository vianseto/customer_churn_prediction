import visualization, predict_frontend, predict_backend
import streamlit as st

st.set_page_config(
    page_title="Aditya Vianseto FDTS Batch 11")

st.sidebar.write('# Menu Utama')
halaman = st.sidebar.selectbox(options=['Data Visualization','Predict App'],\
    label='Pilih Halaman :')
 
if halaman == 'Data Visualization':
    visualization.app()
else:
    predict_frontend.app()