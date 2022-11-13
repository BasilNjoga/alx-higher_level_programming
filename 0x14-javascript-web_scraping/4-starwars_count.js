#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count  = 0;

request (url, function (error, response, body) {
  if (error) throw error;
  const res = JSON.parse(body);
  for (let key in res) {
    for (let key1 in key) {
      if ( key= 18) {
        count = count + 1;
      }
    }
  }
  console.log(count);
    
});
