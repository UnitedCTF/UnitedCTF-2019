/*@flow*/
exports.getResultsFor = function getResultsFor(_: string | Array<string>) {
  return JSON.stringify({
    results: [
      {
        text: 'SearchPWN is awesome!'
      },
      {
        text: 'Crazy Cat'
      },
      {
        text: 'Crazy Cat'
      },
      {
        text: 'Crazy Cat'
      },
      {
        text: 'Coveo is awesome!'
      }
    ]
  });
};
