/*@flow*/
import type { $Application, $Request, $Response } from 'express';

const utils = require('./utils');

module.exports = (app: $Application) => {
  app.get('/admin', (req: $Request, res: $Response) => {
    if (!utils.isAdmin(req)) {
      res.sendStatus(404);
      return;
    }
    res.render('admin');
  });
};
