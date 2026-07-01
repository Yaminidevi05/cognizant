    import { Routes, Route } from "react-router-dom";

    import Header from "./Hands_on_6(4)";
    import HomePage from "./Hands_on_6(5)";
    import CoursesPage from "./Hands_on_6(6)";
    import CourseDetailPage from "./Hands_on_6(8)";
    import ProfilePage from "./Hands_on_6(9)";

    function App() {

    return (

        <>
        <Header />

        <Routes>

            <Route path="/" element={<HomePage />} />

            <Route path="/courses" element={<CoursesPage />} />

            <Route
            path="/courses/:courseId"
            element={<CourseDetailPage />}
            />

            <Route path="/profile" element={<ProfilePage />} />

        </Routes>

        </>
    );
    }

    export default App;