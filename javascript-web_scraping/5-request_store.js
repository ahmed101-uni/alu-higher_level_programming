#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const content = body;
    fs.writeFile(filePath, content, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
