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
    start_array = list(find_all(webpageData, 'Stories Index|Story Click|'))
    # print(start_array)
    article_urls = []
    for start in start_array:
      title_index = html_string.find("Stories Index|Story Click|", start)

      # the index number for the CLOSING title string in the array
      start_index = title_index + len("Stories Index|Story Click|")

      end_index = webpageData.find('"',title_index)

      URLStartIndex = webpageData.find('href="',start_index)
      URLStartIndex = URLStartIndex + 6
      URLEndIndex = webpageData.find('"',URLStartIndex)
      URL = webpageData[URLStartIndex:URLEndIndex]
      # Now holding a list of URLS
      article_urls.append(URL)
    return article_urls;

def get_article_info(article_urls):

    for url in article_urls:
        articles = []
        baseURL = Request('https://www.worldwildlife.org' + url, headers={'User-Agent': 'Mozilla/5.0'})
        page = requests.get(baseURL)
        soup = BeautifulSoup(page.content, 'html.parser')
        #  span12 is the class before all the article information
        article_data = webpage.decode("utf-8")
        " ".join(article_data.split())
        # Holds the content container
        results = soup.find(id='content')
        print(results.prettify())


req = Request('https://www.worldwildlife.org/stories', headers={'User-Agent': 'Mozilla/5.0'})
# Opens the url and reads it
page = requests.get(req)
# Holds the data from the url request
webpageData = page.decode("utf-8")
# Calls URL For Article Info
article_urls = get_title_url(webpageData)
get_article_info(article_urls)
# Get article info from article page
