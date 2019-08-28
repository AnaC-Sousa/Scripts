from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.uuidgenerator.net/"
request = urlopen(url)

soup = BeautifulSoup(request, 'html.parser')
uuid = soup.find(id = 'generated-uuid')

print(uuid.get_text())