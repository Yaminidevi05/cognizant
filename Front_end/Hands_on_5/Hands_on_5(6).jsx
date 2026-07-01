import { useEffect, useState } from "react";

import Header from "./Hands_on_5(2)";
import Footer from "./Hands_on_5(3)";
import CourseCard from "./Hands_on_5(4)";
import StudentProfile from "./Hands_on_5(5)";

import data from "./Hands_on_5(1)";

function App() {

  const [courses, setCourses] = useState(data);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {

    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((res) => res.json())
      .then((result) => {

        const newCourses = result.slice(0,5).map((item) => ({
          id: item.id,
          name: item.title,
          code: "CS" + item.id,
          credits: 3,
          grade: "A"
        }));

        setCourses(newCourses);
        setLoading(false);
      })

      .catch(() => {
        setError("Failed to fetch courses");
        setLoading(false);
      });

  }, []);

  // Runs whenever courses changes.
  // Dependency array prevents it from running after every render.
  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  const handleEnroll = (id) => {

    const course = courses.find((c) => c.id === id);

    if (
      course &&
      !enrolledCourses.some((c) => c.id === id)
    ) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>

      <Header
        siteName="Student Portal"
        count={enrolledCourses.length}
      />

      <input
        type="text"
        placeholder="Search Course"
        value={searchTerm}
        onChange={(e) =>
          setSearchTerm(e.target.value)
        }
      />

      <br /><br />

      {loading && <h2>Loading...</h2>}

      {error && <h2>{error}</h2>}

      {!loading &&
        filteredCourses.map((course) => (
          <CourseCard
            key={course.id}
            {...course}
            onEnroll={handleEnroll}
          />
        ))}

      <StudentProfile />

      <Footer />

    </>
  );
}

export default App;