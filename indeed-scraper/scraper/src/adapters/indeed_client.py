import re
from bs4 import BeautifulSoup as bs
import requests
import pdb
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


def get_indeed_html(position = 'data engineer', location = 'United States', start = 0):
  with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.new_page()
    stealth_sync(page)
    url = 'https://www.indeed.com/jobs?q=data+engineer&l=New+York%2C+NY&vjk=de0e64293cefea2f'
    page.goto(url)
    content = page.content()
    browser.close()
  return content

    
def get_job_cards(position = 'data engineer', location = 'United States', start = 0):
  html_string = get_indeed_html(position = position, location = location, start = start)
  soup = bs(html_string, 'html.parser')
  tds = soup.find_all('td', {'class': 'resultContent'})
  return tds

  