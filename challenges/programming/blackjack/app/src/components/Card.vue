<template>
  <div class="card" :class="suitClass">
    <div class="rank top">
      {{ rank }}
    </div>
    <div class="suit">
      {{ suitChar }}
    </div>
    <div class="rank bottom">
      {{ rank }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    rank: {
      type: String,
      validator: (val) => ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'].includes(val)
    },
    suit: {
      type: String,
      validator: (val) => ['diamonds', 'hearts', 'spades', 'clubs'].includes(val)
    }
  },
  computed: {
    suitClass () {
      return {
        diamonds: this.suit === 'diamonds',
        hearts: this.suit === 'hearts',
        spades: this.suit === 'spades',
        clubs: this.suit === 'clubs'
      }
    },
    suitChar () {
      const htmlEntities = {
        'hearts': '♥',
        'diamonds': '♦',
        'clubs': '♣',
        'spades': '♠'
      }
      return htmlEntities[this.suit]
    }

  },
  name: 'Card'
}
</script>

<style scoped>
.card {
  position: relative;
  width: 120px;
  height: 180px;
  border-radius: 5px;
  font-weight: bold;
  font-size: 28px;
  padding:2px;
  background-color: #F6F7EB;
  display: flex;
  -webkit-box-shadow: 2px -2px 9px -1px rgba(0,0,0,1);
  -moz-box-shadow: 2px -2px 9px -1px rgba(0,0,0,1);
  box-shadow: 2px -2px 9px -1px rgba(0,0,0,1);
  margin-right: 15px;
}

.diamonds, .hearts {
  color:#E94F37;
}

.spades, .clubs {
  color:#393E41;
}

.rank {
  position: absolute;
  width:30px;
  height: 28px;
}

.top {
  top: 2px;
  left: 2px;
}

.bottom {
  bottom:0;
  right: 2px;
  text-align: right;
}

.suit {
  margin:auto;
  font-size: 60px;
}
</style>
