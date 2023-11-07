#!/usr/bin/python3
"""Recursion of getting top ten hot subreddit posts"""
import requests


def recurse(subreddit, hot_list=[], counter=0, after=None):
    """Returns a list of the subreddit's hot article titles"""
    resp = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
        params={"counter": counter, "after": after}
    )

    if resp.status_code != 200:
        return None

    thaList = hot_list + [post.get('data').get('title')
                          for post in resp.json()
                          .get('data')
                          .get('children')]

    apiData = resp.json()
    if not apiData.get('data').get('after'):
        return thaList

    return recurse(
        subreddit,
        thaList,
        apiData.get('data').get('counter'),
        apiData.get('data').get('after')
    )
