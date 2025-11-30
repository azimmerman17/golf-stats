import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'
import GetFlag from '../../../Functions/GetFlag'
import TranslateCountryCode from '../../../Functions/TranslateCountryCode'

const FacilityHeader = ({facility, season}) => {
  const { handle, name, country, state, city } = facility
  const { end_date, start_date, year_round } = season
  return (
    <Container fluid className='border-bottom border-2 border-danger p-1 shadow-lg'>
      <Row>
        <Image src={`https://logos.bluegolf.com/${handle}/profile.png`} alt={`${name} Logo`} style={{ maxWidth: '100px'}} className='m-auto'/>
      </Row>
      <Row>
         <h4 className='mx-auto mb-0 text-center align-text-bottom'>{name}</h4>
         <p className=' text-center text-secondary small-text'>{city}{state ? ` ${state}` : '' }, {country}</p>
      </Row>
      <Row> 
        <Col className='text-start'>
          <p className='mb-0 '>{year_round === true ? 'Year Round' : `${start_date} - ${end_date}`}</p>
          <p className='mb-0 small-text'>Posting Season</p>
        </Col>
        <Col className='text-end'>
          <div >{GetFlag(TranslateCountryCode(country, 'map'), 40)}</div>
          {state ? <div>{GetFlag(`us-${state}`, 40)}</div> : null}
        </Col>
      </Row>
    </Container>    
  )
}

export default FacilityHeader