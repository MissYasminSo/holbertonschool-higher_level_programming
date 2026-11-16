#!/usr/bin/node

const movieList = document.getElementById('list_movies');

async function getData () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error(error.message);
  }
}

async function addElement (title) {
  const para = document.createElement('li');
  para.textContent = title;
  movieList.append(para);
}

async function addMovies () {
  const data = await getData();
  for (const item of data.results) {
    addElement(item.title);
  }
}

addMovies();
