#!/usr/bin/python3
"""Py script that fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    resp = response.text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
