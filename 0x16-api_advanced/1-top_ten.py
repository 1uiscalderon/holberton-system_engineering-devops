#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
https://www.reddit.com/dev/api/"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit"""
    headers_ = {'User-Agent': 'Don Boris'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit), headers=headers_,
                            allow_redirects=False)
    try:
        response.raise_for_status()
    except Exception:
        print(None)
    else:
        try:
            children = response.json().get('data').get('children')
            for child in children[None:10]:
                print(child.get('data').get('title'))
        except Exception:
            print(None)
