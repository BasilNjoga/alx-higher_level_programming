#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;
  const res = JSON.parse(body);
  const obj = res.characters;
  for (let i = 0; i < obj.length; i++) {
    request(obj[i], function (error, response, body) {
      if (error) throw error;
      console.log(JSON.parse(body).name);
    });
  }
});
