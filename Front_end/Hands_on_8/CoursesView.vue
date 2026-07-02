<template>
  <div class="container">

    <h2>Courses</h2>

    <input
      type="text"
      v-model="searchTerm"
      placeholder="Search Course..."
      class="search"
    />

    <div class="course-list">

      <CourseCard
        v-for="course in filteredCourses"
        :key="course.id"
        :id="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
        @enroll="store.enroll(course)"
      />

    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {

  courses.value = [

    {
      id: 1,
      name: 'Java Programming',
      code: 'CS101',
      credits: 4,
      grade: 'A'
    },

    {
      id: 2,
      name: 'Database Management System',
      code: 'CS102',
      credits: 3,
      grade: 'A+'
    },

    {
      id: 3,
      name: 'Web Development',
      code: 'CS103',
      credits: 4,
      grade: 'B+'
    },

    {
      id: 4,
      name: 'Operating System',
      code: 'CS104',
      credits: 3,
      grade: 'A'
    },

    {
      id: 5,
      name: 'Computer Networks',
      code: 'CS105',
      credits: 4,
      grade: 'A+'
    }

  ]

})

const filteredCourses = computed(() => {

  return courses.value.filter(course =>

    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())

  )

})
</script>

<style scoped>

.container{
    padding:20px;
}

h2{
    color:palevioletred;
    text-align:center;
}

.search{

    width:300px;
    padding:10px;
    display:block;
    margin:20px auto;
    border:1px solid gray;
    border-radius:5px;

}

.course-list{

    display:flex;
    flex-wrap:wrap;
    justify-content:center;

}

</style>