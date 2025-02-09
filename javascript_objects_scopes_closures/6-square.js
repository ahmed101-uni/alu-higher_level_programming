#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    c = c ? '' + c : 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
