import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType
import discord
import aiocron
import asyncio
import random
import time
import os
import requests
import json
import datetime
import sys
from discord.ext import commands
from discord.utils import get
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from dotenv import load_dotenv
from prsaw import RandomStuff
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle
import DiscordUtils
#from itertools import cycle

from discord_buttons_plugin import *

load_dotenv()
intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix=".",
                      case_insensitive=True, intents=intents)
api_key = "Q*ht***"
rs = RandomStuff(async_mode=True, api_key=api_key)  # for ai
client.remove_command('help')

client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'
    }
]
#status = cycle(['viraj',' l***','hehe', 'hoo hoo'])
# startup


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('केळ 🍌 | .help'))
    # change_status.start()
    print("client is ready")
    global startTime
    startTime = time.time()
    client.load_extension('dismusic')

    DiscordComponents(client)

# changing status
# @tasks.loop(seconds=2)
# async def change_status():
#   await client.change_presence(activity=discord.Game(next(status)))

# Cogs
for ext in ('levelling', 'help', 'webhooks'):
    client.load_extension(f'cogs.{ext}')

# ping command


@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

# uptime


@client.command(aliases=['up'])
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f"Bot uptime: {uptime}")

# hello command


@client.command()
async def hello(ctx):
    await ctx.send("हे घे केळ खा 🍌")

# admin command


@client.command()
async def admin(ctx):
    # guild.roles or guild.members
    Admin = get(ctx.guild.roles, name='Admin 👑')
    message1 = await ctx.send(f"{Admin.mention} ला ***** नाही <:CringeHarold:826485005089505331> ")
    await message1.add_reaction("<:banana_emote:870308280432488599>")

# mod command


@client.command()
async def mod(ctx):
    mod = get(ctx.guild.roles, name='Moderator 🛡')
    await ctx.send(f"{mod.mention} ****", file=discord.File('images/***.jpg'))

# valorant command


@client.command(aliases=['v', 'valorant'])
async def valo(ctx, member: discord.Member = None):
    if member is None:
        valo = get(ctx.guild.roles, name='Valo-Masters')
        await ctx.send(f"{valo.mention} या मित्रांनो, खेळूया")
    else:
        with open("lists/valo.txt", "r") as f:
            valo = f.readlines()
            msg = random.choice(valo)
            await ctx.send(f'{member.mention} { msg}')

# donate


@client.command()
async def donate(ctx):
    await ctx.send('Here is my Bitcoin address: 1AX1GBzvpxsh14rWVY1nf8wEJWkREVkeVy, Scan the QR:', file=discord.File('images/btc.jpeg'))

# Scheduled message
CHANNEL_ID = 76957****1*15*816

# valorant timer


@aiocron.crontab('0,15 16 * * *')  # 9.30 9.45 = 0,15 16 * * *
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID)
    valo1 = get(channel.guild.roles, name='Valo-Masters')
    await channel.send(f'{valo1.mention} Come into the unkown')

# One Piece Timer


@aiocron.crontab('30 4 * * SUN')
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID)
    anime = get(channel.guild.roles, name='Anime')
    await channel.send(f'{anime.mention} Miyou One Piece!', file=discord.File('images/op.gif'))

# gm message timer


@aiocron.crontab('30 3 * * *')
async def cornjob1():
    channel = client.get_channel(CHANNEL_ID)
    mem = get(channel.guild.roles, name='Valo-Masters')
    await channel.send(f'{mem.mention} Good Morning Beautiful People 😀')


# bot replies

@client.event
async def on_message(message):

    await client.process_commands(message)
    if message.author.bot is True:
        return
    elif message.content == "kelya":
        # await message.reply(message.author.mention +' तु******👋')
        await message.channel.send('तु*****👋')
    elif message.content == "hello":
        words = ['Sup B*tch ', 'Hi', 'Hello', 'Keep that pillow talk to yourself',
                 'Sorry babe i\'m going to bed', 'The Discord gods say hello 👋']

        msg = random.choice(words)
        # await message.reply(message.author.mention + " " +msg)
        await message.channel.send(msg)

    elif "mhanje" in message.content:
        await message.channel.send('waghache panje 🐾')
    elif "kay" in message.content:
        await message.channel.send('kahi nahi')
    elif "noob" in message.content:
        await message.channel.send('pappa ko bol')
    elif "yedi g***d" in message.content:
        await message.channel.send("Pakistan")
    elif message.content.lower() == 'f':
        await message.channel.send('f')
    elif "lol" in message.content.lower():
        await message.channel.send('lol')
    elif client.user.mentioned_in(message) and 'prefix' in message.content:
        await message.channel.send(f'My Prefix is `{client.command_prefix}`')
    elif message.channel.id == 868079083915989022:
        response = await rs.get_ai_response(message.content)
        await message.reply(response[0]['message'])

