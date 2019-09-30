var express = require('express')
var bodyParser = require('body-parser')
var rateLimit = require('express-rate-limit')
var app = express()

app.set('view engine', 'ejs')

app.use(express.static('public'))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

database = { 
  "admin@gouv.qc.ca": getRandomCode()
}

app.get('/', (req, res) => {
  res.render('index')
})

app.post('/', (req,res) => {
  res.status(400)
  res.render('index', {error: true})
})

app.get('/forgot', (req, res) => {
  res.render('forgot')
})

app.get('/verify', (req, res) => {
  if (database[req.query.email]) {
    res.render('verify', {email: req.query.email})
  } else {
    res.status(404)
    res.render('forgot', {error: true})
  }
})

app.get('/reset', (req, res) => {
  if (database[req.query.email] && database[req.query.email] == req.query.code) {
      res.send("FLAG-f0rg0ts3cur1ty")
  } else {
    // give error
    res.status(400)
    res.render('verify', {email: req.query.email, error: true})
  }
})


app.listen(3000, function () {
  console.log('app listening on port 3000!')
})

function getRandomCode() {
  return getRandomInt(1000, 10000) 
}
/**
 * Returns a random integer between min (inclusive) and max (inclusive).
 * The value is no lower than min (or the next integer greater than min
 * if min isn't an integer) and no greater than max (or the next integer
 * lower than max if max isn't an integer).
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
