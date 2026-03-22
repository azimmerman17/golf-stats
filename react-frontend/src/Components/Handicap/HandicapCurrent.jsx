import { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'

import InfoDisplay from '../../Functions/InfoDisplay'
import GetMonthName from '../../Functions/GetMonthName'

const HandicapCurrent = ({ current, setHandicapContext }) => {
  const [ message, setMessage ] = useState(null)

  if (!current) return 'Loading...'
  const { ghin_number, hard_cap, hi_displsy, low_hi_displsy, rev_date, soft_cap, person_id } = current

  const date_display = (date) => {
    const new_date = new Date(date)

    const year = new_date.getFullYear()
    const month = GetMonthName(new_date.getMonth(), 'long')
    const day = new_date.getDate()

    return `${month} ${day}, ${year}`
  }

  const handleClick = async () => {
    const BASE_URL = import.meta.env.VITE_BACKEND_URL

    const options = {
      method: 'POST',
    }

    let response = await fetch(BASE_URL + `handicap/${person_id}`, options)
    const data = await response.json()

    if (response.status === 200) {
      setHandicapContext({current: null, history: null})
      setMessage(data.msg)
    } else {
      setMessage(data.msg)
    }
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
              <Row>
                  <Button className='w-75 m-auto' variant="primary" onClick={e => handleClick()}>
                    Update Handicap
                  </Button>
                  <p className='text-center my-1'>
                    {message ? message : null}
                  </p>
              </Row>
            </Container>
  )
}

export default HandicapCurrent