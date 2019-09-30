<template>
  <div class="dealer">
    <Hand :cards="dealerHand"/>
  </div>
</template>

<script>
import Hand from './Hand'
import { mapState } from 'vuex'
export default {
  name: 'Dealer',
  computed: mapState([
    'dealerHand'
  ]),
  components: {
    Hand
  }
}
</script>

<style scoped>
.dealer {
  box-sizing: border-box;
  padding-left:160px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-start;
  height: 214px;
  position: relative;
  width:100%;
}
</style>
