#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
https://www.reddit.com/dev/api/"""
import requests


def number_of_subscribers(subreddit):
    """Brings the subscribers"""
    headers_ = {'User-Agent': 'Don Boris'}
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit), headers=headers_)
    try:
        response.raise_for_status()
    except Exception:
        return 0
    else:
        subscribers = response.json().get('data').get('subscribers')
        if subscribers is None:
            return 0
        return subscribers
