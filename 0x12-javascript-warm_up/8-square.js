#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let lengh = 0; lengh < parseInt(process.argv[2], 10); lengh++) {
    console.log('X'.repeat(parseInt(process.argv[2], 10)));
  }
}
