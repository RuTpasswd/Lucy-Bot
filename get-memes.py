# model scraping for themodelbot

import requests
from bs4 import BeautifulSoup as bs
import os 

#website with model images
url = 'https://www.memedroid.com'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create a directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to a new diectory
os.chdir('models')

# image file name variable
x = 0

# writing images
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
