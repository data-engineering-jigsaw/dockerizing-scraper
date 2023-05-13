class Position:
    def __init__(self, id, title, salaries, city, state, company_name):
        self.id = id
        self.title = title
        self.set_salaries(salaries)
        self.city = city
        self.state = state
        self.company_name = company_name

    def set_salaries(self, salaries):
        if len(salaries) == 2:
            self.min_salary = salaries[0]
            self.max_salary = salaries[1]
        elif len(salaries) == 1:
            self.min_salary = salaries[0]
            self.max_salary = salaries[0]
