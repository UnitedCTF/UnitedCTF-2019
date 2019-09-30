import Vue from 'vue'
import Vuex from 'vuex'
import api from './api'
import gameStates from './gameStates'
import deck from './deck'

Vue.use(Vuex)

const initialState = {
  state: gameStates.IDLE,
  cash: 10000,
  bet: 10,
  playerHand: [],
  dealerHand: []
}

const store = new Vuex.Store({
  state: initialState,
  getters: {
    playerValue (state) {
      return deck.handValue(state.playerHand)
    },
    dealerValue (state) {
      return deck.handValue(state.dealerHand)
    }
  },
  mutations: {
    resetGame (state) {
      Object.assign(state, initialState)
    },
    setState (state, newState) {
      Object.assign(state, newState)
    }
  },
  actions: {
    getFlag ({ commit }) {
      api
        .get('/flag')
        .then(response => {
          alert(response.data.FLAG)
          commit('setState', response.data)
        })
        .catch(e => {
          alert('Cannot afford $2000 flag.')
        })
    },
    load ({ commit, state }) {
      api.get('/load').then(response => {
        commit('setState', response.data)
      })
    },
    deal ({ commit, state }) {
      api.post('/deal', { bet: state.bet }).then(response => {
        commit('setState', response.data)
      })
    },
    hit ({ commit, state }) {
      api.post('/hit').then(response => {
        commit('setState', response.data)
      })
    },
    hold ({ commit, state }) {
      api.post('/hold').then(response => {
        commit('setState', response.data)
      })
    }
  }
})

export default store
