import requests

url_template= 'http://wttr.in/{}?mTn&lang=ru'
cities = ['london', 'svo', 'cherepovets']
for city in cities:
    url = url_template.format(city)
    #print(url)
    response = requests.get(url)
    print(response.text)
