<template>
  <div class="table">
    <Deck />
    <Score label="Dealer score" :score="dealerValue"/>
    <Dealer />
    <div class="border-line"/>
    <Score label="Player score" :score="playerValue"/>
    <Player />
  </div>
</template>

<script>
import Dealer from './Dealer'
import Deck from './Deck'
import Player from './Player'
import Score from './Score'
import { mapGetters } from 'vuex'

export default {
  name: 'Table',
  data () {
    return {
      score: 0
    }
  },
  computed: {
    ...mapGetters([
      'playerValue',
      'dealerValue'
    ])
  },
  components: {
    Dealer,
    Deck,
    Player,
    Score
  }
}
</script>

<style scoped>
.table {
  position: relative;
  padding-top: 20px;
}
.border-line {
  border:4px dashed #F6F7EB;
  opacity: 0.4;
  margin: 20px 0;
}
</style>
