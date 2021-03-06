import discord
from discord.ext import commands

from server import roles


def setup(bot):
    bot.add_cog(Roles(bot))


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def toggleRole(self, ctx, role):
        role = ctx.guild.get_role(roles[role])

        if role:
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.send(
                    embed=discord.Embed(
                        description=f"Removed from <@&{role.id}>",
                        color=1146986,
                    )
                )

            else:
                await ctx.author.add_roles(role)
                await ctx.send(
                    embed=discord.Embed(
                        description=f"Added to <@&{role.id}>",
                        color=1146986,
                    )
                )

    @commands.command()
    @commands.guild_only()
    async def gamer(self, ctx):
        await self.toggleRole(ctx, "gamer")

    @commands.command()
    @commands.guild_only()
    async def lgbt(self, ctx):
        await self.toggleRole(ctx, "lgbt")

    @commands.command()
    @commands.guild_only()
    async def politics(self, ctx):
        await self.toggleRole(ctx, "politics")

    @commands.command()
    @commands.guild_only()
    async def programmer(self, ctx):
        await self.toggleRole(ctx, "programmer")

    @commands.command()
    @commands.guild_only()
    async def moot(self, ctx):
        await self.toggleRole(ctx, "moot")
