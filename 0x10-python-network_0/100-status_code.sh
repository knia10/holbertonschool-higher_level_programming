#!/bin/bash
# Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -o /dev/null -s --write-out '%{http_code}\n' $1
