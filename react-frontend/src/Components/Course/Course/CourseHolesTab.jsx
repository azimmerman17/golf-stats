import { useEffect, useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/esm/Col'
import Button from 'react-bootstrap/esm/Button'

import Dropdowns from '../../Home/Dropdowns'
import CourseHoleDetails from './CourseHoleDetails'
import HoleMap from '../../Map/HoleMap'
import CourseMap from '../../Map/CourseMap'

const CourseHolesTab = ({ tees, gps, currentTee, setCurrentTee }) => {
  const [currentHole, setCurrentHole] = useState({
                                                  male: currentTee.holes.M.filter(g => g.number === 1)[0], 
                                                  female: currentTee.holes.F.filter(g => g.number === 1)[0], 
                                                  teeName: currentTee.name
                                                })
  const [currentMap, setCurrentMap] = useState(gps.filter(g => g.number == 1)[0])   
  const [displayMap, setdisplayMap] = useState('Hole')

  useEffect(() => {
    const setHoleDetails = (g, h) => {
      const { meters, number, yards, hole_id } = g
      h = {...h, meters, number, yards, hole_id}
      setCurrentHole(h)
      setCurrentMap(gps.filter(g => g.number == number)[0])
    } 

    const { hole_id, teeName, male, female } = currentHole
    if (!hole_id || teeName !== currentTee.name) {
      let newHole = {
        male, 
        female, 
        teeName: currentTee.name
      }

      if (newHole.male) setHoleDetails(newHole.male, newHole)
      else setHoleDetails(newHole.female, newHole) 
    }
  }, [currentHole, currentTee])
  
  // Build Dropdowns
  let teeDropdown = []
  tees.forEach(t => {teeDropdown.push({name: t.name, selected: t})})
  let holeDropdown = []

  gps.forEach(h => {holeDropdown.push({name: `Hole ${h.number}`, selected: {male: currentTee.holes.M.filter(g => g.number === h.number)[0], female: currentTee.holes.F.filter(g => g.number === h.number)[0]}})})

  const handleMapClick = (display) => {
    if (display === 'Hole') setdisplayMap('Course')
    else setdisplayMap('Hole')
  }

  return (
    <Container fluid>
      <Row className='my-1 text-center'>
        <Col>
          <Dropdowns items={teeDropdown} color={'white'} id={'tee-dropdown'} align='start' current={currentTee ? currentTee.name : teesSorted[0].name} setCurrent={setCurrentTee} />
          <p className='text-muted mb-0'><small>TEE</small></p>
        </Col>
        <Col>
          <Dropdowns items={holeDropdown} color={'white'} id={'hole-dropdown'} align='end' current={`Hole ${currentHole.number}`} setCurrent={setCurrentHole} />
          <p className='text-muted mb-0'><small>HOLE</small></p>
        </Col>
      </Row>
      <hr className='text-danger' />
      <Row>
        <CourseHoleDetails currentHole={currentHole} greenDepth={currentMap.green_depth}/>
      </Row>
      <hr className='text-danger' />
      <Row>
        {displayMap === 'Hole' ?  <HoleMap mapData={currentMap} /> : <CourseMap gps={gps} />}
      </Row>
      <Row className='m-1'>
        <Button variant='danger' className='fw-bold' onClick={e => handleMapClick(displayMap)}>
          {displayMap === 'Hole' ? 'View Course Map' : `View Hole #${currentHole.number}`}
        </Button>
      </Row>
    </Container>
  )
}

export default CourseHolesTab