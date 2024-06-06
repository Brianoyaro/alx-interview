#!/usr/bin/node
const endpoint = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${endpoint}`;
const request = require('request');
request(url, { json: true }, function(error, response, body) {
	if (error) console.log(error);
	for ( let character of body['characters']) {
		request( character, { json: true }, function(error, response, body) {
			console.log(body['name'])
		});
	}
});
