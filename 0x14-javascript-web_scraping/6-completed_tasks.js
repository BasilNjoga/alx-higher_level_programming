#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
let count = 0;

request (url, function (error, response, body) {
  if (error) throw error;
  const res = JSON.parse(body);
  for(let i = 0; i < res.length; i++) {
    let obj = res[i];
    if (obj.completed = "true") {
      count = count + 1;
    }
    }
  console.log(count);
});
