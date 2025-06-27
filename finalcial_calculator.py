from user_data import UserData
import random

from yearly_report import YearlyReport

class FinancialCalculator():
    data: UserData
    years: int
    yearly_report: list[float]

    def __init__(self, data: UserData):
        self._data = data
        self._years = self._data.retirement_age - self._data.age
        self.report = []

    def calculate_totals_over_years(self) -> list[YearlyReport]:
        investment_history = self._simulate_investment_growth()

        for year in range(self._years):
            inflation_factor = self._get_inflation_multiplier(year)
            growth_factor = self._get_income_multiplier(year)

            base_income = self._calculate_total_gross_income() * growth_factor
            base_expenses = self._calculate_month_expenses() * 12 * inflation_factor
            unexpected_expenses = self._calculate_expenses_for_unexpected_events() * inflation_factor

            if self._data.investements:
                investment_balance, total_contributions = investment_history[year]
                investment_gains = investment_balance - total_contributions
            else:
                investment_balance = 0
                investment_gains = 0

            self.report.append(YearlyReport(
                base_income,
                base_expenses,
                unexpected_expenses,
                investment_gains
            ))

        return self.report

    def _simulate_investment_growth(self) -> list[float]:
        investment_balance = 0.0
        history = []
        total_contributions = 0.0

        if not self._data.investements:
            return [0.0] * self._years

        for _ in range(self._years):
            annual_contribution = self._data.monthly_investments * 12
            total_contributions += annual_contribution
            investment_balance += annual_contribution

            simulated_return = random.normalvariate(
                self._data.expected_returns,
                self._data.returns_std_dev
            ) / 100

            gross_gain = investment_balance * simulated_return

            if gross_gain > 0:
                taxed_gain = gross_gain * (1 - self._data.investment_tax_pct / 100)
            else:
                taxed_gain = gross_gain

            investment_balance += taxed_gain
            history.append((investment_balance, total_contributions))

        return history



    def _calculate_total_net_from_investments(self) -> float:
        return (
            self._calculate_total_gross_from_investments()
            - self._calculate_total_expenses_from_investements()
        )
    def _calculate_total_gross_income(self) -> float:
        current_income: float = self._data.monthly_income * 12 # annual income
        return current_income
        # for _ in range (self._years): # includes income from current age to retirement
        #     total_income += current_income
        #     current_income += (current_income * self._data.income_growth_pct / 100) # compound growth
        # return total_income + self._calculate_total_gross_from_investments()

    def _calculate_total_gross_from_investments(self) -> float:
        annual_investment = self._data.monthly_investments * 12
        return self.__future_value_annuity(annual_investment, self._data.expected_returns, self._years)

    def __future_value_annuity(self, annual_contribution: float, rate_pct: float, years: int) -> float:
        rate = rate_pct / 100
        if rate == 0:
            return annual_contribution * years
        return annual_contribution * ((pow(1 + rate, years) - 1) / rate)

    def _calculate_total_expenses_from_investements(self):
        return self._data.monthly_investments * 12 * self._years

    def _calculate_month_expenses(self) -> float:
        expenses = self._data.monthly_expenses
        variabiliy = expenses * self._data.variable_expense_pct / 100
        return random.uniform(expenses - variabiliy, expenses + variabiliy)

    def _calculate_expenses_for_unexpected_events(self) -> float:
        total_expenses: float = 0.0
        event_count: int = 0

        # Calculate the number of unexpected events
        for _ in range(self._data.unexpected_event_freq_years):
            if random.random() < (self._data.unexpected_event_prob / 100):
                event_count += 1

        # Estimate expense for each unexpected event
        for _ in range(event_count):
            # Assume each event costs between half to full monthly expenses
            expense = random.uniform(self._data.monthly_expenses / 2, self._data.monthly_expenses)
            total_expenses += expense

        return total_expenses

    def _get_inflation_multiplier(self, year: int) -> float:
        inflation_rate = self._data.estimated_inflation / 100
        return pow(1 + inflation_rate, year)

    def _get_income_multiplier(self, year: int) -> float:
        growth_rate = self._data.income_growth_pct / 100
        return pow(1 + growth_rate, year)
