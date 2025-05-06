import streamlit as st
import messages as m
import form as f

m.main_title()
m.main_description()

st.divider()

user_data = f.user_data_form()

if user_data != None:
    net_income=user_data.calculate_total_net_income()


st.divider()
