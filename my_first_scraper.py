import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return requests.get(url)

def extract(abc):
    hj = BeautifulSoup(abc.text, "html.parser")
    return hj.find_all("article")

def transform(html_repos):
    bf = []
    for row in html_repos:
        repo_name_element = row.select_one('h2 a')
        number_stars_element = row.select_one('span.d-inline-block.float-sm-right')
        developer_name = row.select_one('img.avatar.mb-1.avatar-user')['alt']

        # Check if elements are not None before accessing their text
        rn = repo_name_element.get_text(strip=True) if repo_name_element else ''
        number_stars = number_stars_element.get_text(strip=True) if number_stars_element else ''

        bf.append({'developer': developer_name, 'repository_name': rn, 'nbr_stars': number_stars})
    return bf

def format(repositories_data):
    bf = ["Developer, Repository Name, Number of Stars"]
    for repos in repositories_data:
        row = [repos["developer"], repos['repository_name'], repos["nbr_stars"]]
        bf.append(', '.join(row))
    return "\n".join(bf)

def _main():
    url = "https://github.com/trending"
    abc = request_github_trending(url)
    html_repos = extract(abc)
    repositories_data = transform(html_repos)
    print(format(repositories_data))

_main()
