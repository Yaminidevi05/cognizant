import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import {
  fetchAllCourses,
  selectCourses,
  selectCoursesLoading,
  selectCoursesError,
} from "../redux/courseSlice";

function CoursesPage() {
  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  if (loading) {
  return (
    <div
      style={{
        textAlign: "center",
        marginTop: "80px",
      }}
    >
      <h2>Loading Courses...</h2>
      <p>Please wait while courses are fetched.</p>
    </div>
  );
}
  

if (error) {
  return (
    <div
      style={{
        textAlign: "center",
        marginTop: "80px",
        color: "red",
      }}
    >
      <h2>Failed to Load Courses</h2>
      <p>{error}</p>
    </div>
  );
}

  return (
  <div
    style={{
      maxWidth: "1100px",
      margin: "30px auto",
      fontFamily: "Arial, sans-serif",
      padding: "20px",
      backgroundColor: "#f4f7fb",
      minHeight: "100vh",
    }}
  >
    <h1
      style={{
        textAlign: "center",
        color: "#1565C0",
        marginBottom: "30px",
      }}
    >
      Course Management
    </h1>

    {courses.slice(0, 10).map((course) => (
      <div
        key={course.id}
        style={{
          background: "#fff",
          borderRadius: "10px",
          padding: "20px",
          marginBottom: "20px",
          boxShadow: "0 2px 8px rgba(0,0,0,0.15)",
        }}
      >
        <h2 style={{ color: "#222" }}>
          Course ID : {course.id}
        </h2>

       <p>
  <strong>Course Name :</strong>{" "}
  {[
    "React Fundamentals",
    "Redux Toolkit",
    "JavaScript Essentials",
    "HTML & CSS Basics",
    "REST API Development",
    "Node.js Basics",
    "Database Fundamentals",
    "Spring Boot Essentials",
    "React Routing",
    "Frontend Project"
  ][(course.id - 1) % 10]}
</p>

<p>
  <strong>Description :</strong>{" "}
  {[
    "Learn React components and hooks.",
    "Manage application state with Redux Toolkit.",
    "Master JavaScript ES6 features.",
    "Build responsive web pages using HTML & CSS.",
    "Develop and consume RESTful APIs.",
    "Learn server-side development with Node.js.",
    "Understand SQL and database concepts.",
    "Build backend applications using Spring Boot.",
    "Implement navigation using React Router.",
    "Create a complete frontend application."
  ][(course.id - 1) % 10]}
</p>
        <p>
          <strong>Instructor :</strong> Cognizant Trainer
        </p>

        <p>
          <strong>Duration :</strong> 6 Weeks
        </p>

        <button
          onClick={() =>
            alert(
              `Enrollment Successful for Course ${course.id}`
            )
          }
          style={{
            background: "#1565C0",
            color: "white",
            border: "none",
            padding: "10px 20px",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Enroll
        </button>
      </div>
    ))}
  </div>
);
}

export default CoursesPage;