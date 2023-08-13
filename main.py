from selenium import webdriver
import discord
from selenium.webdriver.common.action_chains import ActionChains
import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()
ytkey = os.getenv('YT_API')
token = os.getenv('DISCORD_TOKEN')
driver = webdriver.Firefox()

def youtube(query):
    response = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=% s&type=video&key=% s' % (query, ytkey))
    response_json = json.loads(response.text)
    videoid = response_json['items'][0]['id']['videoId']
    title = response_json['items'][0]['snippet']['title']
    thumb = response_json['items'][0]['snippet']['thumbnails']['default']['url']
    url = "https://www.youtube.com/watch?v=" + videoid
    return title, thumb, url

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('!g'):
            await message.reply('Hello!', mention_author=True)
            link = message.content.replace('!g ', '')
            driver.get(link)
        if message.content.startswith('!p'):
            await message.reply('Playing..', mention_author=True)
            actions = ActionChains(driver)
            actions.send_keys('k')
            actions.perform()
        if message.content.startswith('!s'):
            query = message.content.replace('!s ','')
            title, thumb, url = youtube(query)
            await message.reply('https://gasaisb.net/embed.php?title=% s&image=% s' % (title.replace(' ','%20'), thumb))
            driver.get(url)

client = MyClient()
client.run(token)
