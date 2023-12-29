import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return requests.get(url)

def extract(page):
    mySoup = BeautifulSoup(page.text, "html.parser")
    return mySoup.find_all("article")

def transform(html_repos):
    data = []
    for i in html_repos:
        data_hash = {'developer': [], 'repository_name': [], 'nbr_stars': []}

        all = i.select_one("a.d-inline-block")["href"].split("/")[1:-1]
        developer, repos_name = all
        nbr_stars = i.select_one("a.Link.Link--muted.d-inline-block.mr-3").text.strip()

        data_hash["developer"] = developer
        data_hash["repository_name"] = repos_name
        data_hash["nbr_stars"] = nbr_stars

        data.append(data_hash)

    return data

def format(repositories_data):
    response = "Developer, Repository Name, Number of Stars\n"
    for ind in repositories_data:
        developers = ind["developer"]
        repository_name = ind["repository_name"]
        stars = ind["nbr_stars"]

        response+=f"{developers}, {repository_name}, {stars}\n"

    return response


url = "https://github.com/trending"
page = request_github_trending(url)
html_repos = extract(page)
repositories_data = transform(html_repos)
print(format(repositories_data))
