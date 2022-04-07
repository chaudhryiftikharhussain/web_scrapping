# pip install beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.dawn.com/opinion').text

soup = BeautifulSoup(html_text, 'html.parser')

opinions = soup.findAll('article', class_="story box mb-2 p-2 border-b border-gray-200")

count = 1
for i in opinions:
    author_name = i.find('a', class_="story__byline__link").text
    opinion_title = i.find('a', class_="story__link").text
    short_description = i.find('div', class_="story__excerpt font-merriweather overflow-hidden text-3.5 text-gray-600 leading-5").text
    if "Updated" in short_description:
        short_description = short_description.split(" Updated ")
    elif "Published" in short_description:
        short_description = short_description.split(" Published ")
    short_description = short_description[0]
    time_stamp = i.find('span', class_="timestamp--time timeago").text
    view_at = i.find('a', class_="story__link")['href']

    print(f'{count})')
    print(f'Author Name: {author_name.strip()}')
    print(f'Title: {opinion_title.strip()}')
    print(f'Description: {short_description.strip()}')
    print(f'Vist at: {view_at.strip()}')
    print(f'Time Stamp: {time_stamp.strip()}')
    print('')
    count += 1
