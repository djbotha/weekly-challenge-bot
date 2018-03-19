# Weekly Challenge Judge

## Introduction
A bot I wrote using [discord.py](https://github.com/Rapptz/discord.py) to tally up entries in a Discord competition. The competitions are hosted by the server admins and moderators, and every week/month users submit an image in a specific channel. The entry with the most ❤ reacts at the end of the period wins the competition.

The bot downloads all images in the specified channel, saves them in `./images/dd-mm-YYYY/` and uploads all of those files to Google Drive.

This bot was written in python3 using [discord.py](https://github.com/Rapptz/discord.py) and [numpy](http://www.numpy.org). I assume you already have python3 installed.

## Installation Instructions
### Step 1
Install `discord.py`:

```
python3 -m pip install -U discord.py
```

### Step 2
Install `numpy`:
```
python3 -m pip install numpy -v
```
I added the `-v` flag so the installation process will show all steps due to numpy being a very large library (and way too overkill for our application).

### Step 3
Install [PyDrive](http://pythonhosted.org/PyDrive/quickstart.html) and get your Google Drive API credentials.

### Step 4
Get your discord API key:

- Go to the [discord developers page](https://discordapp.com/developers/applications/me)
- Click on `new app`
- Add an app name
- Click `create app`
- On the next page, click `create a bot user`
- Under the `Bot` section, click `click to reveal` next to `token` to get your API key. 
- Save your API key in a file called `discord_key.txt` in the root directory of your project.

### Step 5
To run your application, type the following in your terminal:
```
python3 weekly-challenge.py
```

### Step 6
To use the bot in your discord server, change the specified fields in `weekly-challenge.py` to the channel you'd like.
Then, run `>count` in your channel and the bot will PM the winning user return a nicely formatted list, looking like this:

![screenshot](https://i.imgur.com/gI0Us1K.png)

![screenshot](https://i.imgur.com/xJG95uA.png)

Feel free to PM me on Discord at `iggnore#0146` if you have any issues.
