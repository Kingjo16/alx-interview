#!/usr/bin/node
const request = require('request');
const API_BASE_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  request(`${API_BASE_URL}/films/${movieId}/`, (error, _, responseBody) => {
    if (error) {
      console.log(error);
      return;
    }
    
    const characterUrls = JSON.parse(responseBody).characters;
    const characterNamesPromises = characterUrls.map(url => 
      new Promise((resolve, reject) => {
        request(url, (promiseError, __, characterResponseBody) => {
          if (promiseError) {
            reject(promiseError);
          } else {
            resolve(JSON.parse(characterResponseBody).name);
          }
        });
      })
    );

    Promise.all(characterNamesPromises)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.log(error));
  });
}
