#!/usr/bin/node
// script that writes a string to a file.

const file = process.argv[2];
const strWrite = process.argv[3];
const fs = require('fs');
fs.appendFile(file, strWrite, function (err) {
  if (err) throw err;
  console.log(strWrite);
});
