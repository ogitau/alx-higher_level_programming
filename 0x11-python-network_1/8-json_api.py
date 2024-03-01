#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ""
    val = {'q': q}

    try:
        re = requests.post(url, data=val)
        data = re.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except (ValueError) as e:
        print("Not a valid JSON")
