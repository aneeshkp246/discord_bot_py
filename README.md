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

Next, you will need to install the Discord.py library for Python, which allows you to interact with the Discord API. This can be done by running the following command: ```pip install discord.py```

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt ( Windows) .

Before running the bot you will need to install all the requirements with this command:
```python -m pip install -r requirements.txt```

After running the file, the bot appears online in the server member list.

# Using the APIs in the file

givequote: Quotable is a free, open source quotations API. It was originally built as part of a FreeCodeCamp project. You can check their github [here]{https://github.com/lukePeavey/quotable}



