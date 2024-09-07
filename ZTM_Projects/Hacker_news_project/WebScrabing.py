import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def create_custome_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href =links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[idx].getText().replace('points',""))
            print(points)
            hn.append({"title":title, "links":href})
    return hn 
    
print(create_custome_hn(links, subtext))