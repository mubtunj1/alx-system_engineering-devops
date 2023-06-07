#!/usr/bin/python3
""""subscribers for  subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)

    result = response.json()

    try:
        return result.get('data').get('subscribers')

    except Exception:
        return 0
