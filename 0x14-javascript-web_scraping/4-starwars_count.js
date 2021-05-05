#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
    if (error) {
        console.error(error);
        return
    }
    const character = JSON.parse(body).results;
    let counter = 0;
    for (let i = 0; i < character.length; i++) {
        for (let x = 0; x < character[i].characters.length; x++) {
            if (character[i].characters[x].endsWith("/18/")) {
            counter++;
            }
        }
    }
  console.log(counter);
});
