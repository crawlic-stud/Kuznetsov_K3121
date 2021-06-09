import re

import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    total_news = parser.findAll('tr', {'class': 'athing'})
    total_subtexts = parser.findAll('td', {'class': 'subtext'})
    for i in range(30):
        news_structure = {
            'title': article(total_news[i])[0],
            'author': subtext(total_subtexts[i])[0],
            'comments': subtext(total_subtexts[i])[2],
            'points': subtext(total_subtexts[i])[1],
            'link': article(total_news[i])[1]
        }
        news_list.append(news_structure)

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    next_page = parser.find("a", class_="morelink").get("href")
    return next_page


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news


def article(a):
    title = a.find('a', {'class': 'storylink'})
    links = a.find('span', {'class': 'sitestr'})
    try:
        link = links.text
    except AttributeError:
        link = 'no link'
    return [title.text, link]


def subtext(s):
    authors = s.find('a', {'class': 'hnuser'})
    scores = s.find('span', {'class': 'score'})
    comments = s.find("a", href=re.compile("item"), recursive=False)

    try:
        ugly = comments.text
        s = ''
        for x in ugly:
            if ugly[0] == 'd':
                comment = '0 comments'
            elif x.isdigit():
                s += x
            else:
                if s[-1] == '1':
                    comment = s + ' comment'
                else:
                    comment = s + ' comments'
    except AttributeError:
        comment = '0 comments'

    try:
        author = authors.text
    except AttributeError:
        author = 'unknown author'

    try:
        score = scores.text
    except AttributeError:
        score = '0 points'

    return [author, score, comment]

"""
# DEBUGGING:
y = 0
for i in total_news:
    y += 1
    print(y, 'out of', len(total_news))
    print(article(i))

print('_____________________________________')

x = 0
for i in total_subtexts:
    x += 1
    print(x, 'out of', len(total_subtexts))
    print(subtext(i))
"""

print(get_news('https://news.ycombinator.com', 3))



