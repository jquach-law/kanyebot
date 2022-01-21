import discord
import os
import requests
import json
from keep_alive import keep_alive
import random

client = discord.Client()

# First list of keywords, if matched trigger get request
greatest = ['a', 'list', 'of', 'keywords']
  
# Second list of keywords, if match trigger get request
ye = ['a', 'different', 'list', 'of', 'keywords']

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

  # Bot responds 100% to message: '$bruteforce'
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

keep_alive()
client.run(os.getenv('TOKEN'))
