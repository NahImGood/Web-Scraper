import requests
from bs4 import BeautifulSoup

def find_all(a_str, sub):
    start = 60000
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def get_title_url(html_string):
    text = html_string.text
    start_array = list(find_all(text, 'Stories Index|Story Click|'))
    article_urls = []
    for start in start_array:
      title_index = text.find("Stories Index|Story Click|", start)
      # the index number for the CLOSING title string in the array
      start_index = title_index + len("Stories Index|Story Click|")
      end_index = text.find('"',title_index)
      URLStartIndex = text.find('href="',start_index)
      URLStartIndex = URLStartIndex + 6
      URLEndIndex = text.find('"',URLStartIndex)
      URL = text[URLStartIndex:URLEndIndex]
      # Now holding a list of URLS
      article_urls.append(URL)
    return article_urls;

def get_article_info(article_urls):
    articles = []
    for url in article_urls:
        article = []
        baseURL = 'https://www.worldwildlife.org' + url
        #baseURL = "https://www.worldwildlife.org/stories/seed-dispersing-drones-help-rebuild-koala-populations-devastated-by-bushfires"
        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(baseURL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #  span12 is the class before all the article information
        results = soup.find(id='content')
        # Holds the content container
        title_elem = results.find_all('h1', "hdr-page")
        sub_title_elem = results.find_all('h2', 'hdr-page')
        article_content = results.find_all('div', 'span12')
        if not sub_title_elem:
            continue
        if not article_content:
            continue
        article = {'title': title_elem, 'subtitle': sub_title_elem,'body': article_content}
        articles.append(article.copy())
    print(articles)



url = 'https://www.worldwildlife.org/stories'
headers = {'User-Agent': 'Mozilla/5.0'}
# Opens the url and reads it
webpageData = requests.get(url, headers=headers)
# Calls URL For Article Info
article_urls = get_title_url(webpageData)
get_article_info(article_urls)
# Get article info from article page
