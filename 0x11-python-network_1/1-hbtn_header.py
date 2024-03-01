#!/usr/bin/python3
# script that takes url sends a request to url
# and displays the value of the X-Request_Id var found in header response
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
