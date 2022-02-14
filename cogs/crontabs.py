import discord
import aiocron
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import bot

class crontabs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    #CHANNEL_ID=**5712262****
    #valorant timer
    @aiocron.crontab('18,19,20 6 * * *') #9.30 9.45 = 0,15 16 * * *
    async def cornjob1():
        CHANNEL_ID=769571226213154816
        channel = bot.get_channel(CHANNEL_ID)
        valo1 = get(channel.guild.roles, name = 'Valo-Masters')
        await channel.send(f'{valo1.mention} Come into the unkown')

    #One Piece Timer
    @aiocron.crontab('17 13 * * *') # 30 4 * * SUN
    async def cornjob1(ctx:commands.Context):
        CHANNEL_ID=769571226213154816
        channel = bot.get_channel(CHANNEL_ID)
        anime = get(channel.guild.roles, name = 'Anime')
        await channel.send(f'{anime.mention} Miyou One Piece!', file=discord.File('images/op.gif'))
        
    #gm message timer
    @aiocron.crontab('30 3 * * *')
    async def cornjob1():
        CHANNEL_ID=769571226213154816
        channel = bot.get_channel(CHANNEL_ID)
        mem = get(channel.guild.roles, name = 'Valo-Masters')
        await channel.send(f'{mem.mention} Good Morning Beautiful People 😀')
        
def setup(bot):
    bot.add_cog(crontabs(bot))
