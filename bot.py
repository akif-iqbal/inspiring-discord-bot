import discord
import os
from dotenv import load_dotenv
import requests
import json
import random

client = discord.Client()
load_dotenv()

sad_words = ["lonely", "unhappy", "depressed", "sad", "alone", "anxious", "nervous", "miserable"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person! ", "Stay strong buddy!"]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))