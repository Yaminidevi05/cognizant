import { useParams } from "react-router-dom";
import data from "./Hands_on_6(2)";

function CourseDetailPage() {

    const { courseId } = useParams();

    const course = data.find(
        (c) => c.id === Number(courseId)
    );

    if (!course) {
        return <h2>Course Not Found</h2>;
    }

    return (

        <div>

            <h2>Course Details</h2>

            <p><b>Name:</b> {course.name}</p>

            <p><b>Code:</b> {course.code}</p>

            <p><b>Credits:</b> {course.credits}</p>

            <p><b>Grade:</b> {course.grade}</p>

        </div>

    );

}

export default CourseDetailPage;