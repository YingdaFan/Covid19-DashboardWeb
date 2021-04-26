import requests
import bs4


def get_news():
    url = "https://www.nytimes.com/search?query=covid"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "lxml")
    all_news = soup.find_all(class_='css-e1lvw9')
    news_list = []
    for item in all_news:
        url = "https://www.nytimes.com/" + item.contents[1].attrs["href"]
        title = item.contents[1].contents[0].contents[0]
        content = item.contents[1].contents[1].contents[0]
        news = {"url": url, "title": title, "content": content}
        news_list.append(news)
    return news_list
