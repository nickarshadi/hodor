#!/usr/bin/python3
"""Module for Hodor challenge."""
import requests
"""Website to vote on"""
url = "http://158.69.76.135/level0.php"
data = {'id': 7, 'holdthedoor': "Submit"}
sucess = "Hold the Door challenge - Level 0"
votes = 1024
win = 0
fail = 0

print("Starting {} votes:".format(votes))

while win < votes and fail < 100:
    try:
        response = requests.post(url, data=data)
        if response.status_code is 200 and sucess in response.text:
            fail = 0
            win += 1
            print("{} wins!".format(win))
    except Exception as e:
        print(e)
        fail += 1

print("Finished: {}/{} votes.".format(win, votes))
