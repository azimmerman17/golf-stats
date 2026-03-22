import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import InfoDisplay from '../../Functions/InfoDisplay'
import GetMonthName from '../../Functions/GetMonthName'

const HandicapHistory = ({ history }) => {
  if (!history) return 'Loading...'
  if (history.length <= 1) return null

  const date_display = (date) => {
    const new_date = new Date(date)

    const year = new_date.getFullYear()
    const month = GetMonthName(new_date.getMonth(), 'long')
    const day = new_date.getDate()

    return `${month} ${day}, ${year}`
  }

  const displayHistory = history.map((h, i) => {
    const { hard_cap, hi_displsy, low_hi_displsy, soft_cap, rev_date } = h
    return (
      <>
        {i > 0 ? <hr className='mx-2 my-0' /> : null}
        <Row >
          <Col><InfoDisplay data={date_display(rev_date)} label={'REVISION DATE'} /></Col>
          <Col><InfoDisplay data={hi_displsy} label={'HANDICAP INDEX'} /></Col>
          <Col><InfoDisplay data={low_hi_displsy} label={'LOW INDEX'} /></Col>
          {hard_cap === 'Y' ? <Col><InfoDisplay data={hard_cap} label={'HARD CAP'} /></Col> : null} 
          {soft_cap === 'Y' ? <Col><InfoDisplay data={soft_cap} label={'SOFT CAP'} /></Col> : null} 
        </Row>
      </>
    )
  })
  return (
    <Container fluid className='m-0 my-2 p-0 w-100 h-100 border border-danger rounded border-2 shadow-lg'>
      {displayHistory}
    </Container>
  )  
}

export default HandicapHistory