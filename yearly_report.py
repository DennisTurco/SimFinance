class YearlyReport():
    gross_income: float
    base_expenses: float
    unexpected_expenses: float
    investment_balance: float

    def __init__(self, gross_income: float, base_expenses: float, unexpected_expenses: float, investment_balance: float) -> None:
        self.gross_income = gross_income
        self.base_expenses = base_expenses
        self.unexpected_expenses = unexpected_expenses
        self.investment_balance = investment_balance

    def get_net_income(self) -> float:
        return self.gross_income + self.investment_balance - self.base_expenses - self.unexpected_expenses