/**
 * Shuffles array in place. ES6 version
 * @param {Array} a items An array containing the items.
 */
function shuffle (a) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

module.exports = {
  generateRandomDeck () {
    const ranks = [
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '9',
      '10',
      'J',
      'Q',
      'K',
      'A'
    ]
    const suits = ['hearts', 'spades', 'clubs', 'diamonds']
    const cards = []

    for (const rank of ranks) {
      for (const suit of suits) {
        const card = {
          rank,
          suit
        }
        cards.push(card)
      }
    }
    shuffle(cards)
    return cards
  },
  handValue (hand) {
    const values = {
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9,
      '10': 10,
      J: 10,
      Q: 10,
      K: 10,
      A: 1
    }
    let value = 0
    for (const card of hand) {
      value += values[card.rank]
    }
    for (const card of hand) {
      if (card.rank === 'A' && value < 12) {
        value += 10
      }
    }
    return value
  }
}
