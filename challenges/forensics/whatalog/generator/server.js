const express = require('express');
const morgan = require('morgan');
const fs = require('fs');
const path = require('path');

const app = express();

const stream = fs.createWriteStream(path.join(__dirname, 'requests.log'));

app.use(morgan('combined', {
  stream,
}));

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(3000, () => {
  console.log('logger is ready');
})