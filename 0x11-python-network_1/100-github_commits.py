#!/usr/bin/python3
""" Script takes 2 arguments in order to solve this challenge
    list 10 commits (from the most recent to oldest) of the repository “
    rails” by the user “rails”
"""
import requests
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    r = requests.get(url)
    commits = r.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
