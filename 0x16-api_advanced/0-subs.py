#!/usr/bin/python3
"""How many subs"""
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for the passed in subreddit"""
    apiURL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = requests.get(
        apiURL,
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    if resp.status_code != 200:
        return 0

    jsonData = resp.json()
    noOfSubs = jsonData.get('data').get('subscribers')
    return noOfSubs
