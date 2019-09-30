<template>
  <div class="score">
    {{ label }}: {{ score }}
  </div>
</template>

<script>
export default {
  name: 'Score',
  props: {
    label: {
      type: String,
      default: 'Score'
    },
    score: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style scoped>
.score {
  position: relative;
  text-align: center;
  color: #F6F7EB;
  opacity: 0.7;
  font-size: 20px;
  z-index:10;
  text-shadow: 1px 1px 2px rgba(10, 10, 10, 1);
}
</style>
