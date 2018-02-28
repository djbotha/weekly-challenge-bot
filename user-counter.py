# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import pprint
import sys

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="user-counter by iggnore", command_prefix=">", pm_help = False)
serverid = 411402280060059648
max_message_length = 1980

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	buff = '\0'
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

	print('--------')

	output_names = open("./sag_names.txt", "w");
	output_mentions = open("./sag_mentions.txt", "w");
	

	for s in client.servers:
		if int(s.id) == 306878380777799682:
			await asyncio.sleep(3)
			
			users = 0;
			messages = 0;	
			for member in s.members:
				if not member.bot:
					if (len(buff)+len(member.display_name)+2) >= max_message_length:
						output_mentions.write(buff)
						output_mentions.write('\n\n')
						buff = ''
						messages += 1

					users += 1
					buff += member.mention + ' '
					output_names.write(member.display_name + '\n')



	print('{} {}'.format(users, messages))
	output_names.close()
	output_mentions.close()

	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

client.run(sys.argv[1])

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
