import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL,)

soup = BeautifulSoup(response.text, "html.parser")

titles_data = soup.select(selector="h3")

title_list = []
for title in titles_data:
    title_list.append(title.getText())
   
title_list.reverse()

with open('movies_scrapper/movies.txt', 'w') as movies_list:
    for movie in title_list:
        movies_list.write(f"{movie}\n")