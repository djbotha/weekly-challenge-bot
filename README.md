# Weekly Challenge Judge

## Introduction
A bot I wrote using [discord.py](https://github.com/Rapptz/discord.py) to tally up entries in a Discord competition. The competitions are hosted by the server admins and moderators, and every week/month users submit an image in a specific channel. The entry with the most ❤ reacts at the end of the period wins the competition.

This bot was written in python3 using [discord.py](https://github.com/Rapptz/discord.py) and [numpy](http://www.numpy.org). I assume you already have python3 installed.

## Installation Instructions
### Step 1
Install `discord.py`:

```python
python3 -m pip install -U discord.py
```

### Step 2
Install `numpy`:
```python
python3 -m pip install numpy -v
```
I added the `-v` vlag so the installation process will show all steps due to numpy being a very large library (and way overkill for our application).

### Step 3
Get your discord API key:

- Go to the [discord developers page](https://discordapp.com/developers/applications/me)
- Click on `new app`
- Add an app name
- Click `create app`
- On the next page, click `create a bot user`
- Under the `Bot` section, click `click to reveal` next to `token` to get your API key. 

### Step 4
To run your application, type the following in your terminal:
```python
python3 weekly-challenge.py <API KEY HERE>
```

### Step 5
To use the bot in your discord server, change the specified fields in `weekly-challenge.py` to the channel you'd like.
Then, run `>count` in your channel and the bot will return a nicely formatted list, looking like this:

![screenshot](https://i.imgur.com/xJG95uA.png)

Feel free to PM me on Discord at `iggnore#0146` if you have any issues.
