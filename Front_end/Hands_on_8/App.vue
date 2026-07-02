<template>
  <div>
    <Header />

    <RouterView />
  </div>
</template>

<script setup lang="ts">
import Header from './components/Header.vue'
import { RouterView } from 'vue-router'
</script>

<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:Arial, Helvetica, sans-serif;
}

body{
  background:#f5f5f5;
}
</style>