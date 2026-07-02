<template>
  <div class="home">
    <h1>Welcome to Student Portal</h1>

    <p>
      This Student Portal is developed using
      <strong>Vue 3 Composition API</strong>,
      <strong>Vue Router</strong> and
      <strong>Pinia</strong>.
    </p>

    <RouterLink to="/courses">
      <button>View Courses</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

.home{
    text-align:center;
    margin-top:80px;
}

h1{
    color:palevioletred;
}

p{
    font-size:18px;
    margin:20px;
}

button{
    background:palevioletred;
    color:white;
    border:none;
    padding:10px 20px;
    border-radius:5px;
    cursor:pointer;
    font-size:16px;
}

button:hover{
    background:#d64d8b;
}

</style>