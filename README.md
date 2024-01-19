# Description

HTML has been built to be "displayed". It's working very well... but when you want to build a script to collect actionable data, you are left with this:

Google search page engine HTML Euuh... I just wanted to collect all the links on the page...

It’s likely that there are libraries to navigate through the jungle. Let's scrap some Data!

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

$ py my_first_scraper.py

# Usage
$ py my_first_scraper.py