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



================= { OUTPUT } =================

1)
Author Name: Ahmed Bilal Mehboob
Title: Role of the Speaker
Description: The judiciary should be given the power, as an exceptional measure, to check constitutional violations.
Vist at: https://www.dawn.com/news/1683849/role-of-the-speaker
Time Stamp: 07 Apr, 2022 09:22am

2)
Author Name: Jawed Naqvi
Title: For God’s sake, stop the war
Description: There are as many sides in the battlefield as there are merchants of weapons.
Vist at: https://www.dawn.com/news/1683848/for-gods-sake-stop-the-war
Time Stamp: 07 Apr, 2022 09:26am

3)
Author Name: F.S. Aijazuddin
Title: Avec moi, le déluge
Description: Certain questions cannot be repressed.
Vist at: https://www.dawn.com/news/1683847/avec-moi-le-deluge
Time Stamp: 07 Apr, 2022 07:34am

4)
Author Name: Maria Taimur
Title: A sensitive approach
Description: Women police are better able to engage with communities.
Vist at: https://www.dawn.com/news/1683846/a-sensitive-approach
Time Stamp: 07 Apr, 2022 07:32am

5)
Author Name: Sikander Ahmed Shah
Title: Non-intervention & the law
Description: Western powers have developed novel ways to justify intervention and bring about regime change.
Vist at: https://www.dawn.com/news/1683696/non-intervention-the-law
Time Stamp: 06 Apr, 2022 08:33pm

6)
Author Name: Rafia Zakaria
Title: The massacre in Bucha
Description: Human suffering should be the ultimate instigator of action.
Vist at: https://www.dawn.com/news/1683695/the-massacre-in-bucha
Time Stamp: 06 Apr, 2022 08:33pm

7)
Author Name: Waqas Younas
Title: Defying authority
Description: Scarcity of thought in education is dangerous.
Vist at: https://www.dawn.com/news/1683694/defying-authority
Time Stamp: 06 Apr, 2022 08:05am

8)
Author Name: Mahir Ali
Title: Cracks in Colombo
Description: Sri Lanka’s crisis is both specific and global.
Vist at: https://www.dawn.com/news/1683693/cracks-in-colombo
Time Stamp: 06 Apr, 2022 08:03am

9)
Author Name: Arifa Noor
Title: Wood for the trees
Description: Govts cannot battle political crises, leaving the economy and other matters on autopilot, as they fight for survival.
Vist at: https://www.dawn.com/news/1683545/wood-for-the-trees
Time Stamp: 05 Apr, 2022 08:39am

10)
Author Name: Faisal Siddiqi
Title: Constitutional frauds
Description: How are such frauds possible in the presence of a constitution, a democratic process and an independent judiciary?
Vist at: https://www.dawn.com/news/1683544/constitutional-frauds
Time Stamp: 05 Apr, 2022 08:54am
