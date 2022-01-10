#!/usr/bin/python3
'''
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
from sys import argv


if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    req = requests.post("http://0.0.0.0:5000/search_user")