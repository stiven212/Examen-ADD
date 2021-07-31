import requests
import pandas as pd
from bs4 import BeautifulSoup

------------------------------


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def find_1st(string, substring):
    return string.find(substring, string.find(substring))


response = requests.get("https://olympics.com/tokyo-2020/es/")
soup = BeautifulSoup(response.content, "lxml")

Title = []
Notice = []

---------------------------

post_title = soup.find_all("div", class_="tk-liveblog__home-post-discipline")
post_notice = soup.find_all("div", class_="tk-liveblog__home-post-body-title")


--------------------------------------------------

for element in post_title:
    element = str(element)
    limpio = str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Title.append(limpio.strip())

for element in post_notice:
    element = str(element)
    limpio = str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Notice.append(limpio.strip())


--------------------------------------------------------------


dfDS = pd.DataFrame({'titulo': Title, 'Noticia': Notice})


--------------------------------------------------------------

dfDS
