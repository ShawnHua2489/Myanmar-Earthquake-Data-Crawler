import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import plotly.express as px
from datetime import datetime
import os
import shutil

class EarthquakeDataVisualizer:
    def __init__(self):
        self.earthquake_data = None
        self.visualization_dirs = {
            'old': 'visualizations_old',
            'new': 'visualizations_new'
        }
        self.setup_directories()
        self.load_data()

    def setup_directories(self):
        """Create or clean visualization directories"""
        for dir_name in self.visualization_dirs.values():
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
            os.makedirs(dir_name)

    def load_data(self):
        """Load the most recent JSON files from data_files directory"""
        data_dir = 'data_files'
        if not os.path.exists(data_dir):
            print(f"Error: {data_dir} directory not found")
            return

        files = os.listdir(data_dir)
        earthquake_files = [f for f in files if f.startswith('earthquake_info_')]

        if earthquake_files:
            latest_file = max(earthquake_files)
            filepath = os.path.join(data_dir, latest_file)
            with open(filepath, 'r') as f:
                self.earthquake_data = json.load(f)
                print(f"Loaded {len(self.earthquake_data)} earthquake records from {latest_file}")
        else:
            print("No earthquake data files found")

    def save_visualization(self, filename, dir_type='new'):
        """Save visualization to appropriate directory"""
        target_dir = self.visualization_dirs[dir_type]
        if filename.endswith('.png'):
            plt.savefig(os.path.join(target_dir, filename))
            plt.close()
        elif filename.endswith('.html'):
            # For HTML files (folium and plotly)
            if 'map' in filename:
                # For folium map
                self.current_map.save(os.path.join(target_dir, filename))
            else:
                # For plotly
                self.current_fig.write_html(os.path.join(target_dir, filename))

    def plot_earthquake_magnitudes(self):
        """Create a bar plot of earthquake magnitudes"""
        if not self.earthquake_data:
            return

        df = pd.DataFrame(self.earthquake_data)
        plt.figure(figsize=(12, 6))
        sns.barplot(x='time', y='magnitude', data=df)
        plt.title('Earthquake Magnitudes Over Time (March 28, 2025 onwards)')
        plt.xlabel('Time')
        plt.ylabel('Magnitude')
        plt.xticks(rotation=45)
        plt.tight_layout()
        self.save_visualization('earthquake_magnitudes.png')

    def create_earthquake_map(self):
        """Create an interactive map of earthquake locations"""
        if not self.earthquake_data:
            return

        # Create a map centered on Myanmar
        self.current_map = folium.Map(location=[21.9162, 95.9560], zoom_start=6)

        # Add earthquake markers
        for quake in self.earthquake_data:
            folium.CircleMarker(
                location=[quake['coordinates'][1], quake['coordinates'][0]],
                radius=quake['magnitude'] * 2,
                popup=f"Magnitude: {quake['magnitude']}<br>Time: {quake['time']}",
                color='red',
                fill=True,
                fill_color='red'
            ).add_to(self.current_map)

        # Add heatmap
        heat_data = [[quake['coordinates'][1], quake['coordinates'][0], quake['magnitude']] 
                    for quake in self.earthquake_data]
        HeatMap(heat_data).add_to(self.current_map)

        self.save_visualization('earthquake_map.html')

    def plot_magnitude_distribution(self):
        """Create a distribution plot of earthquake magnitudes"""
        if not self.earthquake_data:
            return

        df = pd.DataFrame(self.earthquake_data)
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='magnitude', bins=10)
        plt.title('Distribution of Earthquake Magnitudes (March 28, 2025 onwards)')
        plt.xlabel('Magnitude')
        plt.ylabel('Count')
        plt.tight_layout()
        self.save_visualization('magnitude_distribution.png')

    def create_interactive_timeline(self):
        """Create an interactive timeline using Plotly"""
        if not self.earthquake_data:
            return

        df = pd.DataFrame(self.earthquake_data)
        df['time'] = pd.to_datetime(df['time'])
        
        self.current_fig = px.scatter(df, x='time', y='magnitude',
                                    size='magnitude',
                                    hover_data=['location'],
                                    title='Interactive Earthquake Timeline (March 28, 2025 onwards)')
        
        self.save_visualization('interactive_timeline.html')

    def run_all_visualizations(self):
        """Run all visualization methods"""
        print("Creating visualizations...")
        self.plot_earthquake_magnitudes()
        self.create_earthquake_map()
        self.plot_magnitude_distribution()
        self.create_interactive_timeline()
        print(f"Visualizations completed! Check the {self.visualization_dirs['new']} directory for new visualizations.")

if __name__ == "__main__":
    visualizer = EarthquakeDataVisualizer()
    visualizer.run_all_visualizations() 