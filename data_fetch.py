import requests
import os
import json
from datetime import datetime

# Directory to save data
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Function to fetch data
def fetch_data():
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
    response = requests.get(url)
    data = response.json()
    print(data)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(data_dir, f'IBM_{timestamp}.json')
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    fetch_data()
