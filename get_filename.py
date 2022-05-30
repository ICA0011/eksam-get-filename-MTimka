import requests
from bs4 import BeautifulSoup
import requests

url = "http://upload.itcollege.ee/~aleksei/random_files/"

def get_b(i):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    trs = soup.findAll('tr')[3:]
    row = trs[i]
    return row.findAll('a')

def get_filename(url):

  # your code here
  filename = url + '/' + str(get_b(5)).split('>')[1].split('<')[0]

  return filename


print(get_filename(url))
