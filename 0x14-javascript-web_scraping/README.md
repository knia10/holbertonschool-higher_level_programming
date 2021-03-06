# 0x14. JavaScript - Web scraping π©
## Learning Objectives
### General
- π Why JavaScript programming is amazing
- π How to manipulate JSON data
- π How to use `request` and fetch API
- π How to read and write a file using `fs` module

## Requirements
### General
- π© Allowed editors: `vi`, `vim`, `emacs`
- π© All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
- π© All your files should end with a new line
- π© The first line of all your files should be exactly `#!/usr/bin/node`
- π© `A README.md` file, at the root of the folder of the project, is mandatory
- π© Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- π© All your files must be executable
- π© The length of your files will be tested using `wc`
- π© You are not allowed to use `var`

## More Info
### Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```
### Install request module and use it
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**_Notes:_** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, itβs a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

By Estefania Ruiz π¦ from Holberton School πͺ