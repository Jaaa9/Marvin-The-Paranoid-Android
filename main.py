from discord.ext import commands
import discord
import os
from marvin import marvinsquotes, marvinvideos

# assigning commands.Bot() to bot variable and setting default command prefix as "!", meaning all commands
# will start with "!". The function name is also the command, for instance calling ping() you would write !ping
bot = commands.Bot(command_prefix="!", status=discord.Status.idle, activity=discord.Game(name="Booting.."))


# Loading bot, setting status as online and activity
@bot.event
async def on_ready():
    print("Logged in as ", bot.user.name)
    print("My user id is: ", bot.user.id)
    print('##### BOT READY #####')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Active!"))


# Creating the !commands command
@bot.command()
async def commands(ctx):
    print("Here are my commands\n")
    await ctx.channel.send("ping, ")


# Creating the !ping command
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.channel.send("My latency is " + str(round(bot.latency, 3)) + " MS")


# Creating the !quote command
# Calling marvinsquotes function from marvinsquotes.py
# TODO: Add aliases??
@bot.command()
async def quote(ctx):
    await ctx.channel.send(marvinsquotes())


# Defining a youtube video command that provide random videos from the movie.
@bot.command()
async def clips(ctx):
    await ctx.channel.send(marvinvideos())


# Creating the !kick command
# TODO: Fix so that the bot doesn't crash if !kick is empty
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot KICK yourself!")
        return
    if reason == None:
        reason = "My protocols have failed me.. I'm sure I can find the reason you were booted from the server " \
                 "somewhere.. maybe you're just sad, like me? "
    message = f"You have been kicked from the server because {reason}"
    await member.send(reason)
    await member.kick()
    await ctx.channel.send(f"There he goes..{member} was a troubled soul for sure")
    await ctx.channel.send("http://45.media.tumblr.com/tumblr_m9mle0CoJM1qhsmbwo1_r3_500.gif")


@bot.command()
async def bustimes(ctx, aliases='Bustimes'):
    BusSchedule = 'http://skilt.akt.no/Tmix.Cap.DigSig.Gui/App/Rtpi.aspx?numberOfRows=10&stopAreaId=10015030'
    await ctx.channel.send("Well..I guess if you MUST know.. here they are\n" + BusSchedule)


# Creating the ban command
# TODO: Fix so that if !ban command is empty the bot doesn't crash
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if member is None or member == ctx.message.author:
        await ctx.channel.send("Considering how depressed you look I should allow this behavior\n however, my"
                               "protocols won't allow this behavior(You can't ban yourself)\n "
                               "https://tenor.com/view/marvin-hitchhiker-guide-to-the-galaxy-gif-4931649")
        return
    if reason is None:
        reason = "YOU offended Marvin"

    message = f"You have been banned from the server because {reason}"
    await member.send(message)
    await member.ban()
    await ctx.channel.send(f"{member} is banned from the server!")


# Creating the !unban command
# TODO: Cannot !unban with @, fix? !unban jekerholt#3601 works but missing @
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"Unbanned {user.mention}")
            return


# Fetching token 'DiscordToken' from env
token = os.getenv("DiscordToken")
bot.run(token)
