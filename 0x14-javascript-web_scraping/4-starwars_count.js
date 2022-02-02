#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const url = process.argv[2];
let countPerson = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let result = JSON.parse(body).results;
    for (let i in result) {
      let character = result[i].characters;
      for (let j in character) {
        if (character[j].includes('18')) {
          countPerson +=1;
        }
      }
    }
    console.log(countPerson)
  }
});