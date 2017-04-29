import urllib
import time
import tweepy
import sys

# Fill in API details and WEBSITE prior to running
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
WEBSITE = '' # URL of website to monitor
POLLING_TIME = 60 # Interval (in seconds) to check if site is up (this value is used if arguments aren't passed via command-line)
DOWNTIME_MESSAGE = "Our site is currently down at the moment. Thank you for your patience." #Tweet for when site goes down
DOWNTIME_FINISHED_MESSAGE = "Our site is back up! Thanks again for your patience." #Tweet for when site comes back up

# Creating API instance
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def handle_args():
    '''Handles command-line arguments (changes polling time if passed via command-line)'''
    args = sys.argv
    if (len(args) > 1):
        if "-s" in args:
            POLLING_TIME = int(args[args.index("-s")+1])
            print("Polling time set to " + str(POLLING_TIME) + " sec")
        elif "-m" in args:
            mins = int(args[args.index("-m")+1])
            POLLING_TIME = 60*mins
            print("Polling time set to " + str(mins) + " min")
        elif "-h" in args:
            hours = int(args[args.index("-h")+1])
            POLLING_TIME = 3600*hours
            print("Polling time set to " + str(hours) + " hr")


def log(entry):
    ''' Logs entry to downtime_log.txt, used to log downtime and uptime messages'''
    try:
        log_file = open("downtime_log.txt", 'a')
    except IOError:
        log_file = open("downtime_log.txt", 'w')
    log_file.write(entry + "\n")

def site_is_up(site):
    ''' Check to see if site is up. '''
    try :
        return (urllib.request.urlopen(WEBSITE).getcode() == 200)
    except:
        return False
    
def downtime_started():
    ''' Called when site is down '''
    api.update_status(DOWNTIME_MESSAGE)
    message = "Site went down at %r" % time.ctime()
    print(message)
    log(message)
    while (not site_is_up(WEBSITE)):
        if site_is_up(WEBSITE):
            downtime_finished()
        time.sleep(POLLING_TIME)

def downtime_finished():
    ''' Called when site comes back up '''
    api.update_status(DOWNTIME_FINISHED_MESSAGE)
    message = "Site went back up at %r" % time.ctime()
    print(message)
    log(message)


def main_loop():
    ''' Handles polling procedure '''
    while True:
        if site_is_up(WEBSITE):
            print("Site is up")
            time.sleep(POLLING_TIME)
        else:
            downtime_started()

handle_args()
main_loop()
