<template>
  <div class="menu">
    <Status :text="status"/>
    <div class="bet_container">
      <label for="bet">Insert bet between $0 and $50: </label>
      <input type="text" name="" id="bet" v-model="bet">
    </div>
    <Button label="DEAL" class="blue" @click.native="deal" :disabled="dealDisabled"/>
    <Button label="HIT" class="green" @click.native="hit" :disabled="hitHoldDisabled"/>
    <Button label="HOLD" class="red" @click.native="hold" :disabled="hitHoldDisabled"/>
    <div class="cash">${{ tweenedCash }}</div>
  </div>
</template>

<script>
import Status from './Status'
import Button from './Button'
import gameStates from '../gameStates'
import { mapState, mapActions } from 'vuex'
import TWEEN from '@tweenjs/tween.js'

function animate (time) {
  window.requestAnimationFrame(animate)
  TWEEN.update(time)
}

export default {
  name: 'Menu',
  data () {
    return {
      tweenedCash: 0,
      bet: 10
    }
  },
  watch: {
    cash () {
      const from = { x: this.tweenedCash }
      const to = { x: this.cash }
      new TWEEN.Tween(from)
        .to(to, 1000)
        .easing(TWEEN.Easing.Quadratic.Out)
        .onUpdate(animatedCash => {
          this.tweenedCash = Math.floor(animatedCash.x)
        }).start()
      animate()
    },
    bet () {
      this.$store.commit('setState', { bet: this.bet })
    }
  },
  computed: {
    dealDisabled () {
      return this.state === gameStates.IN_GAME
    },
    hitHoldDisabled () {
      return this.state !== gameStates.IN_GAME
    },
    status () {
      if (this.state === gameStates.IN_GAME) {
        return 'Your turn.'
      }
      if (this.state === gameStates.WON) {
        return 'You won!'
      }
      if (this.state === gameStates.LOST) {
        return 'You lost!'
      }
      if (this.state === gameStates.IDLE) {
        return 'Press Deal to start a new game.'
      }
      if (this.state === gameStates.TIE) {
        return 'It\'s a tie!'
      }
    },
    ...mapState([
      'state',
      'cash'
    ])
  },
  methods: {
    ...mapActions([
      'deal',
      'hit',
      'hold'
    ])
  },
  components: {
    Status,
    Button
  }
}
</script>

<style scoped>
.menu {
  text-align: center;
  background-color: #40434E;
  border-top: 1px solid #070707;
  position: absolute;
  bottom: 0;
  width: 100%;
  padding-top: 10px;
}
.cash {
  position: absolute;
  left: 10px;
  top: 10px;
  font-size: 30px;
  color: lightgreen;
}
.bet_container {
  color: white;
  position: absolute;
  left: 10px;
  top: 50px;
  font-size: 20px;
}
.bet_container > input {
  width: 40px;
  font-size: 20px;
}
</style>
