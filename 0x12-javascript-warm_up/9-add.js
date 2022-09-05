#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  const myVar = Number(a) + Number(b);
  console.log(myVar);
}
add(argv[2], argv[3]);
