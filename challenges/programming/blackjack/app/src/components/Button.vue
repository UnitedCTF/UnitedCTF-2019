<template>
  <button>
    {{ label }}
  </button>
</template>

<script>
export default {
  name: 'Button',
  props: ['label']
}
</script>

<style scoped>
button {
  border:none;
  border-radius: 5px;
  padding: 15px 25px;
  font-size: 20px;
  text-decoration: none;
  margin: 20px;
  color: #F6F7EB;
  position: relative;
  display: inline-block;
  font-family: Gill Sans;
  text-shadow: 1px 1px 2px rgba(10, 10, 10, 1);
}

button:active {
  transform: translate(0px, 5px);
  -webkit-transform: translate(0px, 5px);
  box-shadow: 0px .5px 0px 0px;
}

.blue {
  background-color: #55acee;
  box-shadow: 0px 5px 0px 0px #3C93D5;
}

.blue:hover {
  background-color: #6FC6FF;
}

.green {
  background-color: #2ecc71;
  box-shadow: 0px 5px 0px 0px #15B358;
}

.green:hover {
  background-color: #48E68B;
}

.red {
  background-color: #e74c3c;
  box-shadow: 0px 5px 0px 0px #CE3323;
}

.red:hover {
  background-color: #FF6656;
}

button:disabled {
  background-color: #999;
  box-shadow: 0px 5px 0px 0px #AAA;
}

button:disabled:hover {
  background-color: #999;
}

button:disabled:active {
  transform: translate(0px, 0px);
  -webkit-transform: translate(0px, 0px);
  box-shadow: 0px 5px 0px 0px #AAA;
}
</style>
