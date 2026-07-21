import {
  createSlice,
  createAsyncThunk,
} from "@reduxjs/toolkit";

import { getAllCourses } from "../api/courseApi";

export const fetchAllCourses = createAsyncThunk(
  "courses/fetchAll",

  async (_, thunkAPI) => {
    try {
      return await getAllCourses();
    } catch (error) {
      return thunkAPI.rejectWithValue(error.message);
    }
  }
);

const courseSlice = createSlice({
  name: "courses",

  initialState: {
    courses: [],
    loading: false,
    error: null,
  },

  reducers: {},

  extraReducers: (builder) => {
    builder

      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload;
      })

      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const selectCourses = (state) => state.courses.courses;

export const selectCoursesLoading = (state) =>
  state.courses.loading;

export const selectCoursesError = (state) =>
  state.courses.error;

export default courseSlice.reducer;