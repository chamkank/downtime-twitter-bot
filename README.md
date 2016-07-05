# downtime-twitter-bot
Twitter bot that tweets when your site is down. 

NOTE: Replace constants with relevant information before using.

# Setup & Usage

Fill in values for the labelled constants in *bot.py*. 

This includes your Twitter app details for authentication (*CONSUMER_KEY*, *CONSUMER_SECRET*, *ACCESS_TOKEN*, *ACCESS_TOKEN_SECRET*), as well as the website to monitor, and the tweets to send when the website experiences downtime (*DOWNTIME_MESSAGE*) and goes back up (*DOWNTIME_FINISHED_MESSAGE*).

The twitter bot will be active and polling every minute as long as bot.py is running. 
