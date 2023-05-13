from bs4 import BeautifulSoup as bs
from src.adapters.indeed_client import *
import pdb

def test_all_cards_are_td():
    tds = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
    list(set([td.name == 'td' for td in tds])) == 'td'

