import requests
from bs4 import BeautifulSoup

def main():
    url ="https://news.ycombinator.com/item?id=40846428"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="comment")

    print(f"Elements: {len(elements)}")

    print(f"Scraping... {url}")
    print(response)
    print(response.content)


if __name__ == "__main__":
    main()
