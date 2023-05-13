import click
from src.adapters.indeed_client import get_job_cards
from index import save_to_json
import pdb

@click.group()
def scraper():
    pass

# Command Group
@click.group(name='tools')
def cli_tools():
    """Tool related commands"""
    pass

@cli_tools.command(name='scrape_jobs', help='help scrape_jobs')
def scrape_jobs(start = 0, position = 'data engineer'):
    cards = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
    print(cards)

@cli_tools.command(name='save_as_json', help='save_to_json')
def save_as_json():
    save_to_json()


if __name__ == '__main__':
    cli_tools()