#!/usr/bin/node

api = "https://swapi-api.hbtn.io/api/films/"

const request = require('request');
request(api + process.argv[2], function (error, response, body) {
    if (error) {
        console.error(error);
        return
    }
    console.log(JSON.parse(body).title);
});
