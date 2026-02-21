import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Image from 'react-bootstrap/Image'

import GetFlag from '../../Functions/GetFlag'
import TranslateCountryCode from '../../Functions/TranslateCountryCode'
import GetIcon from '../../Functions/GetIcon'
import GetPlayerType from '../../Functions/GetPlayerType'

const PersonHeader = ({person}) => {
  const { photo, first_name, last_name, nation, username, player_type  } = person

  return (
    <Container fluid className='border border-3 border-danger rounded p-1 shadow-lg'>
      <Row>
        {photo ? <Image src={photo} alt={`Profile Picture`} style={{ maxWidth: '100px'}} className='m-auto'/> : <div  className='text-success text-center fs-1'>{GetIcon('Courses')}</div>}
      </Row>
      <Row>
        <h4 className='mx-auto mb-0 text-center align-text-bottom'>{first_name} {last_name}</h4>
        <p className=' text-center text-secondary small-text'>{username}</p>
      </Row>
      {/* <Row> 
        <Col className='text-start'>
          <p className='p-1 mb-0'>{GetPlayerType(player_type)}</p>
        </Col>
        <Col className='text-end'>
          <div className='p-1 mb-0'>{GetFlag(TranslateCountryCode(nation, 'map'), 40)}</div>
        </Col>
      </Row> */}
    </Container>    

  )
}

export default PersonHeader
// dob: "Thu, 17 Mar 1994 00:00:00 GMT"
// ​
// email: "azimmerman@pga.com"
// ​
// first_name: "Andrew"
// ​
// gender: "M"
// ​
// handedness: "R"
// ​
// height: 70
// ​
// home_facility: 2967
// ​
// last_name: "Zimmerman"
// ​
// nation: "USA"
// ​
// person_id: 1
// ​
// player_type: "A"
// ​
// units_alt: "FT"
// ​
// units_distance: "Y"
// ​
// units_speed: "MPH"
// ​
// units_temp: "F"
// ​
// units_weight: "LB"
// ​
// username: "azimmer"
// ​
// weight: 210