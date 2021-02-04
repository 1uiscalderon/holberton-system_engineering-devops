#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers
https://www.reddit.com/dev/api/"""
import requests


def recurse(subreddit, hot_list=[], after='null'):
    """Recursive"""
    headers_ = {'User-Agent': 'Don Boris'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=100"
                            .format(subreddit), headers=headers_)
    try:
        response.raise_for_status()
    except Exception:
        return None
    else:
        if after is None:
            return hot_list
        elif after is 'null':
            resp = requests.get(
                "https://www.reddit.com/r/{}/hot.json?limit=100"
                .format(subreddit), headers=headers_).json().get('data')
            after = resp.get('after')
            for threads in resp.get('children'):
                hot_list.append(threads.get('data').get('title'))
            recurse(subreddit, hot_list, after)
            return hot_list
        else:
            resp = requests.get(
                "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"
                .format(subreddit, after), headers=headers_).json().get('data')
            after = resp.get('after')
            for threads in resp.get('children'):
                hot_list.append(threads.get('data').get('title'))
            recurse(subreddit, hot_list, after)
            return hot_list
