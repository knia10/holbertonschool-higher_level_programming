#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''
if __name__ == "__main__":
    import requests

    request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
