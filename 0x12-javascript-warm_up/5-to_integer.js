#!/usr/bin/node

const { argv } = require('process');

let myVar;
if (Number(argv[2])) {
  myVar = 'My number: ' + Number(argv[2]);
  console.log(myVar);
} else {
  console.log('Not a number');
}
