# downtime-twitter-bot
Twitter bot that tweets when your site is down. 

# Setup & Usage

Prior to usage, fill in values for the labelled constants in *bot.py*:

- Twitter app authentication details (if you don't have any you can register at [Twitter Developers](https://apps.twitter.com/)):
  - *CONSUMER_KEY*
  - *CONSUMER_SECRET*
  - *ACCESS_TOKEN*
  - *ACCESS_TOKEN_SECRET*
- Bot specific: 
  - Website to monitor (*WEBSITE*)
  - Tweet to send when the website experiences downtime (*DOWNTIME_MESSAGE*)
  - Tweet to send when the website goes back up (*DOWNTIME_FINISHED_MESSAGE*).

The twitter bot will be active and polling every minute as long as *bot.py* is running. 
