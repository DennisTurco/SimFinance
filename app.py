import streamlit as st
import messages as m
import form as f
from plotter import Plotter

icon_img = "imgs/logo.png"
banner_img = "imgs/banner.png"
st.logo(banner_img, icon_image=icon_img)

st.sidebar.markdown("Sidebar description")

m.main_title()
m.main_description()

n_generations = 10
generations = []

st.divider()

user_data = f.user_data_form()

if user_data != None:
    for i in range(n_generations):
        income_report: list[int] = user_data.calculate_totals_over_years()
        generations.append(income_report)

    if generations:
        Plotter.generate_random_walk_chart(generations)


st.divider()
