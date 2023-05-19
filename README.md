# discord-bot

Personal discord bot made for me to add any fun functionality to as I please.

## Setup

Prior to running, create a `.env` file and add your discord token under the `TOKEN` variable and your Spoontacular api key under the `SPOONACULAR_API_KEY` variable. You may also set `SHOW_EDITS` and `SHOW_DELETES` in the `.env`, though they will default to `True` and can be set while the bot is running in Discord as well.

Next run `pip install -r`

You should be ready to run this simple program locally.

## Commands List

### !bot_help

Lists the commands in an embedded text block in the discord server

### !ready

Use this command to ready up, or unready if you are already ready. The bot will alert you when you have readied up and, if all members in the discord have readed up, will alert you when everyone in the server have readied up

### !recipe

Use this command to display a random recipe. The bot will respond with embedded text displaying a recipe, a link to the recipe, and an image. You may refine the randomness by adding arguments to your command like so `!recipe mediterranean` or `!recipe vegetarian dessert`. Uses the Spoontacular random recipe api

### !delete

Toggles `show_deletes` to True or False respectively

### !edit

Toggles `show_edits` to True or False respectively

## Background Processes

### On Message Delete

If `show_deletes=True` (which is the default, but can be set to `False` in `.env`) then when a message is deleted, the bot sends an embedded message saying the name of the person who deleted the message, the message, and the time of deletion

`show_deletes` can also be toggled in discord by using the `!delete` command

### On Message Edit

If `show_edits=True` (which is the default, but can be set to `False` in `.env`) then when a message is edited, the bot sends an embedded message which the editors name, the before message, and the editted message.

`show_edits` can also be toggled in Discord by using the `!edit` command
