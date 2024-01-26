import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    san = requests.get(url)
    return san

def extract(page):
    rep = []
    soup = BeautifulSoup(page.text, 'html.parser')
    repos = soup.find_all("article", class_="Box-row")
    for repo in repos:
        info = []

        # Check if the selector matches any element
        r_h1 = repo.select_one("h1.h3.lh-condensed")
        if r_h1:
            stars = repo.select_one("span.d-inline-block.float-sm-right").text.strip()
            info.append(stars)
            name = r_h1.select_one("a")["href"]
            info.append(name)
            developer = repo.select_one("img.avatar.mb-1.avatar-user")["alt"]
            info.append(developer)
            rep.append(info)

    return rep


def transform(html_repos):
    bu = []
    for i in html_repos:
        ban = {'developer': i[1], 'repository_name': i[2], 'nbr_stars': i[0]}
        bu.append(ban)
    return bu    

def format(repositories_data):
    csv_sun = "Developer,Repository Name,Number of Stars\n"
    for i in repositories_data:
        csv_sun += i["developer"] + "," + i["repository_name"] + "," + i["nbr_stars"] + "\n"
    return csv_sun
    



def chec():
    url = "https://github.com/trending"
    page = request_github_trending(url)
    buns = extract(page)
    bun = transform(buns)
    format(bun)


chec()    
