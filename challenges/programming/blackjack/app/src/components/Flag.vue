<template>
  <button @click="getFlag" class="flag">⚑</button>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'Flag',
  methods: {
    ...mapActions([
      'getFlag'
    ])
  }
}
</script>

<style scoped>
.flag {
  position: absolute;
  background-color: lightgreen;
  border: none;
  box-shadow: 0px 2px #462;
  color: white;
  border-radius: 100%;
  top: 20px;
  right: 20px;
  font-size: 40px;
  text-align: center;
  vertical-align: center;
  width: 50px;
}
.flag:hover {
  background-color: #afa;
}
.flag:active {
  transform: translate(0px, 2px);
  box-shadow: none;
  border: none;
}
</style>
