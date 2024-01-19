import requests
from bs4 import BeautifulSoup


def request_github_trending(url):
     page = requests.get(url)
     return page

def extract(page):
    res = []
    soup = BeautifulSoup(page.text, 'html.parser')
    arts = soup.find_all("article", class_="Box-row")
    for art in arts:
        my_data = []
        art_h1 = art.select_one("h1.h3.lh-condensed")
        stars = art.select_one("span.d-inline-block.float-sm-right").text.strip()
        my_data.append(stars)
        name = art.select_one("img.avatar.mb-1.avatar-user")["alt"]
        my_data.append(name)
        rep_name = art_h1.select_one("a")["href"]
        my_data.append(rep_name)
        res.append(my_data)
    return res

def transform(html_repos):
    res = []
    for i in html_repos:
        data = {'developer': i[1], 'repository_name': i[2], 'nbr_stars': i[0]}
        res.append(data)
    return res

def format(repositories_data):
    csv_con = "Developer, Repository Name, Number of Stars\n"
    for i in repositories_data:
        csv_con += i["developer"] + "," + i["repository_name"] + "," + i["nbr_stars"]
    return csv_con