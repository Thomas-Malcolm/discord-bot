import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

import base64


load_dotenv()

API_KEY = os.getenv('DISCORD_TOKEN')
SERVER_NAME = os.getenv('DISCORD_GUILD')

mrRobot = commands.Bot(command_prefix='!')


@mrRobot.event
async def on_ready():

	guild = mrRobot.guilds[0]
	memberCount = len(guild.members)
	onlineMemberCount = len([mem for mem in guild.members if mem.status == discord.Status.online])

	print(f'{mrRobot.user} is connected to: {guild.name}')
	print(f'There are {onlineMemberCount} of {memberCount} people online!')

	await mrRobot.change_presence(activity=discord.Game('.help'))



@mrRobot.command(name='test')
async def test_command(ctx):
	response = "This is a test message. :hellothere:"

	await ctx.send(response)


for filename in os.listdir('./commands'):
	if filename.endswith('.py'):
		mrRobot.load_extension(f'commands.{filename[:-3]}')


mrRobot.run(API_KEY)