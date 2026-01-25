import { useContext } from 'react' 
import ListGroup from 'react-bootstrap/ListGroup'
import Button from 'react-bootstrap/Button'
import FacilityCourseCard from './FacilityCourseCard'

import { CurrentPage } from '../../../Contexts/CurrentPageContext'

const FacilityCourseTab = ({ course_list }) => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  

    const addCourse = () => {
    return (
      <Button className='w-50 my-2 mx-auto' onClick={e => setCurrentPage('newCourse')}>
        Add new course
      </Button>
    )
  }
  // Response for when the Facility has no courses attached
  if (course_list.msg) {
    return (
      <>
        <p className='text-center m-2'>
          No courses found for this facility.
        </p>
        {addCourse()}
      </>
    )
  }

  // Response for when the Facility has courses attached
  const courses = course_list.map(item => {
    const { course } = item
    const { course_id } = course
    return (
      <FacilityCourseCard course={course} key={`Facility-Course-${course_id}`}/>
    )
  })

  return (
    <>
      <ListGroup variant='flush'>
        {courses} 
      </ListGroup>
      {addCourse()}
    </>
  )
}

export default FacilityCourseTab