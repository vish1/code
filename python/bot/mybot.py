#!/usr/bin/python
import random
import json
import sys
import urllib2
import time

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(word):
    if word.lower() in GREETING_KEYWORDS:
        return random.choice(GREETING_RESPONSES)

def check_jenkins_job_status(jenkinsUrl):

    print "Checking status of job: "+ jenkinsUrl
    while True:
        try:
            jenkinsStream = urllib2.urlopen(jenkinsUrl)
        except urllib2.HTTPError, e:
            print "URL Error: " + str(e.code)
            sys.exit(1)

        try:
            buildStatusJson = json.load(jenkinsStream)
        except:
            print "Failed to parse json"
            sys.exit(1)

        if buildStatusJson.has_key("result"):
            if buildStatusJson["result"] == "SUCCESS":
                print "Job completed"
                exit(0)
            else:
                print ".",

        time.sleep(10)

if __name__ == "__main__":
    while True:
        x = raw_input("Bot: Say something to me and I will respond!\nYou: ")
        print "Bot: "+check_for_greeting(x)




