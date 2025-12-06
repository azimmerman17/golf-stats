import { useEffect, useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/esm/Col'

import Dropdowns from '../../Home/Dropdowns'
import CourseHoleDetails from './CourseHoleDetails'
import HoleMap from '../../Map/HoleMap'

const CourseHolesTab = ({ tees, gps, currentTee, setCurrentTee }) => {
  const [currentHole, setCurrentHole] = useState({
                                                  male: currentTee.holes.M.filter(g => g.number === 1)[0], 
                                                  female: currentTee.holes.F.filter(g => g.number === 1)[0], 
                                                  teeName: currentTee.name
                                                })
  const [currentMap, setCurrentMap] = useState(gps.filter(g => g.number == 1)[0])       

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

  // console.log(currentHole, currentTee)
  
  // Build Dropdowns
  let teeDropdown = []
  tees.forEach(t => {teeDropdown.push({name: t.name, selected: t})})
  let holeDropdown = []
  gps.forEach(h => {holeDropdown.push({name: `Hole ${h.number}`, selected: {male: currentTee.holes.M.filter(g => g.number === h.number)[0], female: currentTee.holes.F.filter(g => g.number === h.number)[0]}})})

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
        <HoleMap mapData={currentMap} />
      </Row>
    </Container>
  )
}

export default CourseHolesTab