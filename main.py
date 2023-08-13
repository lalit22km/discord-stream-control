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
    search=query
    response = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={search}&type=video&key=AIzaSyC04UyXaN9bTqg_Acao0uv9N6-7TpOVHTw")
    return

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('!goto'):
            await message.reply('Hello!', mention_author=True)
            link = message.content.replace('!goto ', '')
            driver.get(link)
        if message.content.startswith('!play'):
            await message.reply('Playing..', mention_author=True)
            actions = ActionChains(driver)
            actions.send_keys('k')
            actions.perform()

client = MyClient()
client.run(token)
