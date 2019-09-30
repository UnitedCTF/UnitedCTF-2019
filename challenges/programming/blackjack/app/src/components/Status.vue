<template>
  <div class="status">
    {{ text }}
  </div>
</template>

<script>
export default {
  name: 'Status',
  props: ['text']
}
</script>

<style scoped>
.status {
  font-family: Gill Sans;
  text-shadow: 1px 1px 2px rgba(10, 10, 10, 1);
  color: #55acee;
  position: relative;
  opacity: 0.7;
  font-size: 20px;
}
</style>
