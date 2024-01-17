#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:

// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star Wars API
// You must use the request module

const request = require('request');

// command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, async function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        const characters = JSON.parse(body).characters;
        for (const character of characters) {
            const characterResponse = await new Promise((resolve, reject) => {
                request(character, (error, response, html) => {
                    if (error) {
                        reject(error);
                    } else {
                        resolve(JSON.parse(html).name);
                    }
                });
            });
            console.log(characterResponse);
        }
    }
});