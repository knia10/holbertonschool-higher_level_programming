#!/usr/bin/python3
'''
Write a Python script that fetches https://intranet.hbtn.io/status
with package urllib and with statement
'''
if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        fetch = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(fetch)))
        print("\t- content: {}".format(fetch))
        print("\t- utf8 content: {}".format(fetch.decode("utf-8", "ignore")))
