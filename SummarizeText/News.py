import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=d9a29ade6721422a9903c59c296e2092')
url1 = ('https://newsapi.org/v2/everything?q=Wuhan&'
       'apiKey=d9a29ade6721422a9903c59c296e2092')
response = requests.get(url1)
print(response.json())