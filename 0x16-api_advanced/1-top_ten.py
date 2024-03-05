#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        i = 0;
        for item in data:
            if i < 10:
                print(data.get("data").get("title"))
                i = i + 1
            else:
                break
    else:
        print(None)
