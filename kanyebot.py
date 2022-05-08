import discord
import os
import requests
import json
import random

client = discord.Client()

# First list of keywords, if matched trigger get request
greatest = ['greatest', 'Greatest', 'GREATEST', 'perfect', 'Perfect', 'PERFECT', 'highest', 'Highest', 'HIGHEST', 'crazy', 'Crazy', 'CRAZY', 'holy', 'Holy', 'HOLY', 'Kardashian', 'kardasdian', 'KARDASHIAN', 'Chicago', 'chicago', 'CHICAGO', 'West', 'west', 'WEST', 'North', 'north', 'Donda', 'donda', 'DONDA', 'Yeezy', "YEEZY", 'yeezy',
            'trump', 'Trump', 'TRUMP', 'KING', 'King', 'king', 'Grammy', 'grammy', 'Jesus', 'JESUS', 'jesus', 'Pablo', 'pablo', 'PABLO', 'MAGA', 'Maga', 'maga', 'SAINT', 'Saint', 'saint', 'race', 'RACE', 'Race', 'racist', 'Racist', 'RACIST', 'Slavery', 'slavery', 'SLAVERY',  'Yeezus', 'YEEZUS', 'yeezus',  'Taylor Swift', 'TAYLOR SWIFT', 'taylor swift']
  
# Second list of keywords, if match trigger get request
ye = ['ye', 'YE', 'Ye', 'ok', 'OK', 'Ok', 'New York', 'new york', 'NEW YORK', 'ny', 'NY', 'LA', 'impossible', 'IMPOSSIBLE',
      'Impossible', 'important', 'IMPORTANT', 'Important', 'great', 'Great', 'GREAT', 'best', 'Best', 'BEST', 'kanye', 'Kanye', 'KANYE']

def get_quote():
  # Get requests for a random Kanye quote
  response = requests.get("https://api.kanye.rest/")
  
  # JSON conversion to string
  json_data = json.loads(response.text)
  quote = json_data["quote"]
  return(quote)

@client.event
async def on_ready():
  # Output to console Kanye bot has logged on
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  # Don't read your own messages
  if message.author == client.user:
    return

  # Message's content
  msg = message.content

  # For testing, bot responds 100%
  if msg.startswith('$bruteforce'):
    quote = get_quote()
    await message.channel.send(quote)

  # First list of keywords to respond to
  if any(word in msg for word in greatest):
    # Bot responds 1/3 of the time to keywords
    rand_int = random.randint(0, 2)
    if rand_int == 2:
      # Sends quote
      quote = get_quote()
      await message.channel.send(quote)

  # Second list of keywords to respond to
  if any(word in msg for word in ye):
    # Bot respond 1/4 of the time to keywords
    rand_int = random.randint(0, 4)
    if rand_int == 2:
      # Sends quote
      quote = get_quote()
      await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
