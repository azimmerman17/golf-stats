import { useContext } from 'react'
import Container from 'react-bootstrap/Container'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

import { HomeCourse } from '../../Contexts/HomeCourseContext'

import InfoDisplay from '../../Functions/InfoDisplay'
import GetGender from '../../Functions/GetGender'
import ConvertHeight from '../../Functions/ConvertHeight'
import ConvertWeight from '../../Functions/ConvertWeight'
import GetPlayerType from '../../Functions/GetPlayerType'
import FormatDate from '../../Functions/FormatDate'
import GetFlag from '../../Functions/GetFlag'
import TranslateCountryCode from '../../Functions/TranslateCountryCode'


const PersonBio = ({ person }) => {
  const {homeCourse, setHomeCourse} = useContext(HomeCourse)
  const {dob, email, gender, handedness, height, home_facility, nation, player_type, weight, units_height, units_weight} = person

  if (!homeCourse) setHomeCourse(home_facility)
  if (!homeCourse.course) return 'Loading...'
  const { name } = homeCourse.facility


  const dataList = [
    {data: FormatDate(dob, true, 'long', false), label: 'DATE OF BIRTH'},
    {data: email, label: 'EMAIL ADDRESS'},
    {data: GetGender(gender), label: 'GENDER'},
    {data: handedness === 'R' ? 'Right' : 'Left', label: 'HANDEDNESS'},
    {data: ConvertHeight(height, 'IN', units_height), label: 'HEIGHT'},
    {data: `${ConvertWeight(weight, 'LB', units_weight)} ${units_weight.toLowerCase()}`, label: 'WEIGHT'},
    {data: GetFlag(TranslateCountryCode(nation, 'map'), 40), label: 'COUNTRY'},
    {data: GetPlayerType(player_type), label:'PLAYER TYPE'},
    {data: name, label:'HOME COURSE'}
  ]

  const display = dataList.map(item => {
    const { data, label }= item

    return (
      <Col xs={6} key={`Person-Bio-Tab-${label}`}>
        <InfoDisplay data={data} label={label} />
      </Col>
    )
  })

  return (
    <Container fluid>
      <Row>
        {display}
      </Row>
    </Container>
  )
}

export default PersonBio
