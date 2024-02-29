#!/bin/bash
# script that sends request to URL passed as an arg and displays status code
curl -so /dev/null -w "%{http_code}" "$1"
