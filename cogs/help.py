import discord
from discord.ext import commands
from discord.ext import menus


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True, aliases=['hepl', 'h', 'commands', 'command', 'cmd', 'cmds'])
    async def help(self, ctx):
        #author = ctx.message.author

        em = discord.Embed(
            description='`{} : Optional | [] : Compulsary `', colour=discord.Colour.gold())
        em.set_author(name="केळ्या 🍌", icon_url=f"{ctx.bot.user.avatar_url}")
        em.add_field(
            name='Fun', value='`fun      ` : `.help fun`\n`games    ` : `.help games`\n`economy     ` : `.help ecnonomy`\n`music      ` : `.help music`\n`bot     ` : `.help bot`\n`admin        ` : `.help admin`\n`owner       ` : `.help owner`', inline=False)
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)

        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)
        # await ctx.send(f"{author.mention} check DM 🐷")

    @help.command()
    async def fun(self, ctx):
        em = discord.Embed(Description='Fun')
        em.add_field(
            name='Fun', value='`rank      ` : `.rank {member}`\n`avatar    ` : `.avatar {member}`\n`roast     ` : `.roast {member}`\n`bang      ` : `.bang [member]`\n`spank     ` : `.spank {member}`\n`pp        ` : `.pp {member}`\n`rip       ` : `.rip {member}`\n`weather   ` : `.weather [city_name]`\n`mention   ` : `.mention [member] {number 1-5} {message}`\n`status    ` : `.status [member]`\n`emoji     ` : `.emoji [emoji_name]`\n`.meme     ` `.nasa     ` `.whoami   ` `.mod       ` `.admin    `', inline=False)
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)

    @help.command()
    async def games(self, ctx):
        em = discord.Embed(Description='Games')
        em.add_field(
            name='Games', value='`.stats    ` : `.stats {member}`\n`.pokemon  ` `.guessno  ` `.slots    `', inline=False)
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)

    @help.command()
    async def economy(self, ctx):
        em = discord.Embed(Description='Games')
        em.add_field(
            name='Economy', value='`balance   ` : `.balance {member} | Aliases: bal, khata`\n`give      ` : `.give [member] [amount] | Aliases = send`\n`gamble    ` : `.gamble {amount}`\n`rob       ` : `.rob [member]`\n`beg       ` : `Aliases = bhik`\n`daily     `', inline=False)
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)

    @help.command()
    async def music(self, ctx):
        em = discord.Embed(Description='Games')
        em.add_field(
            name='Music', value='`play      ` : `.play [song_name]`\n`volume    ` : `.volume [0-100]`\n`seek      ` : `.seek [seconds(+/-)] `\n`loop      ` : `.loop {NONE/CURRENT/PLAYLIST}`\n`.skip     ` `.pause     ` `.resume   ` `.nowplaying` `.queue    ` `.eqalizer ` `.connect  ` `.disconnect`')
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)

    @help.command()
    async def bot(self, ctx):
        em = discord.Embed(Description='Bot Status')
        em.add_field(name='Bot status',
                     value='`.ping` `.uptime`', inline=False)
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)

    @help.command()
    async def admin(self, ctx):
        em = discord.Embed(Description='Admin')
        em.add_field(
            name='Admin ', value='`warn      ` : `.warn [member] {reason}`\n`kick      ` : `.kick [member] {reason}`\n`ban       ` : `.ban [member] {reason}`\n`unban     ` : `.unban [member_name#discrimantor]`\n`clear     ` : `.clear [message_count]`', inline=False)
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)

    @help.command()
    async def owner(self, ctx):
        em = discord.Embed(Description='Owner')
        em.add_field(
            name='Owner', value='`add_coin  ` : `.add_amt [member] [amount] | Aliases : givecoin`\n`rem_amt   ` : `.rem_amt [member] [amount] | Aliases: remcoin`\n`.reset    ` `.restart  `')
        em.add_field(
            name='IMP', value='Don\'t try commands in bot dm , they wont work since they are server specific', inline=False)
        em.set_footer(
            icon_url=f'{ctx.author.avatar_url}', text='पावर्ड बाय केळ')
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(help(bot))
