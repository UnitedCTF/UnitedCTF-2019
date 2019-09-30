/* @flow */

const locationHash = location.hash.substr(1);
const queryHash = locationHash
  .substr(locationHash.search(/(?:^|&)q=/))
  .split('&')[0]
  .split('=')[1];
buildResults(queryHash);

function buildResults(query) {
  document.addEventListener('DOMContentLoaded', async () => {
    const template = document.querySelector('.result-template');
    const response = await fetch(`/search?q=${query}`);
    const { results } = await response.json();
    const container = document.querySelector('#result-location');
    if (template instanceof HTMLTemplateElement && container) {
      results.forEach(result => {
        const resultElement = document.importNode(template.content, true);
        if (result.text) {
          const textBox = resultElement.querySelector('.card-text');
          if (textBox) {
            textBox.textContent = result.text;
          }
        }
        if (result.link) {
          const anchorTag = resultElement.querySelector('a');
          if (anchorTag && anchorTag instanceof HTMLAnchorElement) {
            anchorTag.href = result.link;
          }
        }

        container.appendChild(resultElement);
      });
    }
  });
}
