import requests
from bs4 import BeautifulSoup


session = requests.Session()
headers = {
    "Content-Type": "",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }

url = 'https://eurovisionworld.com/eurovision/2012'
r = requests.get(url, headers=headers,  timeout=(3.05, 27))
html_text = r.content

soup = BeautifulSoup(html_text, "html.parser")
result = soup.findAll("table", {"class":"v_table v_table_main table_sort table_first table_last table_sort_added"})

print(html_text)
print(result)
