import urllib, urllib2, os
from bs4 import *

vidName = raw_input('Enter Video Search Query Or Video URL: ')
if str.find(vidName, 'https') == 0:
    vidLink = vidName
else:
	query = "https://www.youtube.com/results?search_query=" + urllib.quote(vidName)
	response = urllib2.urlopen(query).read()
	soup = BeautifulSoup(response, 'html.parser')
	vidLink = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']

os.system('youtube-dl -citk FORMAT URL ' + str(vidLink))
