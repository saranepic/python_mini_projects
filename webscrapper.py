import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.thehindu.com/latest-news/")
b = BeautifulSoup(res.text, 'html.parser')
news = b.select('.latest-news')
fn = []
for i in range(len(news)):
    final = news[i].getText()
    fn.append(final)
f = news[0]
h = open('news.txt', 'w')
h.write(f)
print(*fn, sep="\n")
