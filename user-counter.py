# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys

# setup Bot
client = Bot(description="Weekly Challenge Judge by iggnore", command_prefix=">", pm_help = False)

@client.event
async def on_ready():
	
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

	print('--------')

	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

# Counts entries in #weekly-challenges
@client.event
async def on_message(message):
	if not message.content.startswith('>count'):
		return
	
	async for message in client.logs_from(message.channel):
		for attachment in message.attachments:
			if not attachment:
				continue

			print(message.author)
			print(attachment['url'])
			
			for reaction in message.reactions:
				if reaction.emoji == '❤':
					print(reaction.count)

			print('--')

	embed = discord.Embed(title="Weekly Challenge Results", description="Congratulations to our #weekly-challenge winner!", color=discord.Colour.blue())
	embed.add_field(name="Fist Place", value="Xenorra - {} votes".format(21), inline=True)
	embed.add_field(name="Second Place", value="iggnore - {} votes".format(20), inline=True)
	embed.add_field(name="Third Place", value="Malachaai - {} votes".format(10), inline=True)

	await client.send_message(message.channel, embed=embed)
client.run(str(sys.argv[1])) # Send API key via command line arguments
