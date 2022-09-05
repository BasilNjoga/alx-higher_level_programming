#!/usr/bin/node

const { argv } = require('process');
let myVal;

function factorial (a) {
  if (Number(a)) {
    myVal = Number(a);
    if (myVal === 0) {
      return 1;
    } else {
      return myVal * factorial(myVal - 1);
    }
  } else {
    return 1;
  }
}

console.log(factorial(argv[2]));
