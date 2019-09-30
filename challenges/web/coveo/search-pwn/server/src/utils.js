/*@flow*/
import type { $Request } from 'express';

const fs = require('fs');

function isAdmin(req: $Request) {
  return !!req.cookies.admincookie && req.cookies.admincookie == readFlag(2);
}

function readFlag(flagnumber: number) {
  return fs.readFileSync('./flag'+ flagnumber + '.txt', 'utf8');
}

exports.readFlag = readFlag;
exports.isAdmin = isAdmin;
