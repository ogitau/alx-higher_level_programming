#!/bin/bash
# script to send JSON POST request to url passed as frst arg and show response
curl -s -H "Content_Type: application/json" -d @"${2}" "${1}"
