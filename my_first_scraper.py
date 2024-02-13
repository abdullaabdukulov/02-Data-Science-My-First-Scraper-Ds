import requests
from bs4 import BeautifulSoup


# Part 0: Request
def request_github_trending(url):
    response = requests.get(url)
    return response.text


# Part 1: Extract
def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    repo_rows = soup.find_all('article', class_='Box-row')
    return repo_rows


# Part 2: Transform
def transform(html_repos):
    transformed_data = []
    for repo in html_repos:
        developer_elem = repo.find('span', class_='text-normal')
        repo_name_elem = repo.find('h2', class_='h3 lh-condensed')
        stars_elem = repo.find('a', class_='Link Link--muted d-inline-block mr-3')

        if developer_elem and repo_name_elem and stars_elem:
            developer = developer_elem.text.split("/")[0].strip()
            repo_name = repo_name_elem.text.strip().split()[-1]
            stars = stars_elem.text.strip()

            transformed_data.append({'developer': developer, 'repository_name': repo_name, 'nbr_stars': stars})

    return transformed_data


# Part 3: Format
def format(repositories_data):
    csv_string = "Developer | Repository Name | Number of Stars\n\n"
    for repo in repositories_data:
        csv_string += f"{repo['developer']} | {repo['repository_name']} | {repo['nbr_stars']}\n"
    return csv_string


# Main function
def main():
    github_trending_url = 'https://github.com/trending'
    page = request_github_trending(github_trending_url)

    if page:
        html_repos = extract(page)
        transformed_data = transform(html_repos)
        print(format(transformed_data))


if __name__ == "__main__":
    main()
