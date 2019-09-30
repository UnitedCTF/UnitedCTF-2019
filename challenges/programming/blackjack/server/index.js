const express = require('express')
const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')
const uuidv4 = require('uuid/v4')
const _ = require('lodash')
const morgan = require('morgan')
const cors = require('cors')
const gameStates = require('./gameStates')
const deck = require('./deck')
const app = express()

const CASH = 1000
const FLAG_COST = 2000
const FLAG = 'FLAG-sh0w_m3_th3_m0n3y'

const states = {}
const initialState = {
  state: gameStates.IDLE,
  cash: CASH,
  bet: 10,
  dealerHand: [],
  playerHand: [],
  deck: []
}

app.use(cors({ credentials: true, origin: true }))
app.use(morgan('combined'))
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))
// parse application/json
app.use(bodyParser.json())
app.use(cookieParser())

app.get('/flag', (req, res) => {
  let clientID = req.cookies.clientID
  if (!clientID) {
    clientID = uuidv4()
  }
  if (!states[clientID]) {
    states[clientID] = _.cloneDeep(initialState)
  }
  let gameState = states[clientID]
  if (gameState.cash < FLAG_COST) {
    res.status(403).send(`You need $${FLAG_COST} to buy flag.`)
    return
  }
  gameState.cash -= FLAG_COST
  res.cookie('clientID', clientID).json({
    cash: gameState.cash,
    FLAG
  })
})

app.get('/load', (req, res) => {
  let clientID = req.cookies.clientID
  if (!clientID) {
    clientID = uuidv4()
  }
  if (!states[clientID]) {
    states[clientID] = _.cloneDeep(initialState)
  }
  let gameState = states[clientID]
  res.cookie('clientID', clientID).json({
    state: gameState.state,
    cash: gameState.cash,
    dealerHand: gameState.dealerHand,
    playerHand: gameState.playerHand
  })
})
app.post('/deal', (req, res) => {
  let clientID = req.cookies.clientID
  if (!clientID) {
    clientID = uuidv4()
  }
  if (!states[clientID]) {
    states[clientID] = _.cloneDeep(initialState)
  }
  let gameState = states[clientID]
  if (
    gameState.state === gameStates.WON ||
    gameState.state === gameStates.LOST ||
    gameState.state === gameStates.TIE
  ) {
    gameState.state = gameStates.IDLE
  }
  gameState.dealerHand = []
  gameState.playerHand = []
  if (gameState.state !== gameStates.IDLE) {
    res.status(400).send()
    return
  }
  let bet = parseInt(req.body.bet)
  if (isNaN(bet) || bet < 0 || bet > 50) {
    res.status(400).send()
    return
  }
  if (gameState.cash < bet) {
    res.status(400).send()
    return
  }
  gameState.bet = bet
  if (!gameState.deck || gameState.deck.length < 18) {
    gameState.deck = deck.generateRandomDeck()
  }
  gameState.dealerHand.push(gameState.deck.pop())
  gameState.playerHand.push(gameState.deck.pop())
  gameState.playerHand.push(gameState.deck.pop())
  gameState.state = gameStates.IN_GAME
  gameState.cash -= bet
  const playerValue = deck.handValue(gameState.playerHand)
  const dealerValue = deck.handValue(gameState.dealerHand)
  if (playerValue === 21 && dealerValue < 10) {
    gameState.state = gameStates.WON
    gameState.cash += 3 * bet
  }
  res.cookie('clientID', clientID).json({
    state: gameState.state,
    cash: gameState.cash,
    dealerHand: gameState.dealerHand,
    playerHand: gameState.playerHand
  })
})

app.post('/hit', (req, res) => {
  let clientID = req.cookies.clientID
  if (!clientID) {
    res.status(400).send()
    return
  }
  let gameState = states[clientID]
  if (!gameState || gameState.state !== gameStates.IN_GAME) {
    res.status(400).send()
    return
  }
  gameState.playerHand.push(gameState.deck.pop())
  const playerValue = deck.handValue(gameState.playerHand)
  const dealerValue = deck.handValue(gameState.dealerHand)
  if (playerValue > 21) {
    gameState.state = gameStates.LOST
  }
  res.json({
    state: gameState.state,
    cash: gameState.cash,
    dealerHand: gameState.dealerHand,
    playerHand: gameState.playerHand
  })
})

app.post('/hold', (req, res) => {
  let clientID = req.cookies.clientID
  if (!clientID) {
    res.status(400).send()
    return
  }
  let gameState = states[clientID]
  if (!gameState || gameState.state !== gameStates.IN_GAME) {
    res.status(400).send()
    return
  }
  const playerValue = deck.handValue(gameState.playerHand)
  let dealerValue = deck.handValue(gameState.dealerHand)
  while (dealerValue < 17 && dealerValue <= playerValue) {
    gameState.dealerHand.push(gameState.deck.pop())
    dealerValue = deck.handValue(gameState.dealerHand)
  }
  if (playerValue === dealerValue) {
    gameState.state = gameStates.TIE
    gameState.cash += gameState.bet
  } else if (playerValue === 21) {
    gameState.state = gameStates.WON
    gameState.cash += 2 * gameState.bet
  } else if (dealerValue > 21) {
    gameState.state = gameStates.WON
    gameState.cash += 2 * gameState.bet
  } else if (playerValue > dealerValue) {
    gameState.state = gameStates.WON
    gameState.cash += 2 * gameState.bet
  } else {
    gameState.state = gameStates.LOST
  }
  res.json({
    state: gameState.state,
    cash: gameState.cash,
    dealerHand: gameState.dealerHand,
    playerHand: gameState.playerHand
  })
})

app.get('/debug', (req, res) => {
  res.send(states)
})

app.listen(3000, () => {
  console.log('listening on 3000')
})
