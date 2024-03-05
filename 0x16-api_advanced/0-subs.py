#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["subscribers"]
    else:
        return 0
