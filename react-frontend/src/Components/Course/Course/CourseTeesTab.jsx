import Accordion from 'react-bootstrap/Accordion'
import CourseTeeItem from './CourseTeeItem'

const CourseTeesTab = ({ tees, currentTee, setCurrentTee }) => {
  
  const accordionItems = tees.map(tee => {
    const { course_id, tee_id} = tee
    return <CourseTeeItem tee={tee} key={`course-${course_id}-tee-${tee_id}-accordian`} />
  })

  return (
    <Accordion flush activeKey={currentTee ? currentTee.tee_id : null} onSelect={e => setCurrentTee(tees.filter(t => t.tee_id === e)[0])}>
      {accordionItems}
    </Accordion>
  )
}

export default CourseTeesTab