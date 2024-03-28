#!/usr/bin/python3
""" Scrpt that takes an a URL, sends a resuest and displays the values
    of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
