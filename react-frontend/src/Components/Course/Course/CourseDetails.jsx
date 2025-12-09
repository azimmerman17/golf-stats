import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import BarChart from '../../Charts/BarChart'

const CourseDetails = ({ holes, gender }) => {
  if (gender === 'Male') holes = holes.M
  else holes = holes.F

  // UNITS hardcode
  let units = 'yards'

  const holesDisplay = (value, min) => {
    const filteredHoles = holes.filter(h => h.par === value)

    const data = []
    let dMin = min
    let dMax = min

    filteredHoles.forEach(h => {
      const { hole_id, meters, number, yards } = h 
      let distance
      if (units === 'yards') distance = yards
      else distance = meters

      if (distance > dMax) dMax = distance
      if (distance < dMin) dMin = distance
        
      data.push ({label: `Hole #${number}`, value: distance})
     })

    return (
      <BarChart chartData={data} borderWidth={2} dataLabel={`Par ${value}`} axis='y' min={Math.max((Math.floor(dMin / 50) - 1) * 50, 0)} max={(Math.floor(dMax / 50)+ 1) * 50} step={25}  />
    )


  }

  return (
    <Container fluid className='mb-5'>
      <Row>
        <h6>Par 3</h6>
        {holesDisplay(3, 0)}

      </Row>
      <Row>
        <h6>Par 4</h6>
        {holesDisplay(4, 250)}
      </Row>
      <Row>
        <h6>Par 5</h6>
        {holesDisplay(5, 350)}
      </Row>
    </Container>
  )
}

export default CourseDetails