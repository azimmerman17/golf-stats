import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import HomeCards from '../../Assests/HomeCards'
import Breadcrumbs from './BreadCrumbs'
import DisplayCards from './DisplayCards'

const HomePage = ({}) => {

  const breadcrumbList = [
    {name: 'Home', change: '', active: false}
  ]

  const navCards = HomeCards.map(card => {
    const { title, icon, page, path, space } = card

    return (
      <Col className='mx-auto p-1' key={`HPcard-${title}`}>
        <DisplayCards title={title} icon={icon} page={page} path={path} space={space}/>
      </Col>
    )
  })
  return (
    <Container fluid>
      <Breadcrumbs list={breadcrumbList}></Breadcrumbs>
      <Row className='my-1 mx-auto'>
        Profile
      </Row>
      <Row className='my-1 mx-auto'>
        <Col className='p-2'>
          Home Course
        </Col>
        <Col className='p-2'> 
          Handicap Card
        </Col>
      </Row>
      <Row className='my-1 mx-auto'>
        {navCards}   
      </Row>
    </Container>
  )
}

export default HomePage