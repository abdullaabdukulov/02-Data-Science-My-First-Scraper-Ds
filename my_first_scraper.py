import requests
from bs4 import BeautifulSoup


def extract(page):
    mySoup = BeautifulSoup(page.text, "html.parser")
    return mySoup.find_all("article")


def transform(html_repos):
    myDataSet = []
    for r in html_repos:
        dataHash = {'developer': [],
                    'repository_name': [],
                    'nbr_stars': []
                    }

        developer = r.select_one("span.text-normal").text.split("/")[0].strip()
        slash = r.select_one("h2 a.Link").text.index("/")
        reps = "".join(r.select_one("h2 a.Link").text[slash + 1:].strip())
        nbr_stars = r.select_one('a[href$="/stargazers"]').text.strip()

        dataHash["developer"] = developer
        dataHash["repository_name"] = reps
        dataHash["nbr_stars"] = nbr_stars

        myDataSet.append(dataHash)

    return myDataSet


def format(repositories_data):
    res = "Developer, Repository Name, Number of Stars\n"
    for i in range(0, 10):
        devs = repositories_data[i]["developer"]
        reps = repositories_data[i]["repository_name"]
        stars = repositories_data[i]["nbr_stars"]

        res += f"{devs}, {reps}, {stars}\n"
    return res


def request_github_trending(url):
    return requests.get(url)


url = "https://github.com/trending"
page = request_github_trending(url)
html_repos = extract(page)
repositories_data = transform(html_repos)
print(format(repositories_data))
