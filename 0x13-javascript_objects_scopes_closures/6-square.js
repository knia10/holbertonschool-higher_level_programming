#!/usr/bin/node
//  class Square that defines a square and inherits from Square.
const baseClass = require('./5-square');

module.exports = class Square extends baseClass {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let squ = 0; squ < this.height; squ++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
