#!/usr/bin/python3
""" script that takes url sends a request to url
and displays the value of the X-Request_Id var found in header response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get['X-Request-Id'])
