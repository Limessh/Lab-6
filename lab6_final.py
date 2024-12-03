class Officer:
    def __init__(self, hours_work, rate, bonus):
        self.hours_work = hours_work
        self.rate = rate
        self.bonus = bonus

    def calculate_bonus(self):
        return self.hours_work * self.rate * self.bonus

    def salary_to_hours_ratios(self):
        return self.total_salary() / self.hours_work if self.hours_work != 0 else 0

    def total_salary(self):
        return (self.hours_work * self.rate) + self.calculate_bonus()

    def __add__(self, other):
        if isinstance(other, Officer):
            return Officer(0, 0, 0)
        return None


class SeniorOfficer(Officer):
    def __init__(self, hours_work, rate, bonus, project):
        super().__init__(hours_work, rate, bonus)
        self.project = project

    def calculate_bonus(self):
        return super().calculate_bonus() + (self.project * 100)


class Director(Officer):
    def __init__(self, hours_work, rate, bonus, project):
        super().__init__(hours_work, rate, bonus)
        self.project = project

    def calculate_bonus(self):
        return super().calculate_bonus() + (self.project * 50)

#Пример
officer = Officer(160, 20, 0.1)
senior_officer = SeniorOfficer(180, 25, 0.15, 5)
director = Director(200, 30, 0.2, 10)

print(f"Зарплата сотрудника: {officer.total_salary()}")
print(f"Зарплата старшего сотрудника: {senior_officer.total_salary()}")
print(f"Зарплата директора: {director.total_salary()}")

print(
    f"Соотношение зарплаты к рабочим часам для сотрудника: {officer.salary_to_hours_ratios()}"
)
print(
    f"Соотношение зарплаты к рабочим часам для старшего сотрудника: {senior_officer.salary_to_hours_ratios()}"
)
print(
    f"Соотношение зарплаты к рабочим часам для директора: {director.salary_to_hours_ratios()}"
)
