/*@flow*/
import type { $Application, $Request, $Response } from 'express';
import type { CacheClass } from 'memory-cache'

const fs = require('fs')

module.exports = function (app: $Application, cache: CacheClass) {

  app.get('/debug/*', (req: $Request, res, next) => {
    if (tokenIsValid(req)) {
      next();
    } else {
      res.sendStatus(403)
    }
  });

  app.get('/debug/cache', (req: $Request, res) => {
    res.send(cache.exportJson());
  })

  app.get('/debug/stats', (req: $Request, res) => {
    res.send(`cache size: ${cache.size().toString()}\n
      memory used (mb): ${process.memoryUsage().heapUsed / 1024 / 1024}`)
  })

  app.get('/debug/clear-group', (req: $Request, res) => {
    if (cache.del(req.query.group)) {
      res.send('deleted')
    } else {
      res.send('not deleted')
    }
  })

  app.get('/debug/clear-cache', (req: $Request, res) => {
    cache.clear()
    res.send(cache.size().toString)
  })

  function tokenIsValid(req: $Request) {
    const token: string = req.query.token instanceof Array ? req.query.token.join('') : req.query.token;
    return token == fs.readFileSync('./token.txt', 'utf8')
  }
}