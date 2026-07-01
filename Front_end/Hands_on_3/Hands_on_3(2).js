import { courses } from "./Hands_on_3.js";

/* Task 30 - Destructuring */

console.log(courses);
document.querySelector(".course-grid").innerHTML = `
    <article style="border:1px solid black;padding:10px;">
        TEST CARD
    </article>
`;
for(const course of courses){

    const { name, credits } = course;

    console.log(name, credits);
}

/* Task 31 - map() */

const formattedCourses = courses.map(
    course =>
    `${course.code} — ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);

/* Task 32 - filter() */

const highCreditCourses =
    courses.filter(course => course.credits >= 4);

console.log(
    "Courses with credits >= 4:",
    highCreditCourses.length
);

/* Task 33 - reduce() */

const totalCredits =
    courses.reduce(
        (sum, course) => sum + course.credits,
        0
    );

console.log("Total Credits:", totalCredits);

/* DOM Selection */

const courseGrid =
    document.querySelector(".course-grid");

const totalCreditsText =
    document.querySelector("#total-credits");

const selectedCourse =
    document.querySelector("#selected-course");

let displayedCourses = [...courses];

/* Render Function */

const renderCourses = (courseArray) => {

    courseGrid.innerHTML = "";

    courseArray.forEach(course => {

        const article =
            document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p><strong>Code:</strong> ${course.code}</p>
            <p><strong>Credits:</strong> ${course.credits}</p>
        `;

        courseGrid.appendChild(article);
    });

    const total =
        courseArray.reduce(
            (sum, course) =>
            sum + course.credits,
            0
        );

    totalCreditsText.textContent =
        `Total Credits: ${total}`;
};

/* Initial Render */

renderCourses(displayedCourses);

/* Search */

document
.querySelector("#search-courses")
.addEventListener("input", (event) => {

    const searchText =
        event.target.value.toLowerCase();

    displayedCourses =
        courses.filter(course =>
            course.name
            .toLowerCase()
            .includes(searchText)
        );

    renderCourses(displayedCourses);
});

/* Sort */

document
.querySelector("#sort-btn")
.addEventListener("click", () => {

    displayedCourses.sort(
        (a,b) =>
        b.credits - a.credits
    );

    renderCourses(displayedCourses);
});

/* Event Delegation */

courseGrid.addEventListener(
    "click",
    (event) => {

        const card =
            event.target.closest(".course-card");

        if(!card){
            return;
        }

        const id =
            Number(card.dataset.id);

        const course =
            courses.find(
                c => c.id === id
            );

        selectedCourse.textContent =
            `Selected Course: ${course.name} | Grade: ${course.grade}`;
    }
);