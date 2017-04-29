# downtime-twitter-bot
Twitter bot that tweets when your site goes down and tweets again when your site comes back up.

# Setup & Usage


- Twitter app authentication details (if you don't have any you can register at [Twitter Developers](https://apps.twitter.com/)):
  - *CONSUMER_KEY*
  - *CONSUMER_SECRET*
  - *ACCESS_TOKEN*
  - *ACCESS_TOKEN_SECRET*
- Bot specific: 
  - Website to monitor (*WEBSITE*)
- Already defined, but can be changed:
  - Interval (in seconds) to check if site is up (*POLLING_TIME*)
  - Tweet to send when the website experiences downtime (*DOWNTIME_MESSAGE*)
  - Tweet to send when the website goes back up (*DOWNTIME_FINISHED_MESSAGE*).

The twitter bot will be active and polling every *POLLING_TIME* seconds (60 seconds by default) as long as *bot.py* is running. 

You may also change the polling time via command-line. Here are some examples:

- `python bot.py -h 10` sets polling time to 10 hours.
- `python bot.py -m 30` sets polling time to 30 minutes.
- `python bot.py -s 10` sets polling time to 10 seconds.


# Logging

When your site goes down or comes back up, the event will be logged into your console as well as in a file called `downtime-log.txt` in the directory you're running the bot from.