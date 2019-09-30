const deck = require('../deck')

test('hand values', () => {
  expect(deck.handValue([{ rank: '2', suit: 'hearts' }])).toBe(2)
  expect(deck.handValue([{ rank: '3', suit: 'hearts' }])).toBe(3)
  expect(deck.handValue([{ rank: '4', suit: 'hearts' }])).toBe(4)
  expect(deck.handValue([{ rank: '5', suit: 'hearts' }])).toBe(5)
  expect(deck.handValue([{ rank: '6', suit: 'hearts' }])).toBe(6)
  expect(deck.handValue([{ rank: '7', suit: 'hearts' }])).toBe(7)
  expect(deck.handValue([{ rank: '8', suit: 'hearts' }])).toBe(8)
  expect(deck.handValue([{ rank: '9', suit: 'hearts' }])).toBe(9)
  expect(deck.handValue([{ rank: '10', suit: 'hearts' }])).toBe(10)
  expect(deck.handValue([{ rank: 'J', suit: 'hearts' }])).toBe(10)
  expect(deck.handValue([{ rank: 'Q', suit: 'hearts' }])).toBe(10)
  expect(deck.handValue([{ rank: 'K', suit: 'hearts' }])).toBe(10)
  expect(deck.handValue([{ rank: 'A', suit: 'hearts' }])).toBe(11)
  expect(deck.handValue([{ rank: 'A', suit: 'hearts' },
  { rank: 'A', suit: 'hearts' }
  ])).toBe(12)
  expect(deck.handValue([{ rank: '2', suit: 'hearts' },
  { rank: '3', suit: 'hearts' }
  ])).toBe(5)
})
