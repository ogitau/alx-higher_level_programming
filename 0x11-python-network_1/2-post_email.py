#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    params = {'email': argv[2]}
    data = parse.urlencode(params)
    data = data.encode('ascii')
    re = request.Request(argv[1], data)
    with request.urlopen(re) as response:
        body = response.read()
        print(body.decode('utf-8'))
