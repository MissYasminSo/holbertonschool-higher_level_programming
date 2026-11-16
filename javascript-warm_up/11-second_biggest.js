#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const sorted = argv.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
