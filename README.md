# Description

Normally, data transfer between programs is accomplished using data structures suited for automated processing by computers, not people. Such interchange formats and protocols are typically rigidly structured, well-documented, easily parsed, and minimize ambiguity. Very often, these transmissions are not human-readable at all.

Thus, the key element that distinguishes data scraping from regular parsing is that the output being scraped is intended for display to an end-user, rather than as an input to another program. It is therefore usually neither documented nor structured for convenient parsing. Data scraping often involves ignoring binary data (usually images or multimedia data), display formatting, redundant labels, superfluous commentary, and other information which is either irrelevant or hinders automated processing.

# Task

Using python libraries requests and beautifulsoup4, return a CSV of the TOP 25 trending repositories from Github.

Request (with request)
Extract (with beautifulsoup4)
Transform
Format

Part 0: Request Write a function prototyped: def request_github_trending(url) it will return the result of Request.

Part 1: Extract Write a function prototyped: def extract(page) to find_all instances of HTML code of repository rows and return it. You should use BeautifulSoup. :-)

Part 2: Transform Write a function prototyped: def transform(html_repos) taking an array of all the instances of HTML code of the repository row. It will return an array of hash following this format: [{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]

Part 3: Format Write a function prototyped: def format(repositories_data) taking a repository array of hash and transforming it and returning it into a CSV string. Each column will be separated by , and each line by \n The columns will be Developer,Repository Name,Number of Stars

Tip Google: Request get python Google: BeautifulSoup python

# Installation

open terminal and run this command

py my_first_scraper.py

# Usage

$py my_first_scraper.py