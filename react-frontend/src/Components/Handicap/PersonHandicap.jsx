import { useContext } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { HandicapContext } from '../../Contexts/HandicapContext'

import HandicapCurrent from './HandicapCurrent'

const PersonHandicap = ({ person }) => {
  const { handicapContext, setHandicapContext } = useContext(HandicapContext)

  if (!handicapContext) return 'Loading...'
  const {current, history }= handicapContext

  console.log(handicapContext)
  return (

    <Container fluid>
      <Row className='m-2'>
        <Col md={6}>
         <HandicapCurrent current={current} />
        </Col>
        <Col md={6}>
          <p> course handicap Calculator</p>
        </Col>
        <Col>
          <p>handicap history</p> 
        </Col>
      </Row>
    </Container>
  )
}

export default PersonHandicap