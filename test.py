import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()
ytkey = os.getenv('YT_API')

def youtube(query):
    response = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=% s&type=video&key=% s' % (query, ytkey))
    response_json = json.loads(response.text)
    videoid = response_json['items'][0]['id']['videoId']
    title = response_json['items'][0]['snippet']['title']
    thumb = response_json['items'][0]['snippet']['thumbnails']['default']['url']
    url = "https://www.youtube.com/watch?v=" + videoid
    print(title+"\n")
    print(thumb+"\n")
    print(url+"\n")
    return url
youtube("i took a pill in ibiza")

##EMBED URL##
# https://gasaisb.net/embed.php?title=Testing&description=This is a testing embed&image=https://i.ytimg.com/vi/jIQ0Dx-4peE/default.jpg&color=cc66ff