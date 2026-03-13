import { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Accordion from 'react-bootstrap/Accordion'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Button from 'react-bootstrap/Button'

import InfoDisplay from '../../Functions/InfoDisplay'
import EquipmentUpdate from './EquipmentUpdate'

const EquipmentDetails = ({ item }) => {
  const [edit, setEdit] = useState(false)

  const { club, spec, distance } = item
  const { ss_id } = club
  const { active, make, model, name  } = club

  let clubKeys = ['catagory', 'short_name', 'ss_id', 'year']
  let specKeys = ['loft', 'lie', 'club_length', 'wieght', 'swing_weight', 'club_offset', 'bounce', 'club_head' , 'head_weight', 'shaft', 'shaft_flex', 'shaft_weight', 'grip', 'grip_size', 'grip_weight', 'grip_core_dia']
  let mDistanceKeys = ['manual_max_distance', 'manual_stock_distance', 'manual_knockdown_distance', 'manual_shoulder_distance','manual_hip_distance', 'manual_knee_distance',   'manual_dispersion']
  let cDistanceKeys = ['calc_max_distance', 'calc_stock_distance', 'calc_knockdown_distance', 'calc_shoulder_distance', 'calc_hip_distance',   'calc_knee_distance', 'calc_dispersion']
 
  const getLabel = (key) => {
    switch (key) {
      case 'short_name': return 'SHORT NAME'
      case 'ss_id': return '3RD PARTY ID'
      case 'club_length': return 'LENGTH'
      case 'swing_weight': return 'SWING WEIGHT'
      case 'club_offset': return 'OFFSET'
      case 'club_head': return 'CLUB HEAD'
      case 'head_weight': return 'HEAD WEIGHT'
      case 'shaft_flex': return 'FLEX'
      case 'shaft_weight': return 'SHAFT WEIGHT'
      case 'grip_size': return 'GRIP SIZE'
      case 'grip_weight': return 'GRIP WEIGHT'
      case 'grip_core_dia': return 'GRIP CORE DIAMETER'
      case 'manual_max_distance': return 'MAX SHOT ' 
      case 'manual_stock_distance': return 'STOCK SHOT'
      case 'manual_knockdown_distance': return 'KNOCKDOWN SHOT'
      case 'manual_shoulder_distance': return 'SHOULDER SHOT'
      case 'manual_hip_distance': return 'HIP SHOT'
      case 'manual_knee_distance':return 'KNEE SHOT'
      case 'manual_dispersion': return 'DISPERSION'
      case 'calc_max_distance': return 'MAX SHOT ' 
      case 'calc_stock_distance': return 'STOCK SHOT'
      case 'calc_knockdown_distance': return 'KNOCKDOWN SHOT'
      case 'calc_shoulder_distance': return 'SHOULDER SHOT'
      case 'calc_hip_distance': return 'HIP SHOT'
      case 'calc_knee_distance': return 'KNEE SHOT'
      case 'calc_dispersion': return 'DISPERSION'
      default: return key.toUpperCase()
    }
  }

  const getUnit = (key) => {
    switch (key) {
      case 'loft':  
      case 'lie':  //return <sup>o</sup>
      case'bounce': //return <sup>o</sup>
        return '°'
      case 'club_length':
      case 'club_offset': 
      case 'grip_core_dia': 
      case 'grip_size': 
        return 'in'
      case'wieght':
      case'head_weight':
      case 'shaft_weight':
      case 'grip_weight':
        return 'g'
      default: return ''
    }
  }

  const clubData = clubKeys.map(key => {
    let label = getLabel(key)
    return (
      <>
        {club[key] ? (
          <Col key={`equipment-club-${ss_id}-${key}`}>
              <InfoDisplay data={club[key]} label={label} />
          </Col>
        ) : null }
      </>
    )
  })

  const specData = specKeys.map(key => {
    let label = getLabel(key)
    return (
      <>
        {spec[key] ? (
          <Col xs={6}  md={3} key={`equipment-spec-${ss_id}-${key}`}>
              <InfoDisplay data={`${spec[key]}${getUnit(key)}`} label={label} />
          </Col>
        ) : null }
      </>
    )
  })

  const mDistanceData = mDistanceKeys.map(key => {
    let label = getLabel(key)
    let value = distance[key]
    if (key === 'manual_dispersion') value = value * 100

    return (
      <>
        {distance[key] ? (
          <Col key={`equipment-mDistance-${ss_id}-${key}`}>
              <InfoDisplay data={`${value}${key === 'manual_dispersion' ? '%' : 'yds'}`} label={label} />
          </Col>
        ) : null }
      </>
    )
  })

  const cDistanceData = cDistanceKeys.map(key => {
    let label = getLabel(key)
    let value = distance[key]
    if (key === 'calc_dispersion') value = `${value * 100}%`

    return (
      <>
        {distance[key] ? (
          <Col key={`equipment-cDistance-${ss_id}-${key}`}>
              <InfoDisplay data={`${value}${key === 'calc_dispersion' ? '%' : 'yds'}`} label={label} />
          </Col>
        ) : null }
      </>
    )
  })

  return (
    <Container fluid> 
      <Row className='p-2 mb-0'>
        <Col>
          <h5 className='text-start mb-0'>{name}</h5>
        </Col>        
        <Col>
          <h5 className='mb-0'>{make} {model}</h5>
        </Col>
        <Col>
          <Button className='text-end mb-0' onClick={e => setEdit(!edit)} variant={edit ? 'danger' : 'primary'}>
            {!edit ? 'EDIT CLUB' : 'CANCEL'}
          </Button>
        </Col>
      </Row>
      {!edit ? (
        <>
          <Accordion defaultActiveKey='0'>
            <Accordion.Item eventKey='0'>
              <Accordion.Header className='text-end'>Club Information</Accordion.Header>
              <Accordion.Body>
                <Row>
                  {clubData}
                </Row>
              </Accordion.Body>
            </Accordion.Item>
            <Accordion.Item eventKey='1'>
              <Accordion.Header className='text-end'>Club Specs Information</Accordion.Header>
              <Accordion.Body>
                <Row>
                  {specData}
                </Row>
              </Accordion.Body>
            </Accordion.Item>
            <Accordion.Item eventKey='2'>
              <Accordion.Header className='text-end'>Manual Club Distance Information</Accordion.Header>
              <Accordion.Body>
                <Row>
                  {mDistanceData}
                </Row>
              </Accordion.Body>
            </Accordion.Item>
            <Accordion.Item eventKey='3'>
              <Accordion.Header className='text-end'>Calculated Club Distance Information</Accordion.Header>
              <Accordion.Body>
                <Row>
                  {cDistanceData}
                </Row>
              </Accordion.Body>
            </Accordion.Item>
          </Accordion>
          <small className='text-center'>Data Fields with no value assigned intentionally omitted</small> 
        </>
      ) : <EquipmentUpdate item={item} setEdit={setEdit} getLabel={getLabel} getUnit={getUnit} />}
    </Container>
  )
}

export default EquipmentDetails