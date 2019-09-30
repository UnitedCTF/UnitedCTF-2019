const fs = require('fs');

require.extensions['.csv'] = function (module, filename) {
  module.exports = fs.readFileSync(filename, 'utf8');
};

const dataset = require("./dataset.csv");

const [header, ...entries] = dataset.split('\r\n');

const weekDays = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'];

let total = 0.0;

entries.forEach(entry => {
  const current = entry.split(',');
  // console.log(current[2])
  // console.log(current[12])
  // console.log(current[1])
  if (current[2] === 'Ligne orange' && weekDays.includes(current[12]) && current[1] === '73') {
    total += parseFloat(current[14]);
  }
});

console.log(Math.round(total));