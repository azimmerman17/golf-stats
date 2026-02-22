// context for the current navigated facility
import { createContext, useState, useEffect } from 'react';

export const HomeCourse = createContext()

const HomeCourseProvider = ({ children }) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const [homeCourse, setHomeCourse] = useState(null)

  useEffect(() => {
    const getCourseFacility = async (id) => {
      let response = await fetch(BASE_URL + '/facility/' + id)
      let facility = await response.json()

      setHomeCourse(facility)
    }

    console.log(typeof homeCourse)
    console.log(homeCourse)

    if (typeof homeCourse === 'number') getCourseFacility(homeCourse)
  }, [homeCourse])

  return (
    <HomeCourse.Provider value={{ homeCourse, setHomeCourse }}>
        {children}
    </HomeCourse.Provider>
  )
}

export default HomeCourseProvider