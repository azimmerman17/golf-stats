import { useContext } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { HandicapContext } from '../../Contexts/HandicapContext'

import HandicapCurrent from './HandicapCurrent'
import HandicapCalculator from './HandicapCalculaor'
import HandicapHistory from './HandicapHIstory'

const PersonHandicap = ({ person }) => {
  const { handicapContext, setHandicapContext } = useContext(HandicapContext)

  if (!handicapContext) return 'Loading...'
  const {current, history }= handicapContext

  return (

    <Container fluid>
      <Row className='m-2'>
        <Col md={6}>
         <HandicapCurrent current={current} setHandicapContext={setHandicapContext} />
        </Col>
        <Col md={6}>
          <HandicapCalculator current={current} />
        </Col>
        <Col>
          <HandicapHistory history={history} />
        </Col>
      </Row>
    </Container>
  )
}

export default PersonHandicap