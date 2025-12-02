import ListGroup from 'react-bootstrap/ListGroup';
import FacilityCourseCard from './FacilityCourseCard';

const FacilityCourseTab = ({ course_list }) => {

  // Response for when the Facility has no courses attached
  if (course_list.msg) {
    return (
      <p className='text-center m-2'>
        No courses found for this facility.
      </p>
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
    <ListGroup variant='flush'>
      {courses} 
    </ListGroup>
  )
}

export default FacilityCourseTab