#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movies = JSON.parse(body).results;
    const amount = movies.filter(mov => mov.characters.some(ch => ch.endsWith('18/')));
    console.log(amount.length);
  }
});
