import streamlit as st
import messages as m
import form as f
from plotter import Plotter
from finalcial_calculator import FinancialCalculator
from yearly_report import YearlyReport

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
        report = FinancialCalculator(user_data)
        yearly_report: list[YearlyReport] = report.calculate_totals_over_years()
        generations.append(yearly_report[i].get_net_income())

    if generations:
        Plotter.generate_random_walk_chart(generations)


st.divider()
