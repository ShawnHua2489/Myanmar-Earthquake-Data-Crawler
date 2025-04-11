# Myanmar Earthquake Data Analysis

A Python project that collects and visualizes earthquake data from the USGS (United States Geological Survey) API for the Myanmar region.

## Project Overview

This project consists of two main components:
1. **Data Collection**: Fetches earthquake data from the USGS API
2. **Data Visualization**: Creates various visualizations of the collected data

## Features

### Data Collection
- Fetches earthquake data from USGS API
- Filters for earthquakes in Myanmar region
- Collects magnitude, location, time, and coordinates
- Saves data in JSON format

### Visualizations
- Interactive map showing earthquake locations with heatmap
- Bar plot of earthquake magnitudes over time
- Distribution plot of earthquake magnitudes
- Interactive timeline of earthquakes

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Collect earthquake data:
```bash
python myanmar_earthquake_crawler.py
```

2. Generate visualizations:
```bash
python visualize_data.py
```

## Project Structure

```
myanmar-earthquake-analysis/
├── data_files/              # Directory for collected data
├── visualizations_new/      # Directory for new visualizations
├── visualizations_old/      # Directory for archived visualizations
├── myanmar_earthquake_crawler.py  # Data collection script
├── visualize_data.py        # Visualization script
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## Data Source

This project uses the [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/), which provides:
- Real-time earthquake data
- Historical earthquake records
- Detailed earthquake information including:
  - Magnitude
  - Location
  - Time
  - Geographic coordinates

## Dependencies

- requests: For API calls
- pandas: For data manipulation
- matplotlib & seaborn: For static visualizations
- folium: For interactive maps
- plotly: For interactive timelines

## Contributing

Feel free to contribute by:
- Adding new visualization types
- Improving data collection methods
- Enhancing error handling
- Adding data analysis features

## License

MIT License 