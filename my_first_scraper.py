import requests
from bs4 import BeautifulSoup



def request_github_trending(url):
    return requests.get(url)
def extract(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all("article", class_= "Box-row")
    return news
def transform(html_repos):
    res = []
    for i in html_repos:
        my_dict = {'developer': "", 'repository_name': "", 'nbr_stars': ""}
        my_dict['nbr_stars'] = i.select_one("span.d-inline-block.float-sm-right").text.strip()
        rep_name = i.select_one("h1.h3.lh-condensed")
        my_dict['repository_name'] = rep_name.select_one("a")["href"]
        my_dict['developer'] = i.select_one("img.avatar.mb-1.avatar-user")["alt"]
        res.append(my_dict)
    return res

def format(repositories_data):
    # print(repositories_data)
    # print("Developer,Repository Name,Number of Stars")
    csv_str = "Developer,Repository Name,Number of Stars\n"
    for i in repositories_data:
        csv_str += i["developer"] + "," + i["repository_name"] + "," + i["nbr_stars"] + "\n"
        # print(i["developer"])
    return (csv_str)
    

def runner():
    url = "https://github.com/trending"
    req = request_github_trending(url)
    sp = extract(req)
    tr = transform(sp)
    format(tr)



# runner()