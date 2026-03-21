import Card from 'react-bootstrap/Card'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import InfoDisplay from '../../Functions/InfoDisplay'
import GetMonthName from '../../Functions/GetMonthName'

const HandicapCurrent = ({ current }) => {
  const { ghin_number, hard_cap, hi_displsy, low_hi_displsy, rev_date, soft_cap } = current

  const date_display = (date) => {
    const new_date = new Date(date)

    const year = new_date.getFullYear()
    const month = GetMonthName(new_date.getMonth(), 'long')
    const day = new_date.getDate()

    return `${month} ${day}, ${year}`
  }

  return (
            <Container fluid className='m-0 p-0 w-100 h-100 border border-danger rounded border-2 shadow-lg'>
              <Row className='my-2'>
                <h4 className='text-center text-bottom m-0'>Current Handicap</h4>
              </Row>
              <hr className='mx-2 my-0'/>
              <Row>
                <InfoDisplay data={date_display(rev_date)} label={'REVISION DATE'} />
              </Row>
              <Row>
                <Col>
                  <InfoDisplay data={hi_displsy} label={'INDEX'} />
                </Col>
                <Col>
                  <InfoDisplay data={low_hi_displsy} label={'LOW INDEX'} />
                </Col>
              </Row>
              <Row className='text-center' >
                <Col>{hard_cap === 'Y' ? 'HARD CAP' : null}</Col>
                <Col>{soft_cap === 'Y' ? 'SOFT CAP' : null}</Col>
              </Row>
              <Row className='text-center'>
                <Col>
                  <InfoDisplay data={ghin_number} label={'GHIN NUM'} />
                </Col>
              </Row>
            </Container>
  )
}

export default HandicapCurrent