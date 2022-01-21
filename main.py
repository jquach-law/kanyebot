import discord
import os
import requests
import json
from keep_alive import keep_alive
import random

client = discord.Client()

greatest = ['greatest', 'Greatest', 'GREATEST', 'perfect', 'Perfect', 'PERFECT','highest', 'Highest', 'HIGHEST', 'crazy', 'Crazy', 'CRAZY','holy', 'Holy', 'HOLY', 'Kardashian', 'kardasdian', 'KARDASHIAN', 'Chicago', 'chicago', 'CHICAGO', 'West', 'west', 'WEST', 'North', 'north', 'Donda', 'donda', 'DONDA', 'Yeezy', "YEEZY", 'yeezy', 'trump', 'Trump', 'TRUMP', 'KING', 'King', 'king', 'Grammy', 'grammy', 'Jesus', 'JESUS', 'jesus', 'Pablo', 'pablo', 'PABLO', 'MAGA', 'Maga', 'maga', 'SAINT', 'Saint', 'saint', 'race', 'RACE', 'Race', 'racist', 'Racist', 'RACIST', 'Slavery', 'slavery', 'SLAVERY',  'Yeezus', 'YEEZUS', 'yeezus',  'Taylor Swift', 'TAYLOR SWIFT', 'taylor swift']

ye = ['ye', 'YE', 'Ye', 'ok', 'OK', 'Ok', 'New York', 'new york', 'NEW YORK', 'ny', 'NY', 'LA', 'impossible', 'IMPOSSIBLE', 'Impossible', 'important', 'IMPORTANT', 'Important', 'great', 'Great', 'GREAT', 'best', 'Best', 'BEST', 'kanye', 'Kanye', 'KANYE']

def get_quote():
  response = requests.get("https://api.kanye.rest/")
  json_data = json.loads(response.text)
  quote = json_data["quote"]
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  # Don't read your own messages
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$bruteforce'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in greatest):
    rand_int = random.randint(0, 2)
    if rand_int == 2:
      quote = get_quote()
      await message.channel.send(quote)

  if any(word in msg for word in ye):
    rand_int = random.randint(0, 4)
    if rand_int == 2:
      quote = get_quote()
      await message.channel.send(quote)

keep_alive()
client.run(os.getenv('TOKEN'))