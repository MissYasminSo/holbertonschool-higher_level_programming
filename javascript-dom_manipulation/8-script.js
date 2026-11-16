#!/usr/bin/node

async function sayFrenchHello () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const helloElement = document.getElementById('hello');
    const result = await response.json();
    helloElement.textContent = result.hello;
  } catch (error) {
    console.error(error.message);
  }
}

sayFrenchHello();
