import apiClient from "./apiClient";

export const getAllCourses = async () => {
  await new Promise((resolve) => setTimeout(resolve, 3000));
  return apiClient.get("/posts");
};

export const getCourseById = (id) => {
  return apiClient.get(`/posts/${id}`);
};

export const enrollStudent = (studentId, courseId) => {
  return apiClient.post("/posts", {
    studentId,
    courseId,
  });
};