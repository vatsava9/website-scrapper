import requests
from bs4 import BeautifulSoup

youtube_trending_url = 'https://www.youtube.com/feed/trending'

response = requests.get(youtube_trending_url)
print('Status code is ', response.status_code)

with open('trending.html', 'w') as t:
  t.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print('Page title : ', doc.title)
print('Page title : ', doc.title.text)

# Find all video divs
video_divs = doc.find_all('div', class_ = 'ytd-video-renderer')
print(f'Found {len(video_divs)} videos')