# who am i


@client.command()
async def whoami(ctx):
    await ctx.send(f'You are {ctx.message.author.mention}')

# bang


@client.command()
async def bang(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send('Mention who you want to bang dum**ck🤡')
    else:
        await ctx.send(f"{member.mention} you were banged hard by {ctx.message.author.mention} ")

# pp command


@client.command(pass_context=True)
async def pp(ctx, member: discord.Member = None):
    len = random.randint(0, 100)
    dep = random.randint(0, 100)
    len1 = '='
    len2 = round(len/2)  # round length
    # embed
    embed = discord.Embed(colour=discord.Colour.gold())
   # 40 line omitted


# wait for user reply
@client.command()
async def test(ctx):
    await ctx.send('Say boo')

    def check(m):
        return m.content == 'boo'
    msg = await client.wait_for('message', check=check)
    await ctx.send('boo right back at ya {.author.name}!'.format(msg))

# rip imgae manipulation


@client.command()
async def rip(ctx, member: discord.Member = None):
    if member is None:
        member = ctx. author

    rip = Image.open("images/rip.png")
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    draw = ImageDraw.Draw(rip)
    # font = ImageFont.truetype(r"fonts/28.ttf", 16) # font = ImageFont.truetype(<font-file>, <font-size>)
    # draw.text((0, 0),"IDK - 2021",(255,255,255),font=font) # draw.text((x, y),"Sample Text",(r,g,b))
    pfp = pfp.resize((165, 150))  # resolution of user pfp
    rip.paste(pfp, (137, 285))  # cordinates of upper left corner
    rip.save("images/output.png")
    await ctx.send(file=discord.File("images/output.png"))

# spank


@client.command()
async def spank(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
        #asset1 = bot.user.avatar_url(size =256)

    spank = Image.open("images/spank.png")
    spank = spank.convert("RGB")
    asset = member.avatar_url_as(size=256)
    asset1 = ctx.author.avatar_url_as(size=256)
    data = BytesIO(await asset.read())
    data1 = BytesIO(await asset1.read())
    pfp = Image.open(data)
    #pfp = Image.convert("RBG")
    pfp1 = Image.open(data1)
    pfp = pfp.resize((70, 70))
    pfp1 = pfp1.resize((70, 70))  # resolution of user pfp
    spank.paste(pfp, (46, 41))  # cordinates of upper left corner
    spank.paste(pfp1, (299, 53))
    spank.save("images/output1.png")
    await ctx.send(file=discord.File("images/output1.png"))

# purge


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    if amount > 50:
        await ctx.send('Purging')
    await ctx.channel.purge(limit=amount+2)
    #print (f'{amount} message deleted')
    await ctx.send(f'**Messages deleted:** {amount} \n**Initiated by:** {ctx.message.author.name} ', delete_after=2)

# status


@client.command(name='status')
async def status(ctx, member: discord.Member = None):
    await ctx.send(f'**{member.name}** is {str(member.status)}')

# roast command


@client.command()
async def roast(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    with open("lists/roast.txt", "r") as f:
        roasts = f.readlines()
        # print(roasts)
        msg = random.choice(roasts)
        await ctx.send(f'`{member.name}` {msg}')


# reddit memes
@client.command()
async def meme(ctx):
    r = requests.get("https://memes.blademaker.tv/api?lang=en")
    res = r.json()
    title = res['title']
    ups = res['ups']
    sub = res['subreddit']
    em = discord.Embed(title=f"{title}", colour=discord.Colour.gold())
    em.set_image(url=res['image'])
    em.set_footer(text=f"👍 {ups} | r/{sub}")
    await ctx.send(embed=em)

# weather command


@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(aliases=['w'])
async def weather(ctx, city_name=None):
    api_key = "*****"
    # api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API key}
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    #complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    #print(complete_url, city_name)
    x = response.json()
    # print(x)
    if city_name is None:
        await ctx.send('Enter city name dummy')
    elif x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        a = x["wind"]
        current_temperature = y["temp"]
        current_humidity = y["humidity"]
        wind_speed = a["speed"]
        weather_description = z[0]["description"]
        icon = z[0]["icon"]
        em = discord.Embed(colour=discord.Colour.gold())
        em.set_author(name=f"Weather Data of {(city_name).capitalize()}")
        em.set_thumbnail(url=f"http://openweathermap.org/img/wn/{icon}@2x.png")
        em.add_field(name='Temperature',
                     value=f"{round((float(current_temperature) -273.15), 2)} °C", inline=False)
        em.add_field(name='Humidity',
                     value=f"{str(current_humidity)} %", inline=True)
        em.add_field(name="‎‎‏‏‎ ‎", value="‏‏‎ ‎", inline=True)
        em.add_field(name='Wind', value=f"{str(wind_speed)} m/s", inline=True)
        em.add_field(name='Description', value=str(
            weather_description).capitalize(), inline=False)
        em.set_footer(text="पावर्ड बाय केळ")
        await ctx.send(embed=em)
    else:
        await ctx.send("City ille")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):  # checks if on cooldown
        msg = 'Slow it down bullya, try again in `{:,.2f}s`'.format(
            error.retry_after)  # says the time
        await ctx.send(msg, delete_after=2)

 # member special access


def special(ctx):
    return ctx.message.author.id == 6542***0250, 592912*****1803

# reset cooldown


@client.command()
# @commands.is_owner()
@commands.check(special)
async def reset(ctx):
    weather.reset_cooldown(ctx)
    slots.reset_cooldown(ctx)
    gamble.reset_cooldown(ctx)
    # daily.reset_cooldown(ctx)
    mention.reset_cooldown(ctx)
    rob.reset_cooldown(ctx)
    beg.reset_cooldown(ctx)
    await ctx.send("cooldown reset!", delete_after=2)


# kick
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason="Bullya Admin didn't provide a reason"):

    em = discord.Embed(
        description=f"***✅ {member.name} has been kicked: {reason}***", colour=discord.Colour.gold())
    em1 = discord.Embed(
        description=f"*** {member.name}, You have been kicked: {reason}***", colour=discord.Colour.gold())
    await member.send(embed=em1)
    await ctx.send(embed=em)
    await member.kick(reason=reason)
# ban


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason="** Admin didn't provide a reason"):
    em = discord.Embed(
        description=f"***✅ {member.name} has been banned\n {reason}***", colour=discord.Colour.gold())
    em1 = discord.Embed(
        description=f"*** {member.name}, You have been banned from: {reason}***", colour=discord.Colour.gold())
    await ctx.send(embed=em)
    await member.send(embed=em1)
    await member.ban(reason=reason)
