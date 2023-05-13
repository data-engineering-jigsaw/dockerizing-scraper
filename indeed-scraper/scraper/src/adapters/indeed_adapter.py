from src.adapters.indeed_client import *
from src.models.position import Position
import requests
import re
import pdb

class IndeedAdapter:
    def __init__(self, card):
        self.card = card
        
    def get_id(self):
        return self.card.find('a')['data-jk']
    
    def get_title(self):
        return self.card.find('h2').text

    def get_salary_text(self):
        
        salary = self.card.find('div', {'class': 'salaryOnly'})
        # salary = self.card.find('span', {'class': 'salary-snippet-container'})
        return salary.text

    def get_company_name(self):
        company = self.card.find('span', {'class': 'companyName'})
        return company.text
        
    def get_city_state(self):
        city_state = self.card.find('div', {'class': 'companyLocation'}).text
        split_text = city_state.split(', ')
        city = split_text[0]
        state = split_text[1].split()[0]
        return (city, state)

    def clean_salaries(self, salary_text):
        split_salaries = salary_text.split(' - ')
        if len(split_salaries) == 2:
            first_salary_text, second_salary = split_salaries
            second_salary_text = second_salary.split()[0]
            
            cleaned_first = self.clean_salary(first_salary_text)
            cleaned_second = self.clean_salary(second_salary_text)
            return [cleaned_first, cleaned_second]
        else:
            salary = split_salaries[0]
            return [self.clean_salary(salary.split()[0])]

        
    
    def clean_salary(self, salary_text):
        num_str = salary_text.replace('$', '').replace(',', '').replace('Estimated ', '')
        if not num_str: return None
        if num_str[-1] == 'K':
            return float(num_str[:-1]) * 1000
        try:
            return float(num_str[:-1]) * 1000 if num_str.endswith('K') else float(num_str)
        except ValueError:
            return None

    def run(self):
        id = self.get_id()
        title = self.get_title()
        salary_text = self.get_salary_text()
        clean_salaries = self.clean_salaries(salary_text)
        company_name = self.get_company_name()
        city, state = self.get_city_state()
        return Position(id, title, clean_salaries, company_name, city, state)

# change format of salaries to remove nesting
# change to minimum salary and maximum salary
# {'id': 'b6011e15bf167def', 'title': 'Data Engineer', 'salaries': [85000.0, 100000.0], 'city': 'Aretove Technologies', 'state': 'New York', 'company_name': 'NY'}
    