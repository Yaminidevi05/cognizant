<template>

<div class="card">

    <h3>{{ name }}</h3>

    <p>
        <strong>Course Code :</strong>
        {{ code }}
    </p>

    <p>
        <strong>Credits :</strong>
        {{ credits }}
    </p>

    <p>
        <strong>Grade :</strong>
        {{ grade }}
    </p>

    <div class="buttons">

        <RouterLink :to="'/courses/' + id">
            <button class="details">
                View Details
            </button>
        </RouterLink>

        <button
            class="enroll"
            @click="$emit('enroll')"
        >
            Enroll
        </button>

    </div>

</div>

</template>

<script setup>

import { RouterLink } from 'vue-router'

defineProps({

    id:Number,

    name:String,

    code:String,

    credits:Number,

    grade:String

})

defineEmits(['enroll'])

</script>

<style scoped>

.card{

    width:300px;

    border:1px solid #ddd;

    border-radius:10px;

    padding:20px;

    margin:15px;

    box-shadow:0 0 10px lightgray;

    background:white;

}

h3{

    color:palevioletred;

    margin-top:0;

}

p{

    margin:8px 0;

}

.buttons{

    display:flex;

    justify-content:space-between;

    margin-top:20px;

}

button{

    padding:8px 14px;

    border:none;

    border-radius:5px;

    cursor:pointer;

    color:white;

}

.details{

    background:royalblue;

}

.enroll{

    background:palevioletred;

}

button:hover{

    opacity:.9;

}

</style>