import requests
import itertools
from bs4 import BeautifulSoup


def makeSortedDictionary():
    url = "https://icanhazwordz.appspot.com/dictionary.words"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    defaultList = str(soup).split() 
    dictionary = {} 
    for i in defaultList:
        key = "".join(sorted(i))
        dictionary[key] = i
    return dictionary
