const fs = require('fs');

require.extensions['.log'] = function (module, filename) {
  module.exports = fs.readFileSync(filename, 'utf8');
};

const logs = require("./generator/requests.log");

let binaryString = "";

logs.split('\n').forEach(element => {
  const request = element.split(' ')[6];
  binaryString += request.charAt(request.length - 1);
});

let text = '';

for (let i = 0; i < binaryString.length; i += 8) {
  let byte = binaryString.substring(i, i + 8);
  while (byte.charAt(0) === '0') {
    byte = byte.substring(1);
  }
  text += String.fromCharCode(parseInt(byte, 2));
}

console.log(text.length)

for (let i = 0; i < text.length; i += 29) {
  const line = text.substring(i, i + 29)
  if (line.includes('flag')) {
    console.log(line)
  }
}