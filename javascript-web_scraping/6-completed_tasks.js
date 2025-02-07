#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    const reduced = content.reduce((a, i) => {
      if (i.completed) {
        a[i.userId] = a[i.userId] ? a[i.userId] + 1 : 1;
      }
      return a;
    }, {});
    console.log(reduced);
  }
});
