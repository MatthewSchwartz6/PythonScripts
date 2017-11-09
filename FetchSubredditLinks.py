#!/home/alive/projects/venv/FetchSubredditLinks/bin/python
###############
##Fetch Subreddit's Youtube Links ##
##(and download them)
#For Python 2.x on the command line

#Edit the "mainDir" variable in fetchLinks() to pick a directory to store the downloaded mp3's in.

#This program will create a batch text file of Youtube URL's from a subreddit.

#In case you don't want to download the mp3's, just comment out the musicListener.downloadtracks() statement at the bottom.

#You need to download a couple of packages too.
#pip install requests bs4 youtube_dl
#apt install ffmpeg
##############


from __future__ import unicode_literals
import os
import datetime

import requests
from bs4 import BeautifulSoup
import youtube_dl


class FetchLinks:
    subredditPage = ""
    subredditName = ""
    pageDepth     = 0
    nav           = ""
    youtubeLinks  = ""

    def getsubreddit(self):
        self.subredditName = raw_input("Download some of the youtube tracks from a music subreddit.\nSubreddit name: ")

        self.subredditPage = self.subredditName

        self.nav = raw_input("\nSubreddits have many options for their pages.\nYou can check out \"hot\",\"new\" or \"top\".\nPage option: ")
        #work on this so it spits an error if they don't enter one of the three
        self.subredditPage+=("/" + self.nav + "/")

        if self.nav == "top":
        	timePref = raw_input("For the top voted posts to this subreddit you can choose between posts from the past week, month, year, or \"all\" for all time.\nTime preference: ")
        	self.subredditPage+=("?sort=top&t=" + timePref)

        self.pageDepth = raw_input("How many pages deep you want to extract links from?\nFor just the first page enter \"1\".\nPage depth: ")

    def fetchlinks(self):

        i = 0
        count = 25
        pd = int(self.pageDepth)

        todayBox = []
        date = datetime.date.today()
        todayBox.append(date)

        URL = []
        baseURL = "https://www.reddit.com/r/"
        mainDir = "/media/alive/secondary/Music/"
        directory = mainDir + self.subredditName + "/"
        if os.path.isdir(directory) is not True:
		          os.mkdir(directory)
        os.chdir(directory)
        self.youtubeLinks = directory + self.subredditName + "[" + self.nav + " as of " + str(todayBox[0]) + "]" + ".txt"
        File = open(self.youtubeLinks,'a')

        while (i<pd):
            if i>0:
                nextPage = ("?count=" + str(count) + "&after=")
                nextPageID = lastDiv['data-fullname']
                URL.append(baseURL + self.subredditPage + nextPage + nextPageID)
                count+=25
            else:
                URL.append(baseURL + self.subredditPage)

            request = requests.get(URL[i],headers = {'User-agent':'your bot 0.1'})
            soup = BeautifulSoup(request.text,'html.parser')
            links = soup.find_all('div',{'data-url':True})
            lastDiv = links[(len(links))-1]
            print "\n"
            i+=1

            for link in links:
                music = link['data-url']
                if ((str(music)[:23]) == "https://www.youtube.com"):
                    File.write("%s\n" % music)
                    print (str(i) + ".) " + music)

        File.close()


    def downloadtracks(self):
        listURL = []
        URLFile = open(self.youtubeLinks,'r')
        readURLFile = URLFile.read()
        listURL = readURLFile.splitlines()
        URLFile.close()

        def hook(d):
            if d['status']=='finished':
                print '\nTrack downloaded \m/'

        ydlOpts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
	        'ignoreerrors': True,
            'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
            }],
            'progress_hooks':[hook],
        }


        with youtube_dl.YoutubeDL(ydlOpts) as ydl:
		          ydl.download(listURL)

if __name__ == '__main__':
            musicListener = FetchLinks()
            musicListener.getsubreddit()
            musicListener.fetchlinks()
            musicListener.downloadtracks()
