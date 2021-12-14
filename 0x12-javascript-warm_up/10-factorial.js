#!/usr/bin/node
const myVar = parseInt(process.argv[2]);

function myFact (num) {
  if (isNaN(num) || (num === 1)) {
    return (1);
  } else {
    return (num * myFact(num - 1));
  }
}
console.log(myFact(myVar));
