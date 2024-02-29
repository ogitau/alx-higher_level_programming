#!/bin/bash
#  script that takes in a URL and displays all allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
