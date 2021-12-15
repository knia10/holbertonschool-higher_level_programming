#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method that prints the rectangle using the character X
  print () {
    for (let rec = 0; rec < this.height; rec++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method called that exchanges the width and the height of the rectangle
  rotate () {
    const change = this.height;
    this.height = this.width;
    this.width = change;
  }

  // instance method called that multiples the width and the height of the rectangle by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
