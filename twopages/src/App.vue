<script setup>
  import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <h1>Ejemplo de uso de Router</h1>
    <a class="button"><router-link to="/page-one">Click for Page 1</router-link></a>&nbsp;
    <a class="button"><router-link to="/page-two">Click for Page 2</router-link></a>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {}
</script>
