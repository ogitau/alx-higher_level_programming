#!/bin/bash
# script to send JSON POST request to url passed as frst arg and show response
curl -s -X POST -H "Content-Type: application/json" -d @"${2}" "${1}"
