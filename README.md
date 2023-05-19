# discord-bot

Personal discord bot made for me to add any fun functionality to as I please.

## Setup

Prior to running, create a `.env` file and add your discord token under the `TOKEN` variable and your Spoontacular api key under the `SPOONACULAR_API_KEY` variable.

Next run `pip install -r`

You should be ready to run this simple program locally.

## Commands List

### !bot_help

Lists the commands in an embedded text block in the discord server

### !ready

Use this command to ready up, or unready if you are already ready. The bot will alert you when you have readied up and, if all members in the discord have readed up, will alert you when everyone in the server have readied up

### !recipe

Use this command to display a random recipe. The bot will respond with embedded text displaying a recipe, a link to the recipe, and an image. You may refine the randomness by adding arguments to your command like so `!recipe mediterranean` or `!recipe vegetarian dessert`. Uses the Spoontacular random recipe api
