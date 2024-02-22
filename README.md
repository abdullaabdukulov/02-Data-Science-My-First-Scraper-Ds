# My first Scraper 

![img.png](img.png)

## Task
Part 0: Request Write a function prototyped: def request_github_trending(url) it will return the result of Request.

Part 1: Extract Write a function prototyped: def extract(page) to find_all instances of HTML code of repository rows 
and return it. You should use BeautifulSoup. :-)

Part 2: Transform Write a function prototyped: def transform(html_repos) taking an array of all the instances of HTML 
code of the repository row. It will return an array of hash following this format: [{'developer': NAME, 
'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]

Part 3: Format Write a function prototyped: def format(repositories_data) taking a repository array of hash and 
transforming it and returning it into a CSV string. Each column will be separated by , and each line by \n The columns 
will be Developer,Repository Name,Number of Stars

## Description

***
Using python libraries `requests and beautifulsoup4`, return a CSV of TOP 25 repositories from Github

1. Request (with request)
2. Extract (with beautifulsoup4)
3. Transform 
4. Format

**Part 0: Requests** Write function like `def request_github_trending(url)` it will return the result of `requests`

**Part 1: Extract** Write function like `def extract(page)` to `find_all` instances of HTML code of repo rows and return it
\
You should use `BeautifulSoup`:)

**Part 2: Transform** Write a function prototyped: `def transform(html_repos)` 
taking an array of all the instances of HTML code of the repository row. 
It will return an array of hash following this format: `[{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]`
\
\
**Part 3: Format** Write a function prototyped: `def format(repositories_data)` taking a repository array of hash and transforming
it and returning it into a `CSV` string. Each column will be separated by `,` and each line by `\n` 
The columns will be `Developer`,`Repository` `Name`,`Number of Stars`

## Installation

- `requests`
- `BeautifulSoup`

```bash
pip install requests
pip install bs4
```

## Usage
To use this code, simply call the 'runner()' function. This function will execute all the necessary steps to extract, 
transform, and format data about trending repositories on GitHub. The formatted data will be displayed as a CSV string 
in the console.
