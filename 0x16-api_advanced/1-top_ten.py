#!/usr/bin/python3
"""Top ten hot subreddit posts"""
import requests


def top_ten(subreddit):
    """Prints a subreddit's top ten titles"""
    resp = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    if resp.status_code == 200:
        apiData = resp.json()
        postsList = apiData.get('data').get('children')
        for i in range(10):
            print(postsList[i].get('data').get('title'))
    else:
        print('None')
