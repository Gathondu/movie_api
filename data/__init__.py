import json
import os

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
movies = json.load(open(os.path.join(DIR,'data/MOCK_DATA.json')))