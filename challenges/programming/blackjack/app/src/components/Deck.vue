<template>
  <div class="deck">
    <div class="back" />
  </div>
</template>

<script>
export default {
  name: 'Deck'
}
</script>

<style scoped>
.deck {
  top:60px;
  left:15px;
  z-index: 10;
  position: absolute;
  width: 120px;
  height: 180px;
  border-radius: 5px;
  padding:2px;
  background-color: #F6F7EB;
  display: block;
  -webkit-box-shadow: 2px -2px 9px -1px rgba(0,0,0,1);
  -moz-box-shadow: 2px -2px 9px -1px rgba(0,0,0,1);
  box-shadow: 2px -2px 9px -1px rgba(0,0,0,1);
}

.back {
  background: #36c;
  background:
  linear-gradient(115deg, transparent 75%, rgba(255,255,255,.8) 75%) 0 0,
  linear-gradient(245deg, transparent 75%, rgba(255,255,255,.8) 75%) 0 0,
  linear-gradient(115deg, transparent 75%, rgba(255,255,255,.8) 75%) 7px -15px,
  linear-gradient(245deg, transparent 75%, rgba(255,255,255,.8) 75%) 7px -15px,
  #36c;
  background-size: 15px 30px;
  width:96%;
  height: 98%;
  margin: 1% auto;
  border-radius: 5px;
}
</style>
