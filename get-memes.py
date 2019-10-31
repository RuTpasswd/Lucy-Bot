import requests
from bs4 import BeautifulSoup as bs
import os 

url = 'https://www.memedroid.com'

page = requests.get(url)
soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')

if not os.path.exists('memes'):
    os.makedirs('memes')

os.chdir('memes')

x = 0

for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-'+ str(x) + '.jpeg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x+=1
    except:
        pass
