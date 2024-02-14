import requests
from bs4 import BeautifulSoup


def request_github_trending(url):
    res = requests.get(url)
    return res


def extract(page):
    res = []
    soup = BeautifulSoup(page.text, 'html.parser')
    rs = soup.find_all("article", class_="Box-row")
    for r in rs:
        try:
            iteam = []
        except:
            r_h1 = None
        r_h1 = r.select_one("h2.h3.lh-condensed")
        stars = r.select_one("span.d-inline-block.float-sm-right").text.strip()
        iteam.append(stars)
        name = r.select_one("img.avatar.mb-1.avatar-user")["alt"]
        iteam.append(name)
        re_name = r_h1.select_one("a")["href"]
        iteam.append(re_name)
        res.append(iteam)

        #print(bun)
    return res


def transform(html_repos):
    res = []
    for i in html_repos:
        ban = {'developer': i[1], 'repository_name': i[2], 'nbr_stars': i[0]}
        res.append(ban)
    return res


def format(repositories_data):
    csv_data = "Developer,Repository Name,Number of Stars\n"
    for i in repositories_data:
        csv_data += i["developer"] + "," + i["repository_name"] + "," + i["nbr_stars"] + "\n"
    return csv_data


def check():
    url = "https://github.com/trending"
    page = request_github_trending(url)
    results = extract(page)
    res = transform(results)
    print(format(res))


check()
