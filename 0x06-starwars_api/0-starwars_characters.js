#!/usr/bin/node
const endpoint = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${endpoint}`;
const request = require('request');
request(url, function(error, response, body) {
	console.log(error);
	console.log(body['title']);
});
