#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2, process.argv.length);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 0; i < args.length; i++) {
    arr[i] = Number(args[i]);
  }
  for (let k = 0; k < arr.length; k++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] < arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  console.log(arr[1]);
}
