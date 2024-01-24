import requests
from bs4 import BeautifulSoup
import csv



def request_github_trending(url):
    response = requests.get(url)
    return response


def extract(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    repository_rows = soup.find_all('article', class_='Box-row')
    return repository_rows

def transform(html_repos):
    repositories_data = []
    for repo in html_repos:
        developer = repo.find('span', class_='text-normal').text.strip()
        repo_name = repo.find('h1', class_='h3').text.strip()
        stars = repo.find('a', class_='Link--muted').text.strip()
        repositories_data.append({
            'developer': developer,
            'repository_name': repo_name,
            'nbr_stars': stars
        })
    return repositories_data



def format(repositories_data):
    csv_data = []
    csv_data.append(['Developer', 'Repository Name', 'Number of Stars'])
    for repo in repositories_data:
        csv_data.append([repo['developer'], repo['repository_name'], repo['nbr_stars']])
    csv_string = ''
    csv_data = [','.join(row) for row in csv_data]
    csv_string = '\n'.join(csv_data)
    return csv_string


def scrape_github_trending():
    url = 'https://github.com/trending'
    page = request_github_trending(url)
    html_repos = extract(page)
    repositories_data = transform(html_repos)
    csv_data = format(repositories_data)
    return csv_data


def test_request_github_trending():
    url = 'https://github.com/trending'
    page = request_github_trending(url)


    assert isinstance(page, requests.Response)


test_request_github_trending()