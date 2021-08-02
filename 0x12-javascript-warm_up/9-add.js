#!/usr/bin/node

const process = require('process');

const args = process.argv;

add(Number(args[2]), Number(args[3]));

function add (a, b) {
  console.log(a + b);
}
