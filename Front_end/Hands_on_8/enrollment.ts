import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useEnrollmentStore = defineStore('enrollment', () => {

  const enrolledCourses = ref<any[]>([])

  const totalCredits = computed(() => {

    return enrolledCourses.value.reduce(
      (total, course) => total + course.credits,
      0
    )

  })

  function enroll(course: any) {

    const exists = enrolledCourses.value.find(
      c => c.id === course.id
    )

    if (!exists) {
      enrolledCourses.value.push(course)
    }

  }

  function unenroll(courseId: number) {

    enrolledCourses.value =
      enrolledCourses.value.filter(
        course => course.id !== courseId
      )

  }

  return {

    enrolledCourses,

    totalCredits,

    enroll,

    unenroll

  }

})