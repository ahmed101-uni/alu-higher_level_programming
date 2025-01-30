#!/usr/bin/node

function esrever (list) {
  const newList = [];
  list.forEach(i => newList.unshift(i));
  return newList;
}

module.exports = { esrever };
