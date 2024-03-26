# Web Scraping Project: LEC Standings Scraper

This project is a web scraping tool built with Python to extract and store League of Legends European Championship (LEC) standings data from the LoL Esports website.

## Description

The script automates the process of fetching data from the LEC standings webpage and storing it in a CSV file. It utilizes the BeautifulSoup and Selenium libraries to parse HTML content and interact with the webpage.

## Features

- Retrieves team standings including name, placement, wins, and losses.
- Appends data to a CSV file with timestamped entries.

## Requirements

- Python 3.x
- BeautifulSoup
- Selenium
- Chrome WebDriver (for Selenium)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/lec-standings-scraper.git
   cd lec-standings-scraper
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Download the Chrome WebDriver and place it in your PATH.

## Usage
1. Run the script:
   ```bash
   python scrape.py

2. The script will launch a Chrome browser, fetch the data from the LEC standings webpage, and store it in a CSV file named data.csv.
## Sample Output
 ```csv
name,placement,wins,losses,time
MAD Lions,1,16,2,26-03-2024
G2 Esports,2,15,3,26-03-2024
Fnatic,3,12,6,26-03-2024
...
 ```

## Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this template according to your project's specific details and requirements.