#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
