#!/usr/bin/node

function nbOccurences (list, searchElement) {
  return list.reduce((a, i) => i === searchElement ? a + 1 : a, 0);
}

module.exports = { nbOccurences };
