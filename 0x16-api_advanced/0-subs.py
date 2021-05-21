#!/usr/bin/python3
'''Reddit API handler'''
import requests as r


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers'''
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    x = r.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
              headers=headers, allow_redirects=False)
    if x.status_code == 404:
        return 0
    response = x.json().get('data')
    return response.get('subscribers')
