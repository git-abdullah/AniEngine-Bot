import json
import requests as re
from graphql_query import search_query, get_query
import time
import discord
from discord.ext import commands

url = 'https://graphql.anilist.co'
discord_api_key = "api key here"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")


@bot.command(
    name='search',
    description="searches for anime based on your query"
    )
async def hi(ctx, search_q):
    # queries and variables
    query = search_query.get('query')
    variables = search_query.get('variables')
    variables['search'] = search_q

    # post request, returns json object
    response = re.post(url, json={'query': query, 'variables': variables})
    data = json.loads(response.text)['data']['Page']['media']

    # discord embed for pretty responses
    embed = discord.Embed(title="SEARCH RESULTS", description="- list of top 5 anime(s) matching your query", color=0x7545b0)
    embed.set_footer(text="- results were fetched from anilist.co using their API")

    for id in data:
        title = id['title']['romaji']
        url_s = id['siteUrl']
        embed.add_field(name=f'🔹 {title}', value=f'ɻ -details at {url_s}', inline=False)
    await ctx.send(embed=embed)
    time.sleep(1)


bot.run(discord_api_key)


# use this func to get details about the anime, takes in anime id 
def details(ani_id):
    # queries and variables
    query = get_query.get('query')
    variables = get_query.get('variables')
    variables['id'] = ani_id

    # post request, returns, json object
    response = re.post(url, json={'query': query, 'variables': variables})
    data = json.loads(response.text)
    return data['data']['Media']['title']['english'] # returns only title (change it)

