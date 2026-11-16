#!/usr/bin/node

const header = document.querySelector('header');
const redHeader = document.getElementById('red_header');

function addRed() {
  header.classList.add('red');
}

redHeader.addEventListener('click', addRed);
