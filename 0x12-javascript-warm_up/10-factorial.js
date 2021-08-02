#!/usr/bin/node

const process = require('process');

const args = process.argv;

let digit = Number(args[2]);

if (isNaN(digit)) {
  digit = 1;
}
console.log(doFactorial(digit));

function doFactorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  const result = a * doFactorial(a - 1);
  return (result);
}
