#!/bin/bash
# script that takes url as arg and gets with custom header
curl -s --header "X-School-User-Id: 98" "$1"
