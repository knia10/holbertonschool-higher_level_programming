#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (const iter in list) {
    if (list[iter] === searchElement) {
      ocurrences += 1;
    }
  }
  return ocurrences;
};
