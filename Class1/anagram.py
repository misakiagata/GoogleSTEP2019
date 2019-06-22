import requests
import itertools
from bs4 import BeautifulSoup
import read


def makeCombinations(word):
    wordCount = len(word)
    combination = []
    while wordCount > 0:
        for i in itertools.combinations(word,wordCount):
            combination.append("".join(sorted(list(i))))
        wordCount -= 1
    return combination


def main():
    givenString = input('input given string: ') 
    combination = makeCombinations(givenString)
    d = read.makeSortedDictionary()
    counter = 0
    for i in combination:
        if i in d.keys():
            print(d[i])
            counter += 1
    if counter == 0:
        print('Sorry...but no word can be created') #1つもanagramができなかった場合

if __name__ == '__main__':
    main()
