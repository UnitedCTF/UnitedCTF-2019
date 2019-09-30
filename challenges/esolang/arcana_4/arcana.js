const fs = require('fs');

require.extensions['.arc'] = function (module, filename) {
  module.exports = fs.readFileSync(filename, 'utf8');
};

const words = require("./program.arc");

const romanCharacters = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
const arabNumbers = [1, 5, 10, 50, 100, 500, 1000];

const stack = [];

words.split('\n').forEach(line => {
  let [instruction, number] = line.split('.');
  number = number.trim();
  switch (instruction) {
    case 'I':
      stack.push(stack.pop() + stack.pop());
      break;
    case 'II':
      stack.push(stack.pop() - stack.pop());
      break;
    case 'III':
      stack.push(stack.pop() * stack.pop());
      break;
    case 'IV':
      stack.push(stack.pop() / stack.pop());
      break;
    case 'V':
      stack.push(stack.pop() & stack.pop());
      break;
    case 'VI':
      stack.push(stack.pop() | stack.pop());
      break;
    case 'VII':
    case 'VIII':
    case 'IX':
    case 'X':
    case 'XI':
    case 'XII':
    case 'XIII':
    case 'XIV':
    case 'XV':
    case 'XVI':
    case 'XVII':
    case 'XVIII':
    case 'XIX':
      console.log('No instructions are associtated to those numbers');
      break;
    case 'XX':
      const characters = []
      while (stack.length) {
        characters.push(String.fromCharCode(stack.pop()));
      }
      console.log(characters.join(''));
      break;
    case 'XXI':
      stack.pop();
      break;
    case 'XXII':
      if (number) {
        stack.push(arabNumbers[romanCharacters.indexOf(number)]);
      }
      break;
    default:
      throw new Error('Not supported');
  }
});