#!/usr/bin/node
const endpoint = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${endpoint}`;
const request = require('request');
request(url, { json: true }, function(error, response, body) {
	if (error) console.log(error);
	let urls = body['characters']
	function requestAPromise(url) {
		return new Promise((resolve, reject) => {
			request (url, {json: true}, (err, response, body) => {
				if (err) {
					reject(err);
				}else{
				resolve(body['name'])
				}
			})
	});};
	async function HandleAllUrls(urls) {
		for (let url of urls) {
			const data = await requestAPromise(url);
			console.log(data)
		}
	};
	HandleAllUrls(urls);
});
