class YearlyReport():
    gross_income: float
    base_expenses: float
    unexpected_expenses: float
    # investement_deposit: float
    # investement_income: float

    def __init__(self, gross_income: float, base_expenses: float, unexpected_expenses: float) -> None:
        self.gross_income = gross_income
        self.base_expenses = base_expenses
        self.unexpected_expenses = unexpected_expenses

    def get_net_income(self) -> float:
        return self.gross_income - self.base_expenses - self.unexpected_expenses