import data from "./Hands_on_6(2)";
import CourseCard from "./Hands_on_6(7)";

function CoursesPage() {

    return (

        <div>

            <h2>Courses</h2>

            {

                data.map(course => (

                    <CourseCard
                        key={course.id}
                        course={course}
                    />

                ))

            }

        </div>

    );

}

export default CoursesPage;