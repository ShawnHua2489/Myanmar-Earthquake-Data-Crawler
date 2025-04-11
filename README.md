# Myanmar Earthquake Data Crawler

This project collects and analyzes data related to the recent earthquake in Myanmar and associated humanitarian efforts.

## Features

- Fetches earthquake data from USGS (United States Geological Survey)
- Collects humanitarian updates from ReliefWeb
- Saves data in JSON format for further analysis

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the crawler:
```bash
python myanmar_earthquake_crawler.py
```

The script will:
1. Fetch earthquake data from USGS
2. Collect humanitarian updates from ReliefWeb
3. Save the data in separate JSON files with timestamps

## Data Sources

- USGS Earthquake API
- ReliefWeb Myanmar Updates
- (Additional sources can be added)

## Output

The crawler generates three types of JSON files:
1. `earthquake_info_[timestamp].json`: Contains earthquake details
2. `humanitarian_updates_[timestamp].json`: Contains humanitarian updates
3. `aid_efforts_[timestamp].json`: Contains information about aid efforts

## Contributing

Feel free to contribute by:
- Adding new data sources
- Improving data processing
- Adding visualization capabilities
- Enhancing error handling

## License

MIT License 