#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
let count = 0;

request (url, function (error, response, body) {
  if (error) throw error;
  const res = JSON.parse(body);
  for(let i = 0; i < res.length; i++) {
    let obj = res[i];
    for (let j = 1; j < 11; j++) {
      while (obj.userId = j) {
	if (obj.completed = "true") {
        count = count + 1;
        }
      }
      console.log('${j}: ${count}');
      count = 0;
    }
}
  console.log(count);
});
