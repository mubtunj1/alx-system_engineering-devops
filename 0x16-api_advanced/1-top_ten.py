#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
from requests import get


def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        print(None)

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    prams = {'limit': 10}
    response = get(url, headers=user_agent, params=prams)
    results = response.json()

    try:
        for post in results.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)
