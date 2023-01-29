import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to the discord server")


@bot.command(
    help="Responds you with a Hey!",
    brief="Greets you when all of your friends are offline!"
)
async def hi(ctx):
    await ctx.send("Hey there!")


@bot.command(
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	brief="Pong back to your channel with the latency."
)
async def ping(ctx):
    await ctx.send(f"pong: {round(bot.latency*1000)} ms")


@bot.command(
    help="Gives you a motivation to cut a mountain :)",
    brief="Gives quotes to boost your confidence"
)
async def givequote(ctx):
    response = requests.get('https://api.quotable.io/random')
    r = response.json()
    quote = r["content"]
    await ctx.send(quote)

@bot.command(
    help="Gives the dumbest joke in the name of a Chuck Norris",
    brief="Gives a dumb joke on Chuck Norris"
)
async def givejoke(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()['value']
    await ctx.send(joke)


@bot.command(
    help="Gives the topmost prime headlines!",
    brief="Gives prime headline of the moment!"
)
async def giveheadline(ctx):
    news_api_key = "your_api_key_here"
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={news_api_key}")
    headline = response.json()['articles'][0]['title']
    url = response.json()['articles'][0]['url']
    await ctx.send(f"{headline}\nFor more info, click here: {url}")


@bot.command(
    help="Gives the weather of your place",
    brief="Temperatures falling or rising; get to know everything here!"
)
async def givetemp(ctx):
    lat = "your_latitude"
    lon = "your_longitude"
    weather_api_key = "your_api_key_here"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}")
    kelvin = response.json()['main']['temp']
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    humidity = response.json()['main']['humidity']
    await ctx.send(f"Local Temperature:\n{celsius} degree Celsius\n{fahrenheit} degree Fahrenheit\nHumidity: {humidity}%")

@bot.command(
    help="Gives the best memes from reddit",
    brief="Drops some best hilarious memes trending on the Internet!"
)
async def givememe(ctx):
    response = requests.get("https://meme-api.com/gimme")
    r = response.json()
    meme = r["url"]
    await ctx.send(meme)

@bot.command(
    help="Gives IMDb rating, plot and poster of the movies or series you enter",
    brief="Let\'s binge baby!(based on IMDb ratings:))"
)
async def giverating(ctx, *, title: str = commands.parameter(description="- Title of the Movie/Series to be retrieved")):
    omdb_api_key = 'your_api_key_here'
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={title}"
    response = requests.get(url)
    await ctx.send(f"The IMDb rating of the movie/series \"{response.json()['Title']}\"({response.json()['Year']}) is "
                   f"{response.json()['imdbRating']} stars out of 10.\n\nThe plot "
                   f"description"
                   f" goes like this: {response.json()['Plot']}\n{response.json()['Poster']}")


token = 'your_discord_bot_token'

bot.run(token)
