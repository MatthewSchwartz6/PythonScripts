#!/home/alive/projects/venv/FetchSubredditLinks/bin/python
from __future__ import unicode_literals
import os
from sys import argv
import requests
from bs4 import BeautifulSoup
import youtube_dl

youtube = "https://www.youtube.com/results?search_query=";

search = argv[1]
word_list = search.split()
searchQ = ""

if len(word_list)>1:
    for word in word_list:
        if word != word_list[(len(word_list))-1]:
            searchQ += (word + '+')
        elif word == word_list[(len(word_list))-1]:
            searchQ +=word
else:
    searchQ = str(word_list)

youtube += searchQ
request = requests.get(youtube)
soup = BeautifulSoup(request.text,'html.parser')

cont = []
videos = []
titles = []

links = soup.find_all("a")
for link in links:
    urls = link["href"]
    if urls[:6] =="/watch" and len(urls) == 20:
        cont.append(urls)

i = 1
for c in cont:
    if i % 2 == 0:
        videos.append(c)
    i += 1

headers = soup.find_all("h3")
for h in headers:
    title = h.get_text()
    if title[len(title)-1] == ".":
        titles.append(title)

for i in range(len(videos)-1):
    print ("\n" + str(i+1) + "). " + titles[i] + "\n" + videos[i] + "\n")

choices = []

choice = raw_input("Type the number(s) of the track(s) you'd like to download separated by a space: ")
choices = choice.split()

tracks_to_download = []
i=0
for i in range(len(choices)):
    tracks_to_download.append("https://www.youtube.com" + videos[ (int( choices[i]) - 1) ])

ydlOpts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'ignoreerrors': True,
    'postprocessors':[{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '320',
    }],
}

directory = "/media/alive/secondary/Music"
if os.path.isdir(directory) is not True:
    os.mkdir(directory)
os.chdir(directory)
with youtube_dl.YoutubeDL(ydlOpts) as ydl:
    ydl.download(tracks_to_download)
