#!/usr/bin/node

const ul = document.querySelector('ul');
const addItem = document.getElementById('add_item');

function addElement () {
  const para = document.createElement('li');
  const node = document.createTextNode('Item');
  const exsisting = document.querySelector('li');
  para.appendChild(node);
  ul.insertBefore(para, exsisting);
}

addItem.addEventListener('click', addElement);
