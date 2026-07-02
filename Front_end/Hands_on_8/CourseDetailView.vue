<template>
  <div class="container">

    <h2>Course Details</h2>

    <div v-if="course" class="card">

      <h3>{{ course.name }}</h3>

      <p><strong>Course Code:</strong> {{ course.code }}</p>

      <p><strong>Credits:</strong> {{ course.credits }}</p>

      <p><strong>Grade:</strong> {{ course.grade }}</p>

      <button @click="enrollCourse">
        Enroll
      </button>

    </div>

    <div v-else>
      <h3>Course Not Found</h3>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const store = useEnrollmentStore()

const course = ref<any>(null)

const courses = [

  {
    id:1,
    name:'Java Programming',
    code:'CS101',
    credits:4,
    grade:'A'
  },

  {
    id:2,
    name:'Database Management System',
    code:'CS102',
    credits:3,
    grade:'A+'
  },

  {
    id:3,
    name:'Web Development',
    code:'CS103',
    credits:4,
    grade:'B+'
  },

  {
    id:4,
    name:'Operating System',
    code:'CS104',
    credits:3,
    grade:'A'
  },

  {
    id:5,
    name:'Computer Networks',
    code:'CS105',
    credits:4,
    grade:'A+'
  }

]

onMounted(() => {

  const id = Number(route.params.id)

  course.value = courses.find(c => c.id === id)

})

function enrollCourse(){

  if(course.value){

    store.enroll(course.value)

    router.push('/profile')

  }

}
</script>

<style scoped>

.container{

    padding:30px;

    text-align:center;

}

.card{

    width:350px;

    margin:auto;

    padding:20px;

    border:1px solid #ccc;

    border-radius:10px;

    box-shadow:0 0 10px lightgray;

}

h2{

    color:palevioletred;

}

button{

    margin-top:20px;

    padding:10px 20px;

    background:palevioletred;

    color:white;

    border:none;

    border-radius:5px;

    cursor:pointer;

}

button:hover{

    opacity:.9;

}

</style>