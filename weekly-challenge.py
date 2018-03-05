# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys
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
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

	print('--------')
	
	
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

# Counts entries in #weekly-challenges
@client.event
async def on_message(message):
	authors    = [] 
	urls	   = []
	votes	   = []

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

	one   = indices[-1]
	two   = indices[-2]
	three = indices[-3]

	embed = discord.Embed(title="Weekly Challenge Results", description="Congratulations to our <#{}> winner!".format(message.channel.id), color=discord.Colour.blue())
	embed.add_field(name="First Place", value="<@!{}> - {}".format(authors[one].id, votes[one]), inline=True)
	embed.add_field(name="Second Place", value="<@!{}> - {}".format(authors[two].id, votes[two]), inline=True)
	embed.add_field(name="Third Place", value="<@!{}> - {}".format(authors[three].id, votes[three]), inline=True)
	embed.set_footer(text='Thank you for all your entries! The next weekly challenge will be announced shortly.')

	# make a small announcement in the current channel
	await client.send_message(message.channel, content='Results posted in <#{}>!'.format(announcement_channel.id))
	
	# send a PM to the winner
	await client.send_message(authors[one], content='Hey {} - congratulations! You\'re the winner of this week\'s weekly challenge! A mod will DM you shortly with your prize.'.format(authors[one].name))

	# make rich embedded announcement in the server's announcement channel
	await client.send_message(announcement_channel, embed=embed)

client.run(str(api_key[0])) # Send API key from opened file
