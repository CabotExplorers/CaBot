import discord
from discord.ext import commands

from checks import isAdmin
from models import KeyValue

def setup(bot) :
    bot.add_cog(Count(bot))

def onlyInCount(ctx) :
    return ctx.channel.id == 692068931032055840

class Count(commands.Cog, name = "Some weird counting game") :

    def __init__(self, bot) :
        self.bot = bot

        self.store, stored = KeyValue.get_or_create(key = "count", defaults = { "value": "0" })
        self.count = int(self.store.value)

    def cog_unload(self) :
        self.store.value = str(self.count)
        self.store.save()

    @commands.command()
    @commands.guild_only()
    @commands.check(onlyInCount)
    async def count(self, ctx) :
        self.count += 1
        emoji = ":tada:" if (self.count == 100) else ":money_with_wings:"

        await ctx.send(embed=discord.Embed(
            description = f"{emoji} {self.count}",
            color = 12745742,
        ))

        if self.count >= 100 :
            points = 20
            self.bot.get_cog('Points').addPoints(points, [ctx.author.id])
            self.count = 0

            await ctx.send(embed=discord.Embed(
                description = f"{points} points for {ctx.author.mention}!",
                color = 12745742,
            ))

        elif self.count % 10 == 0 :
            points = 5
            self.bot.get_cog('Points').addPoints(points, [ctx.author.id])

            await ctx.send(embed=discord.Embed(
                description = f"{points} points for {ctx.author.mention}!",
                color = 12745742,
            ))

    @commands.command()
    @commands.guild_only()
    @commands.check(isAdmin)
    async def setcount(self, ctx, num) :
        if num :
            self.count = int(num)
            await ctx.send(embed=discord.Embed(
                description = f"Count set to {num}",
                color = 12745742,
            ))