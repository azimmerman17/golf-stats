import { useState } from 'react'
import Accordion from 'react-bootstrap/Accordion'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import FormGroupTriage from '../Forms/FormGroupTriage';
import EquipmentCatagoryList from '../../Assests/EquipmentCatagoryList';

const EquipmentUpdate = ({ item, setEdit, getLabel, getUnit}) => { 
  console.log(item)
  const { club, distance, spec } = item
  const { ss_id } = club

  const [equipmentClub, setEquipmentClub] = useState(club)
  const [equipmentSpec, setEquipmentSpec] = useState(spec)
  const [equipmentDistance, setEquipmentDistance] = useState(distance)
      // {name: 'Name', type: 'text', placeholder: 'Facility Name', required: true, formText: null, validationText: 'Please enter a name for the facility', field: 'name'},

  let clubKeys = [
    {field: 'make', type: 'text', },
    {field: 'model', type: 'text', },
    {field: 'name', type: 'text', },
    {field: 'catagory', type: 'select', list:EquipmentCatagoryList},
    {field: 'short_name', type: 'text', },
    {field: 'ss_id', type: 'number', },
    {field: 'year', type: 'number', }
  ]
  let specKeys = [
    {field: 'loft', type: 'text'},
    {field: 'lie', type: 'text'},
    {field: 'club_length', type: 'text'},
    {field: 'wieght', type: 'text'},
    {field: 'swing_weight', type: 'text'},
    {field: 'club_offset', type: 'text'},
    {field: 'bounce', type: 'text'},
    {field: 'club_head' , type: 'text'},
    {field: 'head_weight', type: 'text'},
    {field: 'grip', type: 'text'},
    {field: 'grip_size', type: 'text'},
    {field: 'grip_weight', type: 'text'},
    {field: 'grip_core_dia', type: 'text'},
    {field: 'shaft', type: 'text'},
    {field: 'shaft_flex', type: 'text'},
    {field: 'shaft_weight', type: 'text'},
  ]
  let mDistanceKeys = [
    {field: 'manual_max_distance', type: 'text'},
    {field: 'manual_stock_distance', type: 'text'},
    {field: 'manual_knockdown_distance', type: 'text'},
    {field: 'manual_shoulder_distance', type: 'text'},
    {field: 'manual_hip_distance', type: 'text'},
    {field: 'manual_knee_distance', type: 'text'},
    {field: 'manual_dispersion', type: 'text'},
  ]

  const clubData = clubKeys.map(key => {
    const { field } = key
    key.placeholder = club[field]
    key.name = getLabel(field)

    return <FormGroupTriage formData={key} formObj={equipmentDistance} control='editClub' setFormObj={setEquipmentDistance} labelAfter={true} key={`equipment-spec-${ss_id}-${field}`}/>
  })

  const specData = specKeys.map(key => {
    const { field } = key
    key.placeholder = spec[field]
    key.name = getLabel(field)

    return <FormGroupTriage formData={key} formObj={equipmentSpec} control='editClub' setFormObj={setEquipmentSpec} labelAfter={true} key={`equipment-club-${ss_id}-${field}`}/>
  })

  const distanceData = mDistanceKeys.map(key => {
    const { field } = key
    key.placeholder = distance[field]
    key.name = getLabel(field)

    return <FormGroupTriage formData={key} formObj={equipmentSpec} control='editClub' setFormObj={setEquipmentSpec} labelAfter={true} key={`equipment-club-${ss_id}-${field}`}/>
  })

  
  return (
    <Form>
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
          <Accordion.Header className='text-end'>Club Spec Information</Accordion.Header>
          <Accordion.Body>
            <Row>
              {specData}
            </Row>
          </Accordion.Body>   
        </Accordion.Item>
        <Accordion.Item eventKey='2'>
          <Accordion.Header className='text-end'>Club Distance Information</Accordion.Header>
          <Accordion.Body>
            <Row>
              {distanceData}
            </Row>
          </Accordion.Body>   
        </Accordion.Item>
      </Accordion>
      <Button className='mt-2'>
        Save
      </Button>
    </Form>
  )
}

export default EquipmentUpdate