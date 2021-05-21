#!/usr/bin/python3
'''Reddit API handler'''
import requests as r


def top_ten(subreddit):
    '''prints the titles of the first 10 hot
    posts listed for a given subreddit.'''
    payload = {'limit': 10}
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    x = r.get('https://www.reddit.com/r/{}/hot.json'
              .format(subreddit), headers=headers, params=payload,
              allow_redirects=False)
    if x.status_code == 404:
        print("None")
        return
    response = x.json().get('data').get('children')
    for data in response:
        title = data.get('data').get('title')
        print(title)
