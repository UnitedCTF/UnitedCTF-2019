/* @flow */
import type { $Request, $Response } from 'express';
import type { Browser } from 'puppeteer';

const utils = require('./utils');
const cors = require('cors');
const express = require('express');
const cookieParser = require('cookie-parser');
const puppeteer = require('puppeteer');
const escape = require('escape-html');
const pug = require('pug');
const { URL } = require('url');
const fs = require('fs');

let browser;

const app = express();
app.use(cookieParser());
app.use(cors());
app.use(express.static('bin-client'));
app.use('/materialize', express.static('libs/materialize'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set('views', './views');
app.set('view engine', 'pug');

require('./search.js')(app);
require('./admin.js')(app);

app.get('/*', (req: $Request, res, next) => {
  res.header('X-XSS-Protection', '0');
  next();
});

app.get('/', (req: $Request, res: $Response) => {
  res.render('index', { isAdmin: utils.isAdmin(req), flag: utils.readFlag(1) });
});

app.get('/report-form', (req: $Request, res: $Response) => {
  res.render('report-form');
});

app.get('/search-results', (req: $Request, res: $Response) => {
  if (!req.query.q) {
    req.query.q = '';
  }
  res.render('search-results', { query: req.query.q });
});

app.get('/report-bug', async (req: $Request, res: $Response) => {
  if (!req.query.url || req.query.url instanceof Array || !req.query.description) {
    denyBugReport(res);
    return;
  }

  let url;
  try {
    url = new URL(req.query.url);
  } catch (_) {
    denyBugReport(res);
    return;
  }

  if (!urlHostMatches(req, url)) {
    denyBugReport(res);
    return;
  }

  triggerAdminVisit(url, req.hostname);
  res.render('successful-bug-report');
});

app.get('/subscribe', (req: $Request, res: $Response) => {
  if (!req.query.email) {
    res.render('subscribe-error');
  } else {
    res.render('subscribe-confirm', { email: req.query.email });
  }
});

app.get('/newsboard', async (req: $Request, res: $Response) => {
  if (!req.query.url || req.query.url instanceof Array) {
    denyNewMessage(res);
  } else {
    let url;
    try {
      url = new URL(req.query.url);
    } catch (_) {
      denyNewMessage(res);
      return;
    }

    if (!urlHostMatches(req, url)) {
      res.render('foreign-website');
      return;
    }

    if (!urlIsSearchResults(url)) {
      res.render('not-search-results-page');
      return;
    }
    const clientID = req.cookies.clientID ? req.cookies.clientID : '';
    const resultOrderIsCorrect = await isResultsOrderCorrect(url, req.hostname, clientID);
    if (resultOrderIsCorrect) {
      res.render('second-flag', { flag: utils.readFlag(3) });
    } else {
      res.render('news-published');
    }
  }
});

app.use('/search.js', express.static('./server/src/search.js'));

const server = app.listen(3000, '0.0.0.0', async () => {
  browser = await startBrowser();
  console.log('Server running on port 3000');
});

process.on('SIGTERM', () => {
  server &&
    server.close(async () => {
      if (browser) {
        await browser.close();
      }
    });
});

async function triggerAdminVisit(link: URL, domain: string) {
  link.host = 'localhost:3000';
  try {
    const page = await initNewPage(browser);
    await page.setCookie({
      name: 'admincookie',
      value: utils.readFlag(2),
      path: '/',
      domain: 'localhost:3000',
      httpOnly: false
    });
    await page.goto(link.toString(), { waitUntil: 'networkidle0' });
    await page.close();
  } catch (e) {
    console.log(`Error occured during admin visit: ${e}`);
  }
}

async function isResultsOrderCorrect(link: URL, domain: string, clientID: string) {
  let resultOrderIsCorrect = false;
  link.host = 'localhost:3000';
  try {
    browser = await startBrowser();
    const page = await initNewPage(browser);
    await page.setCookie({
      name: 'clientID',
      value: clientID,
      path: '/',
      domain: 'localhost'
    });
    await page.goto(link.toString(), { waitUntil: 'networkidle0' });
    const firstResultText = await page.$eval('.result-container', firstResult => firstResult && firstResult.textContent);
    if (firstResultText) {
      resultOrderIsCorrect = firstResultText == 'Coveo is awesome!';
    }
    await page.close();
  } catch (e) {
    console.log(`Error occured during user visit: ${e}`);
  } finally {
    return resultOrderIsCorrect;
  }
}

function urlHostMatches(req: $Request, url: URL) {
  return req.hostname == url.hostname;
}

function urlIsSearchResults(url: URL) {
  return url.pathname == '/search-results';
}

async function startBrowser() {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox','--disable-xss-auditor']
  });
  return browser;
}

async function initNewPage(broswer: Browser) {
  const newPage = await broswer.newPage();
  newPage.on('console', msg => console.log('PAGE LOG:', msg.text()));
  return newPage;
}

function denyBugReport(res: $Response) {
  res.render('denied-bug-report');
  return;
}

function denyNewMessage(res: $Response) {
  res.render('news-denied');
}
