from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

youtube_trending_url = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')

  # we need to put path of driver when ising on desktop
  # for replit no need to mention path
  driver = webdriver.Chrome(options = chrome_options)
  return driver

if __name__ == '__main__':
  print('Creating driver')
  driver = get_driver()

  print('Fetching page')
  driver.get(youtube_trending_url)
  # print('Page title: ', driver.title)

  print('Get video divs')
  video_div_class = 'style-scope ytd-video-renderer'
  video_divs = driver.find_elements(By.video_div_class)
  print(f'Found{len(video_divs)} videos')