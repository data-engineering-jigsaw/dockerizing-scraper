# Import necessary libraries
import requests
from src.adapters.indeed_client import get_job_cards
from src.adapters.indeed_adapter import IndeedAdapter
import json

def run():
    cards = get_job_cards()
    position_infos = []
    for card in cards:
        adapter = IndeedAdapter(card)
        position_info = adapter.run()
        position_infos.append(position_info)
    return position_infos

def run_once():
    cards = get_job_cards()
    card = cards[0]
    adapter = IndeedAdapter(card)
    position_info = adapter.run()
    return position_info

def save_to_json():
    positions = run()
    with open("./data/data.json", "a") as f:
        for position in positions:
            json.dump(position.__dict__, f)
            f.write('\n')