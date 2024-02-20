import requests
from bs4 import BeautifulSoup


def request_github_trending(url):
    response = requests.get(url)
    return response


def extract(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    trending = soup.find_all('article')
    return trending


def transform(html_repos):
    repos = []
    for repo in html_repos:
        data = {}
        NAME = repo.find(class_='avatar mb-1 avatar-user')['alt']
        REPOS_NAME = repo.find(class_='h3 lh-condensed').get_text().strip().split()[-1]
        NBR_STARS = repo.find(class_='d-inline-block float-sm-right').get_text().strip().split()[0]
        data['developer'] = NAME
        data['repository_name'] = REPOS_NAME
        data['nbr_stars'] = NBR_STARS
        repos.append(data)
    return repos


def format(repositories_data):
    print("Developer,", "Repository Name,", "Number of Stars")
    for repo in repositories_data:
        print(f'{repo["developer"]}, {repo["repository_name"]}, {repo["nbr_stars"]}\n')


f1 = request_github_trending(url='https://github.com/trending')
f2 = extract(f1)
f3 = transform(f2)
format(f3)