# warn


@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, *, reason="Aise hi **y laga"):
    em = discord.Embed(
        description=f"***✅ {member.name} has been warned***", colour=discord.Colour.gold())
    em1 = discord.Embed(
        description=f"*** {member.name}, You have been warned: {reason}***", colour=discord.Colour.gold())
    await member.send(embed=em1)
    await ctx.send(embed=em)

# unban


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Ban revoked for {user.name}#{user.dicriminator}')
            return

# lock channel


@commands.has_permissions(administrator=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')

# common emjoi
party = '<a:party:875640035871981638>'  # for mega,slots
party1 = '<a:party1:877271922608570389>'  # for normal,slots
banana = '<:banana_emote:870308280432488599>'  # for slots
pop = '<a:pop:869952173826514954>'  # for slots
shake = '<a:shake:871048759390392320>'  # for slots
kelacoin = '<:kelacoin:877438366902255636>'  # kela coins


# pokemon game
@client.command(aliases=['poke'])
async def pokemon(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    with open("lists/pokemon.txt", "r") as f:
        word_list = f.readlines()

    word = random.choice(word_list).lower()
    new_list = list(word)
    length = len(word) - 1
    new_list.pop(-1)
    new_word = ''.join(new_list)
    # print(new_word)

    for x in range(length-4):
        rand_index = random.randint(0, len(word)-1)
        new_list[rand_index] = " _ "

    final = ' '.join(new_list)

    message = await ctx.reply(f'<:awww:780652069526831115> Guess the Pokémon. <a:countdown:875601161779040296>\n\n`{final}` ')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await client.wait_for('message', check=check, timeout=10)
        if msg.content.lower() == new_word:
            earnings = random.randrange(1000, 5000)
            poke_win = 1
            users[str(user.id)]["poke_win"] += poke_win
            users[str(user.id)]["bank"] += earnings
            await ctx.send(f'<a:tick:872141719074902046> You Guessed it right. You won **{earnings:,}** {kelacoin}')
        else:
            poke_lose = 1
            users[str(user.id)]["poke_lose"] += poke_lose
            await msg.reply(f'<a:cross:872140912594141234> Incorrect, Correct answer is `{new_word}`')
    except asyncio.TimeoutError:
        await message.edit(content=f'<:wrong:872119314709381160> Timeout, the anwers was `{new_word}`')

    with open("bank.json", 'w') as f:
        json.dump(users, f)

# email generator


@client.command()
async def creds(ctx, member: discord.Member = None):
    with open("lists/10m.txt", "r") as f:
        word_list = f.readlines()

    word = random.choice(word_list)
    num = random.randint(0, 1000)
    domain_list = ['xnxt.com', 'phub.com', 'gtail.com', 'kelya.com', 's**ymail.com',
                   'kelya.co.in', 'milkmail.eu', 'me.co.in', 'ggwp.org', 'kalaanamail.com']
    domain = random.choice(domain_list)
    await ctx.send(f'Email:`{member.name}{num}@{domain}`\nPassword: `{word}`')

# slots


@commands.cooldown(1, 15, commands.BucketType.user)
@client.command()
async def slots(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    emojis = [banana, pop, shake]
    message = f'{banana} | {pop} | {shake}'
    em = discord.Embed(description=message, colour=discord.Colour.gold())

    message_new = await ctx.reply(embed=em)

    for x in range(5):
        rand = random.choices(emojis, k=3)
        new_em = discord.Embed(
            description=f'{rand[0]} | {rand[1]} | {rand[2]}', colour=discord.Colour.gold())
        await message_new.edit(embed=new_em)

    if rand[0] == rand[1] == rand[2]:
        if rand[0] == rand[1] == rand[2] == banana:
            earnings = random.randrange(50000, 100000)
            mega_count = 1
            await ctx.reply(f'✨ Mega Jackpot {party}. You won **{earnings:,}** {kelacoin} ')
            users[str(user.id)]["bank"] += earnings
            users[str(user.id)]["slots_mega"] += mega_count
        else:
            earnings = random.randrange(10000, 50000)
            jack_count = 1
            await ctx.reply(f"{party1} Jackpot. You won **{earnings:,}** {kelacoin}")
            users[str(user.id)]["bank"] += earnings
            users[str(user.id)]["slots_jackpot"] += jack_count
    elif rand[0] == rand[1] or rand[1] == rand[2] or rand[0] == rand[2]:
        earnings = random.randrange(10, 3000)
        win_count = 1
        await ctx.reply(f"{party1} You won **{earnings:,}** {kelacoin}")
        users[str(user.id)]["bank"] += earnings
        users[str(user.id)]["slots_wins"] += win_count
    else:
        earnings = 0
        lose_count = 1
        users[str(user.id)]["bank"] += earnings
        users[str(user.id)]["slots_lose"] += lose_count
        await ctx.reply("You lost")

    with open("bank.json", 'w') as f:
        json.dump(users, f)


# coin flip
@client.command(aliases=['toss', 'coinflip'])
async def flip(ctx):
    await ctx.send(random.choice(['Heads', 'Tails']))

# Economy system
# open account,update account,helper functions


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["slots_mega"] = 0
        users[str(user.id)]["slots_jackpot"] = 0
        users[str(user.id)]["slots_wins"] = 0
        users[str(user.id)]["slots_lose"] = 0
        users[str(user.id)]["poke_win"] = 0
        users[str(user.id)]["poke_lose"] = 0
        users[str(user.id)]["guess_win"] = 0
        users[str(user.id)]["guess_lose"] = 0
        users[str(user.id)]["gamble_win"] = 0
        users[str(user.id)]["gamble_draw"] = 0
        users[str(user.id)]["gamble_lose"] = 0

    with open("bank.json", 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("bank.json", 'r') as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="bank"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", "w") as f:
        json.dump(users, f)
    bal = [users[str(user.id)]["bank"]]

    return bal

# stats command


@client.command()
async def stats(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await open_account(member)
    user = member
    users = await get_bank_data()
    mega = users[str(user.id)]["slots_mega"]
    jack = users[str(user.id)]["slots_jackpot"]
    win = users[str(user.id)]["slots_wins"]
    lose = users[str(user.id)]["slots_lose"]
    poke_win = users[str(user.id)]["poke_win"]
    poke_lose = users[str(user.id)]["poke_lose"]
    guess_win = users[str(user.id)]["guess_win"]
    guess_lose = users[str(user.id)]["guess_lose"]
    gamble_win = users[str(user.id)]["gamble_win"]
    gamble_draw = users[str(user.id)]["gamble_draw"]
    gamble_lose = users[str(user.id)]["gamble_lose"]

    em = discord.Embed(title=f"{member.name}'s Slot Stats.",
                       color=discord.Color.gold())  # 0x36393F
    em.set_thumbnail(url=f'{member.avatar_url}')
    em.add_field(
        name="Slots", value=f"Mega Jackpots : **{mega}**\nJackpots: **{jack}**\nWins: **{win}**\nLost: **{lose}**")
    em.add_field(name="Pokemon Game",
                 value=f"Wins : **{poke_win}**\nLost: **{poke_lose}**", inline=False)
    em.add_field(name="Guess Number",
                 value=f"Wins : **{guess_win}**\nLost: **{guess_lose}**", inline=False)
    em.add_field(
        name="Gamble", value=f"Wins : **{gamble_win}**\nDraw: **{gamble_draw}\n**Lost: **{gamble_lose}**", inline=False)

    await ctx.send(embed=em)

# balance


@client.command(aliases=['bal', 'khata'])
async def balance(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    await open_account(member)

    user = member

    users = await get_bank_data()

    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(
        title=f"{member.name}'s Balance.", color=discord.Color.gold())
    em.set_thumbnail(url=f'{member.avatar_url}')

    em.add_field(name="Bank:", value=f'**{bank_amt:,}** {kelacoin}')
    await ctx.send(embed=em)


# give
@client.command(aliases=['give'])
async def send(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(ctx.author)

    if amount == None:
        await ctx.send("Enter amount")
        return
    if amount.lower() == 'all':
        amount = bal[0]
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("You dont have that much money")
        return
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    await update_bank(ctx.author, -1*amount, "bank")
    await update_bank(member, amount, "bank")
    await ctx.send(f"You gave **{amount:,}** {kelacoin} to {member.name}")


# beg
@commands.cooldown(1, 60, commands.BucketType.user)
@client.command(aliases=['bhik'])
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(2001)

    await ctx.send(f"Take this Bhikarchot: **{earnings:,}** {kelacoin}")

    users[str(user.id)]["bank"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f)

# daily


@commands.cooldown(1, 86400, commands.BucketType.user)
@client.command()
async def daily(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(10000, 40000)

    await ctx.send(f"Here is your daily reward: **{earnings:,}** {kelacoin}")

    users[str(user.id)]["bank"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f)


# add coins to accounts
@client.command(aliases=['givecoin'])
@commands.is_owner()
async def add_amt(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Enter amount")
        return
    amount = int(amount)
    if amount < 0:
        await ctx.send("Amount must be positive")
        return

    await update_bank(member, amount, "bank")
    await ctx.send(f"You gave **{amount:,}** {kelacoin} to {member.name}")

# remove coins from users


@client.command(aliases=['remcoin'])
@commands.is_owner()
async def rem_amt(ctx, member: discord.Member, amount=None):
    await open_account(member)
    bal = await update_bank(member)
    if amount == None:
        await ctx.send("Enter amount")
        return
    if amount.lower() == 'all':
        amount = bal[0]
    bal = await update_bank(member)
    amount = int(amount)
    if amount < 0:
        await ctx.send("Amount must be positive")
        return
    elif amount > bal[0]:
        await ctx.send("User does not have that much money in their acc")
        return
    # await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member, -1*amount, "bank")
    await ctx.send(f"You removed **{amount:,}** {kelacoin} from **{member.name}**")


# #emoji command
# @client.command(aliases = ['e'])
# async def emoji(ctx, emoji_name):
#     emoji = {"pop" : "<a:pop:869952173826514954>", "pika" : "<a:pikachu:784722270127915030>","dance" : "<a:peped:868039743580012585>","cog" : "",
#             "ash" : "<a:Ash:853589520456482817>", "tick" : "<a:tick:872141719074902046>", "cross" : "<a:crossno:816542621333848084>",
#             "pp":"<a:3607pepesausage:849169211245985842>","gun":"<a:6387pepeguns:849169210268975144>","roll":"<a:1184pikachuroll:849169209141231676>",
#             "vc":"<a:4678joinvc:849162388170080297>","punch":"<a:9046pepepunch:849168017161977887>","hello":"<a:Pikachu_Hello:849169213235134495>",
#             "blob":"<a:8190ablobpainpats:849169209745211422>","sorry":"<a:6261pepesorry:849169209324732416>","bruh":"<a:2801bruh:849169209502335016>",
#             "angry":"<a:3741angrypaimon:849169209261817856>","shake":"<a:shake:871048759390392320>","doge":"<a:8806dogepartyvibrate:849169212316319765>",
#             "yay":"<a:yay:868049083468742676>",}
#     if emoji_name == "list":
#       await ctx.send("1.pop\n2.pika\n3.dance\n4.cog\n5.ash\n6.tick\n7.cross\n8.pp\n9.gun\n10.roll\n11.vc\n12.punch\n13.hello\n14.blob\n15.sorry\n16.bruh\n17.angry\n18.shake\n19.doge\n20.yay")
#     elif emoji_name in emoji:
#       x = emoji.get(emoji_name)
#       await ctx.channel.purge(limit = 1)
#       await ctx.send(x)
#       return
#     else:
#       await ctx.send("No such emoji")

# recation to a messgae id
@client.command(aliases=['r'])
async def react(ctx, msgID: int):
    msg = await ctx.fetch_message(msgID)
    await ctx.channel.purge(limit=1)
    # emojis = ['<a:pop:869952173826514954>','<a:pikachu:784722270127915030>','<a:peped:868039743580012585>','<a:Ash:853589520456482817>','<a:tick:872141719074902046>',
    #         '<a:crossno:816542621333848084>','<a:3607pepesausage:849169211245985842>','<a:1184pikachuroll:849169209141231676>','<a:4678joinvc:849162388170080297>',
    #           '<a:9046pepepunch:849168017161977887>','<a:Pikachu_Hello:849169213235134495>','<a:8190ablobpainpats:849169209745211422>','<a:8190ablobpainpats:849169209745211422>']
    emojis = ['🎈', '🎇', '🎃', '🧨', '🎁', '🎊', '🛒', '🎀', '👓',
              '🎱', '🧶', '♠', '♥', '📢', '📈', '🔒', '📞', '🦺', '🍕', '🥪']
    for i in range(20):
        await msg.add_reaction(emojis[i])

# avatar


@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author
    em = discord.Embed(colour=discord.Colour.gold())
    em.set_image(url=member.avatar_url_as(size=128))
    await ctx.send(embed=em)

# emoji


@client.command(aliases=['e'])
async def emoji(ctx, emojiname, num=None):
    if num is None:
        num = 1
    for i in client.guilds:
        emoji = discord.utils.get(i.emojis, name=emojiname)
    for x in range(num):
        await ctx.channel.purge(limit=1)
        await ctx.send(emoji)

# getemojiid


@client.command()
async def id(ctx, emojiname):

    for i in client.guilds:
        emoji = discord.utils.get(i.emojis, name=emojiname)

    await ctx.channel.purge(limit=1)
    await ctx.send(f'ID : \{emoji}')


# mention
@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def mention(ctx, member: discord.Member = None, x=1, *, msg=''):
    if x >= 6:
        await ctx.send('Limit is 5')
        return
    if member is None:
        await ctx.send('Mention a member dummy, **Usage**: `.member @member number message(optional)`')
    for i in range(x):
        await ctx.send(f'{member.mention} **{msg} **')

# number guess


@client.command()
async def guessno(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    message = await ctx.reply(f"I am guessing a number between **1** and **15**. Guess what number I have in my mind.")
    my_num = random.randrange(1, 15)
    print(my_num)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await client.wait_for('message', check=check)

        # print(f'msg:{msg.content},type:{type(msg.content)}')

        if int(msg.content) > 15 or int(msg.content) < 1:
            await msg.reply(f"You chose a number out of range or that's not a number, You lost.")
        else:
            if msg.content == str(my_num):
                earnings = random.randrange(1000, 2000)
                guess_win = 1
                users[str(user.id)]["guess_win"] += guess_win
                em = discord.Embed(
                    description=f"I chose **`{my_num}`**ㅤㅤㅤㅤㅤㅤYou chose **`{msg.content}`**\n\n You Won, Added **{earnings:,}** to you bank", colour=discord.Colour.gold())
                await msg.reply(embed=em)
                #print(f'You won, added **{earnings}** {kelacoin:,} to you bank')
            else:
                em1 = discord.Embed(
                    description=f"I chose **`{my_num}`**ㅤㅤㅤㅤㅤYou chose **`{msg.content}`**\n\n You Lost.", colour=discord.Colour.gold())
                await msg.reply(embed=em1)
                #print("You lost")
                earnings = 0
                guess_lose = 1
                users[str(user.id)]["guess_lose"] += guess_lose

            users[str(user.id)]["bank"] += earnings

            with open("bank.json", 'w') as f:
                json.dump(users, f)
    finally:
        return

# smoke


@client.command()
@commands.is_owner()
async def smoke(ctx):
    smoke = ['Weed', 'Cigarate', 'Cigar']
    roll = random.choice([0, 1])
    actions = ['fell in a pothole', 'slipped into you **** house']
    earnings = random.randrange(1000, 4000)
    if roll == 0:
        await ctx.send(f'You smoke some {random.choice(smoke)} and {random.choice(actions)}')
    else:
        await ctx.send(f'You smoke some {random.choice(smoke)} and {random.choice(actions)} and found {earnings} Kela coins')

# gamble


@commands.cooldown(1, 15, commands.BucketType.user)
@client.command()
async def gamble(ctx, amount=None):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    bal = await update_bank(ctx.author)

    per = random.randrange(40, 150)
    my_num = random.randrange(1, 11)
    user_num = random.randrange(1, 11)
    if amount is None:
        amount = 1
    if amount.lower() == 'all':
        amount = bal[0]

    amount = int(amount)
    if amount > 0:
        if amount <= bal[0]:
            if my_num < user_num:
                gamble_win = 1
                earnings = round((per/100)*amount)
                em = discord.Embed(
                    description=f"\nWin Percentage: **{per}%**\nAmount won: **{earnings:,} {kelacoin}**\nㅤ", colour=discord.Colour.green())
                em.set_author(name="Gamble Result : Win",
                              icon_url=f"{user.avatar_url}")
                em.add_field(name=f"केळ्या", value=f"**{my_num}**")
                em.add_field(name=f"{ctx.author.name}",
                             value=f"**{user_num}**")
                await ctx.send(embed=em)
                users[str(user.id)]["bank"] += earnings
                users[str(user.id)]["gamble_win"] += gamble_win
            elif my_num == user_num:
                gamble_draw = 1
                em = discord.Embed(
                    description=f"\nWin Percentage: **0%**\nAmount won: **0** {kelacoin}\nㅤ", colour=discord.Colour.gold())
                em.set_author(name="Gamble Result: Draw",
                              icon_url=f"{user.avatar_url}")
                em.add_field(name=f"केळ्या", value=f"**{my_num}**")
                em.add_field(name=f"{ctx.author.name}",
                             value=f"**{user_num}**")
                await ctx.send(embed=em)
                users[str(user.id)]["gamble_draw"] += gamble_draw
            else:
                gamble_lose = 1
                em = discord.Embed(
                    description=f"\nAmount Lost: **{amount:,} {kelacoin}**\nㅤ", colour=discord.Colour.red())
                em.set_author(name="Gamble Result: Lost",
                              icon_url=f"{user.avatar_url}")
                em.add_field(name=f"केळ्या", value=f"**{my_num}**")
                em.add_field(name=f"{ctx.author.name}",
                             value=f"**{user_num}**")
                await ctx.send(embed=em)
                users[str(user.id)]["bank"] -= amount
                users[str(user.id)]["gamble_lose"] += gamble_lose
        else:
            await ctx.reply(f'Insufficient bal. Your bank balance is **`{bal[0]:,}`** {kelacoin}')
    else:
        await ctx.send("Amount cannot be negative")

    with open("bank.json", 'w') as f:
        json.dump(users, f)


@client.command()
# @commands.cooldown(1,130, commands.BucketType.user)
async def rob(ctx, member: discord.Member = None):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)
    bal1 = await update_bank(ctx.author)
    rob_prob = random.choice([0, 1, 2, 3])  # random.randrange(0,5)
    print(rob_prob)
    if member is None:
        await ctx.reply('Mention a user b**ya')

    if bal1[0] < 10000:
        await ctx.reply(f"You must have atleast **10,000** {kelacoin} in your bank")
        return
    if bal[0] < 10000:
        await ctx.reply(f'You cannot steal from **{member.name}**. Their Balance is less than **10,000** {kelacoin}')
        return
    if rob_prob == 0:

        rob_amt = random.randrange(0, bal[0])
        await ctx.reply(f'You stole **{rob_amt:,}** {kelacoin} from **{member.name}**')
        await update_bank(ctx.author, rob_amt, "bank")
        await update_bank(member, -1*rob_amt, "bank")
    elif rob_prob == 1:
        fine = random.randrange(0, (bal1[0]/3))
        await ctx.reply(f"You were sent to h**ny jail and paid a fine of  **{fine:,}** {kelacoin} to **{member.name}**")
        await update_bank(ctx.author, -1*fine, "bank")
        await update_bank(member, fine, "bank")
        # return
    elif rob_prob == 2:
        paid = random.randrange(0, (bal1[0]/2))
        await ctx.reply(f"You paid **{member.name}** **{paid:,}** {kelacoin}")
        await update_bank(ctx.author, -1*paid, "bank")
        await update_bank(member, paid, "bank")
        # return
    else:
        await ctx.reply("Robbery unsuccessful")

# nasa


@client.command()
async def nasa(ctx):
    complete_url = 'https://api.nasa.gov/planetary/apod?api_key=****'

    response = requests.get(complete_url)
    x = response.json()

    em = discord.Embed(title=x['title'], colour=discord.Colour.gold())
    em.add_field(name="Description", value=x['explanation'])
    em.set_image(url=f"{x['hdurl']}")
    em.set_footer(text=x['date'])

    await ctx.send(embed=em)


@client.command()
@commands.is_owner()
async def members(ctx):
    for guild in client.guilds:
        for member in guild.members:
            await ctx.send(member)


@client.command(name="help1", description="Returns all commands available")
@commands.is_owner()
async def help1(ctx):
    helptext = "`"
    for command in client.commands:
        helptext += f"{command},"
    helptext += "`"
    await ctx.send(helptext)


@client.command()
@commands.is_owner()
async def emoji123(ctx):
    for i in client.guilds:
        emoji = discord.utils.get(i.emojis)
        await ctx.send(emoji)

# restart


def restart_bot():
    os.execv(sys.executable, ['python3'] + sys.argv)


@client.command(name='restart')
@commands.is_owner()
async def restart(ctx):
    await ctx.send("Restarting bot...")
    restart_bot()


@client.command(name='toggle', description='enable disable commands')
@commands.is_owner()
async def toggle(self, ctx, *, command):
    command = self.client.get_command(command)

    if command is None:
        await ctx.send("Command not found")
    elif ctx.command == command:
        await ctx.send("This command can't be disabled")
    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        await ctx.send(f"i have {ternary} {command.qualified_name} for you! ")


# main:*****
# test:*****
client.run(os.getenv("TOKEN"))
