import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys
import requests
import os
import time
import uploader
from numpy import argsort

# setup Bot
client = Bot(description="Weekly Challenge Judge by iggnore", command_prefix=">", pm_help = False)

# open private key file
key_file = open('./discord_key.txt', 'r')
if not key_file:
	print('File discord_key.txt can\'t be found')
	sys.exit(0)

# read private key from file
api_key = key_file.read().splitlines()[0]
if not api_key:
	print('No API key in discord_key.txt')
	sys.exit(0)

# close private key file
key_file.close()

def downloadimgs(authors, urls):
	"""Download images from current challenge and save them as 
		'author.jpg' in '/images/dd-mm-yyyy/'"""
	dirname = time.strftime('%d-%m-%Y')
	os.mkdir('images/'+dirname)
	for i in range(len(authors)):
		f = open('./images/'+dirname+'/'+authors[i].name+'.jpg', 'wb')  #create file locally
		f.write(requests.get(urls[i]).content)  #write image content to this file 
		f.close()

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

	print('--------')
	
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

# Counts entries in #weekly-challenges
@client.event
async def on_message(message):
	authors	= [] 
	urls	= []
	votes	= []

	if not message.content.startswith('>count'):
		return
	
	announcement_channel = client.get_channel('306891494726303746')

	async for message in client.logs_from(message.channel):
		for attachment in message.attachments:
			if not attachment:
				continue

			authors.append(message.author)
			urls.append(attachment['url'])		
			
			contains_emoji = False
			for reaction in message.reactions:
				if reaction.emoji == '❤':
					votes.append(reaction.count)
					contains_emoji = True
					break

			if not contains_emoji:
				votes.append(0)

	indices = argsort(votes)

	first	= indices[-1]
	second  = indices[-2]
	third	= indices[-3]
	
	message = await client.send_message(message.channel, content='Downloading images...')
	downloadimgs(authors, urls) # download images from cdn.discordapp.com
	await client.delete_message(message)
	message = await client.send_message(message.channel, content='Downloads done.')
	await client.delete_message(message)
	message = await client.send_message(message.channel, content='Uploading images...')
	link = uploader.upload()	# upload images to Google Drive
	await client.delete_message(message)
	message = await client.send_message(message.channel, content='Uploads done.')
	await client.delete_message(message)
	message = await client.send_message(message.channel, content='Images available at {} !'.format(link))

	embed = discord.Embed(title="Weekly Challenge Results", description="Congratulations to our <#{}> winner!".format(message.channel.id), color=discord.Colour.blue())
	embed.add_field(name="First Place", value="<@!{}> - {}".format(authors[first].id, votes[first]), inline=True)
	embed.add_field(name="Second Place", value="<@!{}> - {}".format(authors[second].id, votes[second]), inline=True)
	embed.add_field(name="Third Place", value="<@!{}> - {}".format(authors[third].id, votes[third]), inline=True)
	embed.set_footer(text='Thank you for all your entries! The next weekly challenge will be announced shortly.')

	# make a small announcement in the current channel
	await client.send_message(message.channel, content='Results posted in <#{}>!'.format(announcement_channel.id))
	
	# send a PM to the winner
	await client.send_message(authors[first], content='Hey {} - congratulations! You\'re the winner of this week\'s weekly challenge! A mod will DM you shortly with your prize.'.format(authors[first].name))

	# make rich embedded announcement in the server's announcement channel
	await client.send_message(announcement_channel, embed=embed)

client.run(str(api_key)) # Send API key from opened file
