#!/usr/bin/node
let arg = 1;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (arg <= parseInt(process.argv[2], 10)) {
    console.log('C is fun');
    arg++;
  }
}
