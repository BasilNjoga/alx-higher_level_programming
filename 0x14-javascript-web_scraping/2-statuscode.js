#!/usr/bin/node

const request = require('request');
request(package.argv[2], function (error, response, body) {
    console.log(response.statusCode)
});