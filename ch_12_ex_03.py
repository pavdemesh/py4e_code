# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import ssl
import urllib.request
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter count: "))
pos = int(input("Enter position: "))

print("Retrieving:", url)

for i in range(count):
    # Empty list to store links
    tmp_list = list()
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Add all links as str items to the list
    for tag in tags:
        tmp_list.append(tag.get('href', None))
    # print(tmp_list)
    # print(tmp_list[pos - 1].split("_")[2][:-5])
    # Assign new url address from the list of links (anchor tags)
    url = tmp_list[pos-1]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print("Retrieving:", url)

try:
    print(tmp_list[pos - 1].split("_")[2][:-5])
except IndexError:
    print("Something wrong with the list indices")
    print("The list looks like this:", tmp_list)
