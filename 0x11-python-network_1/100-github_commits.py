#!/usr/bin/python3
"""Getting commits data from Github API"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    resp = requests.get(url)
    commits = resp.json()
    try:
        for idx in range(10):
            print("{}: {}".format(
                commits[idx].get("sha"),
                commits[idx].get("commit").get("author").get("name")))
    except IndexError:
        pass
