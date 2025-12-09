import { useContext, useState } from 'react'
import { useFloating, useDismiss, useRole, useClick, useInteractions, useId, FloatingFocusManager, FloatingOverlay, FloatingPortal} from '@floating-ui/react';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button'
import Row from 'react-bootstrap/Row'

import Scorecard from '../../Scorecards/Scorecard';
import CourseScorecardHeader from './CourseScorecardHeader';

const CourseScorecard = ({ tee }) => {
  const [ open, setOpen ] = useState(false)
  const [ gender, setGender] = useState('Male')
  
  const { course_rating, holes, name, hole_count} = tee
  console.log(tee)

  const [rating, setRating] = useState(course_rating.M.filter(r => r.hole_count === hole_count)[0])
  if (!rating) setRating(course_rating.F.filter(r => r.hole_count === hole_count)[0])

  // Floating UI box logic
  const { refs, context } = useFloating({
    open: open,
    onOpenChange: setOpen
  })

  // Set Floating UI Props
  const click = useClick(context)
  const role = useRole(context)
  const dismiss = useDismiss(context, { outsidePressEvent: 'mousedown' })

  const { getReferenceProps, getFloatingProps } = useInteractions([
    click,
    role,
    dismiss
  ]);

  const headingId = useId();
  const descriptionId = useId()
  // Floating UI box logic - end  

  return (
    <>
      <Button variant='danger' ref={refs.setReference} {...getReferenceProps()}>
        View Scorecard
      </Button>
      
      {open ? <FloatingPortal>
          <FloatingOverlay className='Data-Dialog-overlay player-dialog' lockScroll>
            <FloatingFocusManager context={context}>
              <Container className='Data-Dialog' ref={refs.setFloating} aria-labelledby={headingId} aria-describedby={descriptionId} {...getFloatingProps()}>
                <CourseScorecardHeader gender={gender} setGender={setGender} course_rating={course_rating} hole_count={hole_count} name={name} />
                {/* {courseRatings.length > 1 ? (
                  <Row className='text-end'>
                    <Dropdowns  items={courseRatings} color='danger' id='scorecard-gender' align={'end'} current={GetGender(rating.gender)} setCurrent={setRating} />
                  </Row>
                ): null} */}
                <Row className='table-row'>
                 <Scorecard holes={holes} gender={gender} hole_count={hole_count} className='p-1'/>
                </Row>
                <Row>
                  Course Details
                </Row>
              </Container>
            </FloatingFocusManager>
          </FloatingOverlay>
        </FloatingPortal> : null}

    </>
  )
}

export default CourseScorecard