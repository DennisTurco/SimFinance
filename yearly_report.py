from user_data import UserData
import random

class YearlyReport():
    data: UserData
    years: int
    yearly_report: list[float]

    def __init__(self, data: UserData):
        self._data = data
        self._years = self._data.retirement_age - self._data.age
        self._yearly_report = []

    def calculate_totals_over_years(self) -> list[float]:
        for _ in range (self._years):
            self._yearly_report.append(self._calculate_total_net_income())
        return self._yearly_report

    def _calculate_total_net_income(self) -> float:
        return (
            self._calculate_total_gross_income()
            - self._calculate_total_expenses()
            + self._calculate_total_net_from_investments()
        )

    def _calculate_total_net_from_investments(self) -> float:
        return (
            self._calculate_total_gross_from_investments()
            - self._calculate_total_expenses_from_investements()
        )
    def _calculate_total_gross_income(self) -> float:
        total_income: float = 0.0
        current_income: float = self._data.monthly_income * 12 # annual income
        for _ in range (self._years): # includes income from current age to retirement
            total_income += current_income
            current_income += (current_income * self._data.income_growth_pct / 100) # compound growth
        return total_income + self._calculate_total_gross_from_investments()

    def _calculate_total_gross_from_investments(self) -> float:
        annual_investment = self._data.monthly_investments * 12
        return self.__future_value_annuity(annual_investment, self._data.expected_returns, self._years)

    def __future_value_annuity(self, annual_contribution: float, rate_pct: float, years: int) -> float:
        rate = rate_pct / 100
        return annual_contribution * ((pow(1 + rate, years) - 1) / rate)

    def _calculate_total_expenses_from_investements(self):
        return self._data.monthly_investments * 12 * self._years

    def _calculate_total_expenses(self) -> float:
        # total_expenses: float = 0
        # return total_expenses
        return 0

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