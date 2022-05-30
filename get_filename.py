import requests
from bs4 import BeautifulSoup
import requests

url = "http://upload.itcollege.ee/~aleksei/random_files/"

def get_b(i):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    trs = soup.findAll('tr')[3:]
    row = trs[i]
    return row.find('a')

def get_filename():

  # your code here
  # get 5th element starts from file10 -> ...
  filename = url + '/' + get_b(5).contents[0]

  return filename


#print(get_filename())
