#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/3', function(error, response, body) {
  console.log(body)
});