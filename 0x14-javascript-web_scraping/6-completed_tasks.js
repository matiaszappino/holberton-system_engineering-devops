#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const dict = {};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const path = JSON.parse(body);

  path.forEach(element => {
    if (element.completed === true) {
      const user = element.userId;
      if (dict[user] === undefined) {
        dict[user] = 1;
      } else {
        dict[user] += 1;
      }
    }
  });
  console.log(dict);
});
