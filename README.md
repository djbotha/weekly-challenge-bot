# Weekly Challenge Judge

## Introduction
A bot I wrote using [discord.py](https://github.com/Rapptz/discord.py) to tally up entries in a Discord competition. The competitions are hosted by the server admins and moderators, and every week/month users submit an image in a specific channel. The entry with the most ❤ reacts at the end of the period wins the competition.

The bot downloads all images in the specified channel, saves them in `./images/dd-mm-YYYY/` and uploads all of those files to Google Drive. 

## Requirements

- [Python 3](https://www.python.org/download/releases/3.0/)
- [discord.py](https://github.com/Rapptz/discord.py)
- [numpy](http://www.numpy.org)
- [PyDrive](http://pythonhosted.org/PyDrive/quickstart.html)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/google/oauth2client)

This bot was written in python3 using [discord.py](https://github.com/Rapptz/discord.py) and [numpy](http://www.numpy.org). I assume you already have python3 installed.

## Installation Instructions
### Step 1
Install [Python 3](https://www.python.org/download/releases/3.0/):

On MacOS:
```
brew install python
```

On Linux:
```
sudo apt-get install python3.6
```

### Step 2
Install [discord.py](https://github.com/Rapptz/discord.py):


```
python3 -m pip install -U discord.py
```

### Step 3
Install [numpy](http://www.numpy.org):

```
python3 -m pip install numpy -v
```
I added the `-v` flag so the installation process will show all steps due to numpy being a very large library (and way too overkill for our application).

### Step 4
Install [PyDrive](http://pythonhosted.org/PyDrive/quickstart.html) and get your Google Drive API credentials.


### Step 5
Install [gspread, oauth2client](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html?utm_source=youtube&utm_medium=video&utm_campaign=youtube_python_google_sheets), and get your Google Service Account Credentials.

### Step 6
Get your discord API key:

- Go to the [discord developers page](https://discordapp.com/developers/applications/me)
- Click on `new app`
- Add an app name
- Click `create app`
- On the next page, click `create a bot user`
- Under the `Bot` section, click `click to reveal` next to `token` to get your API key. 
- Save your API key in a file called `discord_key.txt` in the root directory of your project.

### Step 7
To run your application, type the following in your terminal:
```
python3 weekly-challenge.py
```

### Step 8
To use the bot in your discord server, change the specified fields in `weekly-challenge.py` to the channel you'd like.
Then, run `>count` in your channel and the bot will PM the winning user return a nicely formatted list, looking like this:

![dm](https://i.imgur.com/gI0Us1K.png)

![announcement](https://i.imgur.com/xJG95uA.png)

Feel free to PM me on Discord at `iggnore#0001` if you have any issues.
