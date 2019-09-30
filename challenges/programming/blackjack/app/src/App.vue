<template>
  <div id="app">
    <Table />
    <Menu />
      <Flag />
  </div>
</template>

<script>
import Table from './components/Table'
import Menu from './components/Menu'
import Flag from './components/Flag'

export default {
  name: 'App',
  components: {
    Table,
    Menu,
    Flag
  },
  created () {
    this.$store.dispatch('load')
  }
}
</script>

<style>
html, body, #app {
  font-family: Helvetica, Arial, sans-serif;
  background: rgba(30,66,0,1);
  background: -moz-linear-gradient(top, rgba(30,66,0,1) 0%, rgba(35,161,16,1) 100%);
  background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(30,66,0,1)), color-stop(100%, rgba(35,161,16,1)));
  background: -webkit-linear-gradient(top, rgba(30,66,0,1) 0%, rgba(35,161,16,1) 100%);
  background: -o-linear-gradient(top, rgba(30,66,0,1) 0%, rgba(35,161,16,1) 100%);
  background: -ms-linear-gradient(top, rgba(30,66,0,1) 0%, rgba(35,161,16,1) 100%);
  background: linear-gradient(to bottom, rgba(30,66,0,1) 0%, rgba(35,161,16,1) 100%);
  height: 100%;
  padding: 0;
  margin: 0;
}
button:focus {outline:0;}
</style>
