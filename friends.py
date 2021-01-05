import sys
import urllib.error
from urllib import request
import random
import pickle
import re

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

from bs4 import BeautifulSoup

sys.setrecursionlimit(500)  

extra_stopwords = ["'d", "i-", "i-i", "i'll", "'ll", "'ve", "'", "'re", "'m", "okay", "oh...", "oh" "hey", "gotta", "would", "won't", "'m", "'s", "oh", "n't", "...", "--", "that's"]
stop_words = set(stopwords.words("english"))
stop_words = list(stop_words) + extra_stopwords



series=[
    (1,24),
    (2,24),
    (3,25),
    (4,23),
    (5,23),
    (6,24),
    (7,23),
    (8,23),
    (9,23),
    (10,17),
]
doubleepisode=["0212","0615","0923","1017"]

#for serie, episodes in series:
#    info = {}
#    info[serie] = {}
 #   for serie in range(1,2):
#       url = "https://en.wikipedia.org/wiki/Friends_(season_{serie})".format(serie=serie)
#        print(url)
#        html = request.urlopen(url).read()
#        soup = BeautifulSoup(html, 'html.parser')
#        for i in range(1,episodes+1):
#            output = soup.find(id="ep{ep_number}".format(ep_number = i))
#            print(output)



#for serie, episodes in series:
#    info = {}
#    info[serie] = {}
 #   for serie in range(1,2):
url = "https://en.wikipedia.org/wiki/List_of_Friends_episodes"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#titles=soup.findAll("td",{"class":"summary"})
#for title in titles:
#    print(title.a.text)



#assign titles[0] and remove first tile from the list



#output = soup.findAll("tr", {"class": "summary"})
#print(output)



transcripts={}
tokens={}
titles={}

for serie,episodes in series:
    punctuation = '''!()[]:"\,<>./...?'''
    transcripts[serie]={}
    tokens[serie]={}
    titles[serie]={}
    for episode in range(1,episodes+1):

        if "{serie:02d}{episode:02d}".format(serie=serie,episode=episode) in doubleepisode:
            url = "https://fangj.github.io/friends/season/{serie:02d}{episode_1:02d}-{serie:02d}{episode_2:02d}.html".format(serie=serie,episode_1=episode,episode_2=episode+1)
        else:
            url = "https://fangj.github.io/friends/season/{serie:02d}{episode:02d}.html".format(serie=serie,episode=episode)


        try:
            html = request.urlopen(url).read()
        except urllib.error.HTTPError:
            print("Could not get series {} episode {}".format(serie,episode))
            continue
        title = str(BeautifulSoup(html, 'html.parser').title.string)
        raw = BeautifulSoup(html, 'html.parser').body

        transcripts[serie][episode]=raw.get_text()
        titles[serie][episode] = title


        tokens_raw = word_tokenize(transcripts[serie][episode])
        tokens_no_punct = []
        for item in tokens_raw:
            if item not in punctuation:
                tokens_no_punct.append(item.lower())

        tokens_list = [word for word in tokens_no_punct if word not in stop_words]
        tokens[serie][episode] = tokens_list

#print(titles)

with open('friends_tokens','wb') as friends_tokens:
    pickle.dump(tokens, friends_tokens)

with open('friends_titles','wb') as friends_titles:
    pickle.dump(titles, friends_titles)
