#!/usr/bin/node

const fs = require('fs');
fs.readfile(process.argv[2], 'utf8', function(err, data){
    if (err) throw err;
    console.log(data);
});