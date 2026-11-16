#!/usr/bin/node

const character = document.getElementById('character');

async function getData () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    return (result.name);
  } catch (error) {
    console.error(error.message);
  }
}

getData().then(name => {
  character.textContent = name;
});
