#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays
    the body of the request of the response
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    reponse = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
