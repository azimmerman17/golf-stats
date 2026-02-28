import { useContext, useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import EquipmentItem from './EquipmentItem'

const PersonEquipment =({ equipment }) => {
  let activeEquipment = equipment.filter(e => e.club.active == true)
  let inactiveEquipment = equipment.filter(e => e.club.active == false)
  console.log(activeEquipment)

  const activeList = activeEquipment.map(item => {
    const { equipment_id } = item.club

    return (
      <Col xs={1} md={2} className='my-2'key={`Equipment-${equipment_id}`}>
        <EquipmentItem item={item} />
      </Col>
    )
  })

    const inactiveList = inactiveEquipment.map(item => {
    const { equipment_id } = item.club

    return (
      <Col xs={1} md={2} className='my-2' key={`Equipment-${equipment_id}`}>
        <EquipmentItem item={item} />
      </Col>
    )
  })

  return <Container fluid>
    <Row>
      <h6 className='text-end'>Active Clubs</h6>
      {activeList}
      <small className={`text-center${activeEquipment.length > 14 ? ' text-danger' : ''}`}>Total active clubs {activeEquipment.length}</small>

    </Row>
    <hr />
    <Row>
      <h6 className='text-end'>Inactive Clubs</h6>
      {inactiveList}
    </Row>
  </Container>
}

export default PersonEquipment