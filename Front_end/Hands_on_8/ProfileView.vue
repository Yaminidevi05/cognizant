<template>

<div class="container">

    <h2>Student Profile</h2>

    <h3>Enrolled Courses</h3>

    <div
        v-if="store.enrolledCourses.length > 0"
    >

        <ul>

            <li
                v-for="course in store.enrolledCourses"
                :key="course.id"
            >

                {{ course.name }}

                ({{ course.code }})

                - {{ course.credits }} Credits

                <button
                    @click="store.unenroll(course.id)"
                >
                    Remove
                </button>

            </li>

        </ul>

        <h3>

            Total Credits :

            {{ store.totalCredits }}

        </h3>

    </div>

    <div
        v-else
    >

        <p>No courses enrolled.</p>

    </div>

</div>

</template>

<script setup lang="ts">

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>

<style scoped>

.container{

    padding:30px;

}

h2{

    color:palevioletred;

    text-align:center;

}

ul{

    list-style:none;

    padding:0;

}

li{

    margin:15px 0;

    padding:12px;

    border:1px solid lightgray;

    border-radius:5px;

}

button{

    float:right;

    background:red;

    color:white;

    border:none;

    padding:5px 12px;

    border-radius:5px;

    cursor:pointer;

}

button:hover{

    opacity:.9;

}

h3{

    margin-top:25px;

}

</style>