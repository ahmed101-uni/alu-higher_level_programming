#!/usr/bin/node
function converter (base) {
  return n => n.toString(base);
}

module.exports = { converter };
