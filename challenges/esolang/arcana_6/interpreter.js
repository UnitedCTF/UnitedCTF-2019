const fs = require('fs');

require.extensions['.mc'] = function (module, filename) {
  module.exports = fs.readFileSync(filename, 'utf8');
};

const lines = require("./program.mc");

const stack = [];

lines.split('\n').forEach(line => {
  line.split(' ').forEach(chicken => {
    const instruction = parseInt(chicken);
    if (instruction >= 10) {
      stack.push(instruction - 10);
    } else {
      switch (instruction) {
        case 0:
          return;
        case 1:
          const chicken = 'chicken'.split('').map(e => e.charCodeAt(0));
          stack.push(...chicken);
          break;
        case 2:
          stack.push(stack.pop() + stack.pop());
          break;
        case 3:
          stack.push(stack.pop() - stack.pop());
          break;
        case 4:
          stack.push(stack.pop() * stack.pop());
          break;
        case 5:
        case 6:
        case 7:
        case 8:
          throw new Error('Not implemented for the challenge');
        case 9:
          console.log(String.fromCharCode(stack.pop()));
          break;
      }
    }
  });
});