#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header.
'''
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
