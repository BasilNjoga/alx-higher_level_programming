#!/usr/bin/node

const { argv } = require('process');

if (argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    for (let j = 2; j < argv.length; j++) {
      if (argv[j] < argv[j + 1]) {
        const temp = argv[j];
        argv[j] = argv[j + 1];
        argv[j + 1] = temp;
      }
    }
  }
  console.log(argv[3]);
}
