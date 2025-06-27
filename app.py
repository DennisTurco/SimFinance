import streamlit as st
import streamlit.components.v1 as components
from google_analitycs import GoogleAnalytics
import messages as m
import form as f
from plotter import Plotter
from finalcial_calculator import FinancialCalculator
from user_data import UserData
from yearly_report import YearlyReport

components.html(GoogleAnalytics.ga_code, height=0)

icon_img = "imgs/logo.png"
banner_img = "imgs/banner.png"
st.logo(banner_img, icon_image=icon_img)

st.sidebar.markdown("Sidebar description")

m.main_title()
m.main_description()

generations = []

st.divider()

user_data: UserData = f.user_data_form()

if user_data is not None:
    for _ in range(user_data.n_generations):
        report = FinancialCalculator(user_data)
        yearly_report: list[YearlyReport] = report.calculate_totals_over_years()

        cumulative_series = [user_data.liquid_capital]
        cumulative = user_data.liquid_capital
        for y in yearly_report:
            cumulative += y.get_net_income()
            cumulative_series.append(cumulative)

        generations.append(cumulative_series)

    if generations:
        Plotter.generate_random_walk_chart(generations)


st.divider()
