import time
import requests
from bs4 import BeautifulSoup
import time

from twitter_scraper import get_tweets

ignorewords = ['the','of','to','and','a','in','is','it']

users = ['ryan_gess', 'nick_vanden', 't_cooper16', 'pgroves29', 'alexmikula_', 'nick_brown100', 'samuelbrungo', 'dshoe01', 'iqirara', 'catherincurtin', 'jay_shoop', 'owen_kile', 'juantonsooop', 'WilliamFriedri8']

def getwords():
    url = 'https://twitter.com/ryan_gess'
    result = requests.get(url)
    print(result.status_code)
    if (result.status_code == 200):
        html = result.text
        soup = BeautifulSoup(html, 'html.parser')
        p = soup.div

        print(p)



def getusertweets():
    wordlist = []
    for user in users:
        print(user)
        try:
            for tweet in get_tweets(user, pages=3):
                te = tweet['text'].split()
                for i in range(len(te)):
                    wordlist.append(te[i].lower())
        except Exception:
            pass


    result = [word for word in wordlist if word not in ignorewords and '/' not in word]
    result = remove_duplicates(result)
    print(len(result))
    printout(result)
    get_word_counts(result)

def printout(results):
    out = open('twitterdata.txt', 'w')
    out.write('Blog')
    for word in results:
        out.write('\t%s' % word)

    out.write('\n')



def get_word_counts(results):
    out = open('twitterdata.txt', 'a')
    for user in users:
        out.write(user)
        userlist = []
        try:
            for tweet in get_tweets(user, pages=3):
                te = tweet['text'].split()
                for i in range(len(te)):
                    userlist.append(te[i].lower())
        except Exception:
            pass
    
        for i in range(len(results) - 1):
            x = countwords(userlist, results[i])
            out.write('\t%s' % x)
        out.write('\n')
        

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


def countwords(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


getusertweets()
