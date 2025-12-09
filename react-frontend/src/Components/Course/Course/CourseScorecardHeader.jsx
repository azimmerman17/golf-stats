import { useEffect, useState } from 'react'
import Row from 'react-bootstrap/Row'

import Dropdowns from '../../Home/Dropdowns'

const CourseScorecardHeader = ({ gender, setGender, course_rating, hole_count, name }) => {
  let courseRatings = []
  
  if (course_rating) {
    if (course_rating.M.length > 0) courseRatings.push({name: 'Male', selected: 'Male'})
    if (course_rating.F.length > 0) courseRatings.push({name: 'Female', selected: 'Female'})
  }
    
  const [rating, setRating] = useState({})
      
  useEffect(() => {
    if (rating.name !== gender) {
      if (gender === 'Male') setRating(course_rating.M.filter(r => r.hole_count === hole_count)[0])
      else setRating(course_rating.F.filter(r => r.hole_count === hole_count)[0])

    }
    }, [gender])
  console.log(course_rating)
  return (
    <>
      {courseRatings.length > 1 ? (
        <Row className='text-end'>
          <Dropdowns  items={courseRatings} color='danger' id='scorecard-gender' align={'end'} current={gender} setCurrent={setGender} />
        </Row>
      ): null}
      <Row>
        <h5 className='text-start'>
          {name}
        </h5>
        <p className='text-end text-subtle text-secondary'><small>
          Course Rating: {rating.course_rating} Slope: {rating.slope}
        </small></p>
      </Row>
    </>
  )

}

export default CourseScorecardHeader