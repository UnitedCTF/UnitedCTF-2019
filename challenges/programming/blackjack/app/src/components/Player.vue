<template>
  <div class="player">
    <Hand :cards="playerHand"/>
  </div>
</template>

<script>
import Hand from './Hand'
import { mapState } from 'vuex'
export default {
  name: 'Player',
  computed: mapState([
    'playerHand'
  ]),
  components: {
    Hand
  }
}
</script>

<style scoped>
.player {
  display: flex;
  box-sizing: border-box;
  padding-left: 15px;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-start;
  height: 214px;
  position: relative;
  width:100%;
}
</style>
