from dataclasses import dataclass

@dataclass
class UserData:
    # Plotting settings
    n_generations: int # the number of generations for the plot

    # Personal details and context
    age: int  # Current age of the user
    retirement_age: int  # Estimated age of retirement
    #housing_status: str  # 'rent', 'mortgage', 'owned', 'none' (housing situation)

    # Current financial situation
    liquid_capital: float  # Current liquid capital (savings, investments, etc.)
    monthly_income: float  # monthly revenues
    monthly_expenses: float  # monthly expenses (e.g., bills, groceries)
    variable_expense_pct: float  # % variability in monthly expenses (for unexpected costs)
    income_growth_pct: float  # Annual income growth rate (e.g., salary increases, promotions)

    # Investment risk and returns
    investements: bool
    monthly_investments: float  # Monthly amount allocated to investments
    expected_returns: float  # Expected annual return on investments (%)
    returns_std_dev: float  # Standard deviation of returns (risk/volatility)
    investment_tax_pct: float  # Tax percentage on investment gains

    # Economic factors and unexpected events
    estimated_inflation: float  # Estimated annual inflation rate (%)
    unexpected_event_prob: float  # Probability of unexpected events (e.g., emergency expenses)
    unexpected_event_freq_years: int  # Frequency of unexpected events (in years, e.g., every 5 years)

    def all_data_filled(self, investements: bool) -> bool:
        self.investments = investements

        investements_filled = (
            not investements or (
                self.monthly_investments is not None and
                self.expected_returns is not None and
                self.returns_std_dev is not None and
                self.investment_tax_pct is not None
            )
        )

        return (
            investements_filled and
            self.n_generations is not None and
            self.age is not None and
            self.retirement_age is not None and
            self.liquid_capital is not None and
            self.monthly_income is not None and
            self.monthly_expenses is not None and
            self.variable_expense_pct is not None and
            self.income_growth_pct is not None and
            self.estimated_inflation is not None and
            self.unexpected_event_prob is not None and
            self.unexpected_event_freq_years is not None
        )