from selenium import webdriver
import discord
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

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
client.run('ODgzODM4NTEyODYyOTk0NDQy.GVGnu8.UjcLsUu3fphyVz49WV7FZVftvLYUciJzb5akKw')
