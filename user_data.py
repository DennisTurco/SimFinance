from dataclasses import dataclass

@dataclass
class UserData:
    # Personal details and context
    age: int  # Current age of the user
    retirement_age: int  # Estimated age of retirement
    housing_status: str  # 'rent', 'mortgage', 'owned' (housing situation)

    # Current financial situation
    liquid_capital: float  # Current liquid capital (savings, investments, etc.)
    monthly_income: float  # monthly revenues
    monthly_expenses: float  # monthly expenses (e.g., bills, groceries)
    variable_expense_pct: float  # % variability in monthly expenses (for unexpected costs)
    income_growth_pct: float  # Annual income growth rate (e.g., salary increases, promotions)

    # Investment risk and returns
    monthly_investments: float  # Monthly amount allocated to investments
    expected_returns: float  # Expected annual return on investments (%)
    returns_std_dev: float  # Standard deviation of returns (risk/volatility)
    investment_risk_profile: str  # 'low', 'medium', 'high' (investment risk level)
    investment_tax_pct: float  # Tax percentage on investment gains

    # Economic factors and unexpected events
    estimated_inflation: float  # Estimated annual inflation rate (%)
    unexpected_event_prob: float  # Probability of unexpected events (e.g., emergency expenses)
    unexpected_event_freq_years: int  # Frequency of unexpected events (in years, e.g., every 5 years)

    def all_data_filled(self, investements: bool) -> bool:
        investements_filled = (
            not investements or (
                self.monthly_investments is not None and
                self.expected_returns is not None and
                self.returns_std_dev is not None and
                self.investment_risk_profile is not None and
                self.investment_tax_pct is not None
            )
        )

        return (
            investements_filled and
            self.age is not None and
            self.retirement_age is not None and
            self.housing_status is not None and
            self.liquid_capital is not None and
            self.monthly_income is not None and
            self.monthly_expenses is not None and
            self.variable_expense_pct is not None and
            self.income_growth_pct is not None and
            self.estimated_inflation is not None and
            self.unexpected_event_prob is not None and
            self.unexpected_event_freq_years is not None
        )


    def calculate_total_net_income(self) -> float:
        return (
            self.__calculate_total_gross_income()
            - self.__calculate_total_expenses()
            + self.__calculate_total_net_from_investments()
        )


    def __calculate_total_gross_income(self) -> float:
        total_income: float = 0.0
        current_income: float = self.monthly_income * 12 # annual income

        for _ in range (self.age, self.retirement_age): # includes income from current age to retirement
            total_income += current_income
            current_income += (current_income * self.income_growth_pct / 100) # compound growth

        return total_income + self.__calculate_total_gross_from_investments()

    def __calculate_total_net_from_investments(self) -> float:
        return (
            self.__calculate_total_gross_from_investments()
            - self.__calculate_total_expenses_from_investements()
        )

    def __calculate_total_gross_from_investments(self) -> float:
        years = self.retirement_age - self.age
        annual_investment = self.monthly_investments * 12
        return self.__future_value_annuity(annual_investment, self.expected_returns, years)


    def __calculate_total_expenses_from_investements(self):
        years = self.retirement_age - self.age
        return self.monthly_investments * 12 * years


    def __future_value(self, present_value: float, growth_percentage: float, ages: int) -> float:
        return present_value * pow((1 + growth_percentage/100), ages)


    def __future_value_annuity(self, annual_contribution: float, rate_pct: float, years: int) -> float:
        rate = rate_pct / 100
        return annual_contribution * ((pow(1 + rate, years) - 1) / rate)


    def __calculate_total_expenses(self) -> float:
        # total_expenses: float =
        # return total_expenses
        return 0