import streamlit as st
import user_data as ud

def user_data_form() -> ud.UserData | None:
    if "toggle" not in st.session_state:
        st.session_state.toggle = False

    st.session_state.toggle = st.toggle("Investments", value=st.session_state.toggle)

    with st.form(key="user_data_form"):
        st.header("Insert Your Data")

        st.subheader("Personal details and context")
        age = st.number_input("Age", min_value=0, max_value=100, value=30)
        retirement_age = int(st.number_input("Retirement Age", min_value=age, max_value=100, value=67))
        #housing_status = st.selectbox("Housing Status", ["Rent", "Mortgage", "Owned", "None"])

        st.subheader("Current financial situation")
        liquid_capital = st.number_input("Current Liquid Capital (€)", min_value=0.0, value=10000.0)
        monthly_income = st.number_input("Average Monthly Net Income (€)", min_value=0.0, value=1600.0)
        monthly_expenses = st.number_input("Average Monthly Expenses (€)", min_value=0.0, value=1000.0)
        variable_expense_pct = st.slider("Variable Expense Portion (%)", min_value=0.0, max_value=50.0, value=10.0, help="Estimate the portion of your monthly expenses that changes (e.g. leisure, travel)")
        income_growth_pct = st.slider("Annual Net Income Growth Rate (%)", 0.0, 15.0, 0.5)

        st.subheader("Investment risk and returns")
        if st.session_state.toggle:
            monthly_investments = st.number_input("Monthly Investments (€)", min_value=0.0, value=500.0)
            expected_returns = st.slider("Expected Annual Return (%)", 0.0, 15.0, 5.0)
            returns_std_dev = st.slider("Return Volatility (Standard Deviation, %)", 0.0, 30.0, 12.0, help="Annual standard deviation of returns. Higher values indicate greater risk and larger potential fluctuations in investment value. Typical values: Low ~5%, Medium ~12%, High ~20%+.")
            investment_tax_pct = st.slider("Tax on Investment Gains (%)", 0.0, 50.0, 5.0, help="Typical tax rates: Low risk ~5%, Medium risk ~15%, High risk ~26%")
        else:
            monthly_investments = 0
            expected_returns = 0
            returns_std_dev = 0
            investment_tax_pct = 0

        st.subheader("Economic factors and unexpected events")
        estimated_inflation = st.slider("Estimated Annual Inflation (%)", 0.0, 10.0, 2.0)
        unexpected_event_prob = st.slider("Probability of Unexpected Events (%)", 0.0, 100.0, 30.0)
        unexpected_event_freq_years = st.slider("Frequency of Unexpected Events (Years)", 1, 20, 5)

        st.subheader("Charts Settings")
        n_generations = st.slider("Number of simulations", 1, 100, 30)

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            user_data = ud.UserData(
                n_generations=n_generations,
                age=age,
                retirement_age=retirement_age,
                liquid_capital=liquid_capital,
                monthly_income=monthly_income,
                monthly_expenses=monthly_expenses,
                variable_expense_pct=variable_expense_pct,
                income_growth_pct=income_growth_pct,
                investements=st.session_state.toggle,
                monthly_investments=monthly_investments,
                expected_returns=expected_returns,
                returns_std_dev=returns_std_dev,
                investment_tax_pct=investment_tax_pct,
                estimated_inflation=estimated_inflation,
                unexpected_event_prob=unexpected_event_prob,
                unexpected_event_freq_years=unexpected_event_freq_years
            )

            if not user_data.all_data_filled(investements=st.session_state.toggle):
                st.warning("Please fill in all of the fields")
                return None
            else:
                st.success("All data correctly filled!")
                return user_data