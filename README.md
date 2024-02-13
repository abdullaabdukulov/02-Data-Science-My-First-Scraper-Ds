# 02-Data Science-My First Scraper

## Task

The task for this project is to create a web scraper that retrieves information about the top trending repositories on GitHub and formats the data for display.

## Description

This Python script uses the BeautifulSoup library to scrape the GitHub trending page, extract relevant information from the HTML, and present the top 25 trending repositories. The extracted data includes the developer's name, repository name, and the number of stars.

## Installation

To run the scraper, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/02-Data-Science-My-First-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 02-Data-Science-My-First-Scraper
   ```

3. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

Execute the main script to retrieve and display the top trending repositories:

```bash
python my_first_scraper.py
```

The script will output the formatted data to the console.
