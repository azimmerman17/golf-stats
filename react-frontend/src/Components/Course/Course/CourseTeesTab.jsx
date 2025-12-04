import Accordion from 'react-bootstrap/Accordion'
import CourseTeeItem from './CourseTeeItem'

const CourseTeesTab = ({ tees }) => {

  // sort tees by length - desending
  const teesSorted = tees.sort((a, b) =>  b.yards - a.yards)
  
  const accordionItems = teesSorted.map((tee, i) => {
    const { course_id, tee_id} = tee
    return <CourseTeeItem tee={tee} i={i} key={`course-${course_id}-tee-${tee_id}-accordian`} />
  })



  console.log(teesSorted)
  return (
    <Accordion flush>
      {accordionItems}
    </Accordion>
  )
}

export default CourseTeesTab