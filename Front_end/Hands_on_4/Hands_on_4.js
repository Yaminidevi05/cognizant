import { courses } from "./Hands_on_4(2).js";
function fetchUser(id){
fetch("https://jsonplaceholder.typicode.com/users/" + id)
.then(response=>response.json())
.then(user=>{
console.log(user.name);
});
}
fetchUser(1);
async function fetchUserAsync(id){
try{
const response=await fetch("https://jsonplaceholder.typicode.com/users/"+id);
const user=await response.json();
console.log(user.name);
}
catch(error){
console.log(error);
}
}
fetchUserAsync(1);
function fetchAllCourses(){
return new Promise(resolve=>{
setTimeout(()=>{
resolve(courses);
},1000);
});
}
const courseContainer=document.getElementById("courseContainer");
courseContainer.innerHTML="<h3>Loading courses...</h3>";
fetchAllCourses()
.then(data=>{
courseContainer.innerHTML="";
data.forEach(course=>{
courseContainer.innerHTML+=`
<div class="course-card">
<h3>${course.title}</h3>
<p>${course.instructor}</p>
<p>${course.category}</p>
</div>
`;
});
});
Promise.all([
fetch("https://jsonplaceholder.typicode.com/users/1").then(res=>res.json()),
fetch("https://jsonplaceholder.typicode.com/users/2").then(res=>res.json())
])
.then(users=>{
console.log(users[0].name);
console.log(users[1].name);
});
async function apiFetch(url){
const response=await fetch(url);
if(!response.ok){
throw new Error("Unable to load data");
}
return await response.json();
}
const postsContainer=document.getElementById("postsContainer");
async function loadPosts(){
const posts=await apiFetch("https://jsonplaceholder.typicode.com/posts");
postsContainer.innerHTML="";
const notifications = [
    {
        title: "JavaScript Assignment",
        body: "Complete the Async JavaScript hands-on before Friday."
    },
    {
        title: "Frontend Workshop",
        body: "Attend the frontend workshop at 10:00 AM tomorrow."
    },
    {
        title: "Project Submission",
        body: "Upload your project files to the portal before the deadline."
    },
    {
        title: "Database Lab",
        body: "Practice MySQL joins and indexes for the upcoming lab."
    },
    {
        title: "React Session",
        body: "Learn React components and state management today."
    },
    {
        title: "Placement Training",
        body: "Aptitude and coding practice starts at 2:00 PM."
    },
    {
        title: "Cloud Computing",
        body: "Introduction to AWS services will be covered today."
    },
    {
        title: "Python Practice",
        body: "Solve five Python programming problems."
    },
    {
        title: "Interview Preparation",
        body: "Revise JavaScript promises and async/await concepts."
    }
];
postsContainer.innerHTML = "";
notifications.forEach(post => {
postsContainer.innerHTML += `
<div class="post-card">
    <h3>${post.title}</h3>
    <p>${post.body}</p>
</div>
`;
});
}
const loading=document.getElementById("loading");
async function fetchPosts(){
loading.innerHTML="<p class='spinner'>Loading...</p>";
await loadPosts();
loading.innerHTML="";
}
fetchPosts();
const error=document.getElementById("error");
const retryBtn=document.getElementById("retryBtn");
async function loadWithError(){
try{
loading.innerHTML="Loading...";
error.innerHTML="";
retryBtn.style.display="none";
await apiFetch("https://jsonplaceholder.typicode.com/nonexistent");
loading.innerHTML="";
}
catch(err){
loading.innerHTML="";
error.innerHTML="Something went wrong while loading notifications.";
retryBtn.style.display="block";
}
}
loadWithError();
retryBtn.addEventListener("click",async()=>{
loading.innerHTML="Loading...";
error.innerHTML="";
retryBtn.style.display="none";
await loadPosts();
loading.innerHTML="";
});
async function apiFetchAxios(url){
const response=await axios.get(url);
return response.data;
}
async function getUserPosts(){
const response=await axios.get(
"https://jsonplaceholder.typicode.com/posts",
{
params:{
userId:1
}
}
);
console.log(response.data);
}
getUserPosts();
axios.interceptors.request.use(config=>{
console.log("API call started: "+config.url);
return config;
});