document.addEventListener("DOMContentLoaded", () => {

    // ===========================
    // COURSE CARD ACCESSIBILITY
    // ===========================

    const courseCards = document.querySelectorAll(".course-card");

    courseCards.forEach((card) => {

        // Mouse Click
        card.addEventListener("click", () => {

            const course =
                card.querySelector("h3").textContent;

            alert("You selected the " + course + " course.");

        });

        // Keyboard Navigation
        card.addEventListener("keydown", (event) => {

            if (
                event.key === "Enter" ||
                event.key === " "
            ) {

                event.preventDefault();

                card.click();

            }

        });

    });


    

    const searchBox =
        document.getElementById("search");

    const resultCount =
        document.getElementById("resultCount");

    searchBox.addEventListener("input", () => {

        const searchValue =
            searchBox.value.toLowerCase();

        let visibleCourses = 0;

        courseCards.forEach((card) => {

            const courseName =
                card.querySelector("h3")
                .textContent
                .toLowerCase();

            if (
                courseName.includes(searchValue)
            ) {

                card.style.display = "block";

                visibleCourses++;

            }

            else {

                card.style.display = "none";

            }

        });

        resultCount.textContent =
            visibleCourses +
            " Courses Found";

    });


   

    const menuButton =
        document.getElementById("menuBtn");

    menuButton.addEventListener("click", () => {

        const expanded =
            menuButton.getAttribute("aria-expanded") === "true";

        menuButton.setAttribute(
            "aria-expanded",
            (!expanded).toString()
        );

        if (!expanded) {

            alert("Navigation Menu Opened");

        }

        else {

            alert("Navigation Menu Closed");

        }

    });


    // ===========================
    // ENROLL BUTTONS
    // ===========================

    const enrollButtons =
        document.querySelectorAll(".course-card button");

    enrollButtons.forEach((button) => {

        button.addEventListener("click", (event) => {

            event.stopPropagation();

            const courseName =
                button.parentElement
                .querySelector("h3")
                .textContent;

            alert(
                "Successfully enrolled in " + courseName +"!");

        });

    });


    // ===========================
    // PROFILE FORM
    // ===========================

    const form =
        document.querySelector("form");

    form.addEventListener("submit", (event) => {

        event.preventDefault();

        const name =
            document.getElementById("name")
            .value
            .trim();

        const email =
            document.getElementById("email")
            .value
            .trim();

        const phone =
            document.getElementById("phone")
            .value
            .trim();

        if (
            name === "" ||
            email === "" ||
            phone === ""
        ) {

            alert(
                "Please fill all the fields."
            );

            return;

        }

        alert(
            "Profile Saved Successfully!"
        );

        form.reset();

    });


    // ===========================
    // FEATURE DETECTION
    // ===========================

    if ("querySelector" in document) {

        console.log(
            "Browser supports querySelector."
        );

    }

    else {

        alert(
            "Your browser may not support all features."
        );

    }


    // ===========================
    // WINDOW LOAD
    // ===========================

    window.addEventListener("load", () => {

        console.log(
            "Student Portal Loaded Successfully."
        );

    });


    // ===========================
    // KEYBOARD FOCUS
    // ===========================

    courseCards.forEach((card) => {

        card.addEventListener("focus", () => {

            console.log(
                card.querySelector("h3").textContent +
                " focused"
            );

        });

    });

});