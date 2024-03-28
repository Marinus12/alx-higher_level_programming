#!/usr/bin/python3
""" SCript that takes my Github credentials (username and password)
    and uses the Github API to display my id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
