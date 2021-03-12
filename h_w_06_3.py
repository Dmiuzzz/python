class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        salary = self._income.get("wage") + self._income.get("bonus")
        print(f"Зарплата - {salary}$")


r_income = {"wage": 150000, "bonus": 50000}
real_position = Position('Ivan', 'Ivanov', 'developer', r_income)

real_position.get_full_name()
real_position.get_total_income()

