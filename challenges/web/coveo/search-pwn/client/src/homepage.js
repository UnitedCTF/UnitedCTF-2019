/* @flow */
import { docCookies } from './cookie.js';

declare var M;

if (!docCookies.hasItem('username')) {
  docCookies.setItem('username', 'user' + getRandomNumbers().join(''));
}

function getRandomNumbers(n = 8) {
  const numbers = [];
  for (let i = 0; i < n; i++) {
    numbers.push(Math.floor(Math.random() * 11));
  }
  return numbers;
}

document.addEventListener('DOMContentLoaded', () => {
  const elems = document.querySelectorAll('.modal');
  M.Modal.init(elems);

  const searchForm = document.querySelector('.search-form');

  searchForm &&
    searchForm.addEventListener('submit', (e:Event, ) => {
      e.preventDefault() && e.stopPropagation();
      const searchInput = document.querySelector('.search-input');
      const query = searchInput && searchInput instanceof HTMLInputElement ? searchInput.value : '';
      const encodedQuery = encodeQuery(query);
      const currentURL = new URL(window.location);
      window.location.replace(`/search-results#q=${encodedQuery}`);
    });

  const subscribeForm = document.querySelector('.subscribe-form');

  subscribeForm &&
    subscribeForm.addEventListener('submit', async (e:Event, ) => {
      e.preventDefault();
      e.stopPropagation();
      const subscribeEmailInput = document.querySelector('.subscribe-email-input');
      if (subscribeEmailInput && subscribeEmailInput instanceof HTMLInputElement) {
        const email = subscribeEmailInput.value;
        const response = await fetch(`/subscribe?email=${email}`);
        const html = await response.text();
        M.toast({ html });
        subscribeEmailInput.value = '';
      }
    });
});

function encodeQuery(query: string) {
  let encodedQuery: string;
  try {
    encodedQuery = encodeURIComponent(query);
  } catch (_) {
    encodedQuery = '';
  }
  return encodedQuery;
}
