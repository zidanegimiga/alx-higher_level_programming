#!/usr/bin/node

const process = require('process');
const args = process.argv;

const i = Number(args[2]);

if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
