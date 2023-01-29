# discord_bot_py
A user-friendly discord bot with various functionalites and commands built using Python only.

# Creating the discord bot
Follow these steps to create your own Discord bot:


Step 1: Log into your Discord account and click on “Advanced” in the sidebar. Then activate “Developer Mode”. Then click on “Discord API”.

Step 2: In the Developer Portal, click on “Applications” in the sidebar on the left. Log in to your account again and then click on “New Application”.

Step 3: Give your bot a name and then click on “Create”.

Step 4: Click on “Bot” in the left sidebar, then click on “Add Bot” to create a bot account and bot token. Take note of the token, as this is the how the bot communicates with the API.

Step 5: Now it’s time to start programming your bot. Since this involves advanced programming steps, you should have previous knowledge of programming languages and tools. Use an IDEA programming environment, programming tools like Python 3 or node.js, or a text editor like Notepad++. After you’ve written the bot, save the bot file.

Step 6: Back in Developer Mode in Discord, go to “General Information” and set details like the description and app icon.

Step 7: Go to “OAuth2” and in the field “Scopes” check the box for “bot”. Then set the permissions for your Discord bot.

Step 8: The authentication link including client ID should look as follows:
      https://discordapp.com/oauth2/authorize?&client_id=IHRE-ID&scope=bot&permission=8
      
Click on “Copy” to add the bot link to your server.
      
Step 9: Select your Discord server in order to add your bot.

# Installation
Github:

```$ git clone https://github.com/aneeshkp246/discord_bot_py```
      
Python Packages:

```pip install -r requirements.txt```
      
Or just:

```pip install discord.py```
      
The official documentation of discord.py is [here](https://discordpy.readthedocs.io/en/latest/index.html).

# Setup

1. Open discord_bot.py
2. Replace your discord bot token and other API keys needed.

# Usage

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt ( Windows) .`

After that you can start it with

```python discord_bot.py```

After running the file, the bot appears online in the server member list.

You can type !help in the discord server to see the available commands and their description. You need to prefix "!" to every command to trigger the particular function.

# Using the APIs in the file

givequote: Quotable is a free, open source quotations API. It was originally built as part of a FreeCodeCamp project. You can check their github [here](https://github.com/lukePeavey/quotable).

givejoke: chucknorris is a free JSON API for hand curated Chuck Norris facts. For more infromation, check them out [here](https://api.chucknorris.io/).

giveheadline: Gives the headline of specified region, category and more along with providing the url of the news using News API. You need to sign in and get an API key to use this. For that you can refer [here](https://newsapi.org/).

givetemp: Gives temperature of specifies latitude and longitude in degree celcius and fahrenheit and also the humidity using OpenWeatherMap's API. You need to sign in and get an API key to use this. For that you can refer [here](https://openweathermap.org/).

givememe: Gives memes from Reditt using Meme API. Its documentation is [here](https://github.com/D3vd/Meme_Api).

giverating: Gives IMDb rating of a movie/series entered (as it is from Google), its plot summary and poster using OMDb API. You need to sign in and get an API key to use this. For that you can refer [here](https://www.omdbapi.com/).
An example of usage is given here:

```!giverating Interstellar```


# License

MIT © aneeshkp246

