import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import json
import time
import os
import shutil

class MyanmarEarthquakeCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.data = {
            'earthquake_info': [],
            'humanitarian_updates': [],
            'aid_efforts': []
        }
        self.data_dir = 'data_files'
        self.setup_directory()

    def setup_directory(self):
        """Create or clean data directory"""
        if os.path.exists(self.data_dir):
            shutil.rmtree(self.data_dir)
        os.makedirs(self.data_dir)

    def get_usgs_data(self):
        """Fetch earthquake data from USGS"""
        try:
            # USGS API endpoint for recent earthquakes in Myanmar region
            url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
            params = {
                'format': 'geojson',
                'starttime': '2025-03-28',  # Start from March 28, 2025
                'endtime': datetime.now().strftime('%Y-%m-%d'),
                'minmagnitude': 4.0,
                'latitude': 21.9162,
                'longitude': 95.9560,
                'maxradiuskm': 1000
            }
            
            response = requests.get(url, params=params, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                for feature in data['features']:
                    earthquake = {
                        'time': datetime.fromtimestamp(feature['properties']['time']/1000).strftime('%Y-%m-%d %H:%M:%S'),
                        'magnitude': feature['properties']['mag'],
                        'location': feature['properties']['place'],
                        'coordinates': feature['geometry']['coordinates'],
                        'url': feature['properties']['url']
                    }
                    self.data['earthquake_info'].append(earthquake)
        except Exception as e:
            print(f"Error fetching USGS data: {str(e)}")

    def get_reliefweb_data(self):
        """Fetch humanitarian updates from ReliefWeb"""
        try:
            url = "https://reliefweb.int/country/mmr"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                updates = soup.find_all('article', class_='rw-river-article')
                
                for update in updates:
                    title = update.find('h3').text.strip()
                    date = update.find('time').text.strip()
                    link = update.find('a')['href']
                    
                    humanitarian_update = {
                        'title': title,
                        'date': date,
                        'link': link
                    }
                    self.data['humanitarian_updates'].append(humanitarian_update)
        except Exception as e:
            print(f"Error fetching ReliefWeb data: {str(e)}")

    def save_data(self):
        """Save collected data to JSON files"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        for category, data in self.data.items():
            filename = f'{category}_{timestamp}.json'
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Saved {len(data)} {category} records to {filepath}")

    def run(self):
        """Run all crawlers"""
        print("Starting data collection...")
        self.get_usgs_data()
        self.get_reliefweb_data()
        self.save_data()
        print("Data collection completed!")

if __name__ == "__main__":
    crawler = MyanmarEarthquakeCrawler()
    crawler.run() 