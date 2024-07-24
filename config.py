from domain import *

# PROJECT_NAME='ranveerbrar'
PROJECT_NAME='sanjaykitchen'

# HOMEPAGE= 'https://ranveerbrar.com/'
HOMEPAGE= 'https://sanjaykitchen.com/'

DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME + '/queue.txt'
CRAWLED_FILE=PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS=8

user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

extra_headers = {
    'User-Agent': user_agent,
    'Sec-Ch-Ua':
    '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile':
    '?0',
    'Sec-Ch-Ua-Platform':
    "Linux",
    'Sec-Fetch-Dest':
    'empty',
    'Sec-Fetch-Mode':
    'cors',
    'Sec-Fetch-Site':
    'same-site',
    }

path='/home/kevit/Downloads/chromedriver-linux64/chromedriver'
urls_to_be_removed=['jpg', 'png', 'pdf', 'comment', 'post','respond','page','jpeg','#','addtoany','facebook','youtube','amazon','pinterest','instagram','whatsapp','img','image','gallery']
