import discord
import os
from dotenv import load_dotenv
import requests
import json
import random

client = discord.Client()
load_dotenv()

sad_words = ["lonely", "unhappy", "depressed", "sad", "alone", "anxious", "nervous", "miserable", "dejected", "hurt", "hopeless", "lonely",
              "heartbroken", "mournful", "troubled", "sick", "painful"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person! ", "Stay strong buddy!", "Accept yourself.", "Be awesome!",
                            "Chill out.", "Breathe deeply *sniffff*", "Be Yourself.", "Hold on.", "See the Good!"]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Please use $inspire to get inspired'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$online'):
    await message.channel.send("Akif's Bot has logged in successfully!")

  if msg.startswith('$source'):
    await message.channel.send('Here is the source code - ')
    await message.channel.send('https://github.com/akif-iqbal/inspiring-discord-bot')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.reply(quote, mention_author=True)

  if any(word in msg for word in sad_words):
    await message.reply(random.choice(starter_encouragements), mention_author=True)

client.run(os.getenv('TOKEN'))