#!/usr/bin/python3
""" script that takes url sends a request to url
and displays the value of the X-Request_Id var found in header response"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('x-request-id'))
