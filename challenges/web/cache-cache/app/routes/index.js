var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res, next) {
  res.render('index', {
    title: 'Express'
  });
}).post('/', (req, res, next) => {
  const flag = 'flag-8cf5db61531d44dda0d032abdf3c245b';
  let returnValue = req.body.flag === '0' ? 'envoyé!' : flag;
  res.render('index', {
    flag: returnValue
  });
});

module.exports = router;