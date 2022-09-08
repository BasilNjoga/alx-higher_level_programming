#!/usr/bin/node

exports.logMe = function (item) {
  
  if (typeof logMe.count == 'undefined') {
    countMyself.count = 0;
  }
  ++logMe.count;
  const  myPrint = logMe.count + ': ' + item;
  console.log(myPrint);
}
