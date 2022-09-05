#!/usr/bin/node

const { argv } = require('process');

let newstr;

if (Number(argv[2])) {
  for (let j = 0; j < Number(argv[2]); j++) {
    newstr = '';
    for (let i = 0; i < Number(argv[2]); i++) {
      newstr = newstr + 'x';
    }
    console.log(newstr);
  }
} else {
  console.log('Missing size');
}
