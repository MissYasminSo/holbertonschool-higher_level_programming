#!/usr/bin/node

const { argv } = require('node:process');
let number = parseInt(argv[2]);

while (number > 0) {
  console.log('C is fun');
  number = number - 1;
}
