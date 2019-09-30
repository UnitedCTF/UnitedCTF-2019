/*@flow*/
import type { $Application, $Request, $Response } from 'express';
const Cache = require('memory-cache').Cache
const utils = require('./utils');
const uuid = require('uuid/v4');
const searchIndex = require('./searchIndex');
const fs = require('fs')

const cache = new Cache();


module.exports = (app: $Application) => {
  require('./diagnosticHelpers')(app, cache)


  app.get('/search', (req: $Request, res: $Response) => {
    const query: string = req.query.q instanceof Array ? req.query.q.join('') : req.query.q;
    const isAdmin = utils.isAdmin(req);
    const tag = getTag(req);
    let isNewClientID = false;
    let clientID;

    // FYI: The bot that visits the link that you post on the admin panel, will use the same client id as you
    if (!req.cookies.clientID || !IDisValid(req.cookies.clientID)) {
      isNewClientID = true;
      clientID = generateClientID();
    } else {
      clientID = req.cookies.clientID;
    }

    const requestedBy: string = req.cookies.admincookie ? req.cookies.admincookie : clientID;

    let group: Object | null = cache.get(clientID);
    if (!group) {
      verifyCache();
      group = cache.put(clientID, {});
    }

    let response: string | typeof undefined = group[req.query.q] && group[req.query.q].response;
    if (!response) {
      const results = searchIndex.getResultsFor(req.query.q);
      response = buildResponse(tag, query, isAdmin, results, isNewClientID, clientID);

      verifyGroup(group)
      group[req.query.q] = { response };
    }

    req.connection.write(response, 'utf8', () => req.connection.end());
  });


};


function buildResponse(tag: string, query: string, isAdmin: boolean, results: string, isNewClientID: boolean, clientID: string) {
  return `HTTP/1.1 200 OK\r\nContent-Length: ${Buffer.byteLength(results, 'utf8')}\r\nContent-Type: application/json\r\n${
    isNewClientID ? `Set-Cookie: clientID=${clientID}\r\n` : ''
    }${isAdmin ? `X-Requested-With-Tag: ${tag}\r\n` : ''}\r\n${results}`;
}

function generateClientID() {
  return uuid();
}

function IDisValid(id) {
  const pattern = /[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}/;
  return id.match(pattern);
}

function getTag(req: $Request) {
  if (req.query.withTag) {
    return req.query.withTag instanceof Array ? req.query.withTag.join('') : req.query.withTag;
  }
  return '';
}

function verifyCache() {
  if (cache.size() > 1000) {
    const keys = cache.keys()
    for (let i = 0; i < keys.length / 2; i++) {
      cache.del(keys[i])
    }
  }
}

function verifyGroup(group) {
  const keys = Object.keys(group);
  if (keys.length > 10) {
    for (let i = 0; i < keys.length / 2; i++) {
      delete group[keys[i]]
    }
  }
}
