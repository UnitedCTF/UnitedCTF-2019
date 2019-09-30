<template>
  <div class="hand">
    <Card v-for="card in cards" :rank="card.rank" :suit="card.suit" :key="card.rank+card.suit"/>
  </div>
</template>

<script>
import Card from './Card'
export default {
  name: 'Hand',
  props: {
    cards: Array
  },
  components: {
    Card
  }
}
</script>

<style scoped>
.hand {
  display: flex;
  align-items: center;
}
</style>
