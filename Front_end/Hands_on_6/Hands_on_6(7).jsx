import { Link, useNavigate } from "react-router-dom";

function CourseCard({ course }) {

    const navigate = useNavigate();

    function enrollCourse() {

        alert(course.name + " Enrolled");

        navigate("/profile");

    }

    return (

        <div
            style={{
                border: "1px solid black",
                margin: "10px",
                padding: "10px"
            }}
        >

            <h3>{course.name}</h3>

            <p>{course.code}</p>

            <p>{course.credits}</p>

            <Link to={`/courses/${course.id}`}>

                View Details

            </Link>

            <br />

            <button onClick={enrollCourse}>

                Enroll

            </button>

        </div>

    );

}

export default CourseCard;