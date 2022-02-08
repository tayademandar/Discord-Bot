import discord,requests
from discord.ext import commands

class webhook(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
@commands.Cog.listener()
async def on_message(self,ctx,member :discord.member, message: discord.Message):
    if message.author.bot is True or message.guild is None:
        return
    for i in commands.guilds:
        emoji = discord.utils.get(i.emojis)
        emojiname = []
        emojilist=emojiname.append(emoji)
     
    member = ctx.author   
    if message.content in emojilist:
        pfp = requests.get(member.avatar_url_as(format = "png",size = 256)).content
  
        hook = await ctx.channel.create_webhook(name = member.display_name,avatar = pfp)
  
        await hook.send(message)
        await hook.delete()
        await ctx.message.delete()
def setup(bot):
    bot.add_cog(webhook(bot))