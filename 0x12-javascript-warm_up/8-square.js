#!/usr/bin/node

const process = require('process');

const args = process.argv;

const i = Number(args[2]);

if (isNaN(i)) {
  console.log('Missing size');
} else {
  let str = 'X';
  for (let j = 1; j < i; j++) {
    str = str + 'X';
  }
  for (let k = 0; k < i; k++) {
    console.log(str);
  }
}
