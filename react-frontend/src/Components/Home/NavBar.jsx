import { useContext, useState } from 'react' 
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Offcanvas from 'react-bootstrap/Offcanvas';

import NavItems from '../../Assests/NavItems';
import GetIcon from '../../Functions/GetIcon';

// import { CurrentUser } from '../Contexts/CurrentUserContext'
// import { CurrentPage } from '../Contexts/CurrentPageContext';

// import Login from './Login';

const NavBar = () => {
  // const { currentUser, setCurrentUser } = useContext(CurrentUser) 
  // const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const [expanded, setExpanded] = useState(false)
  let currentUser = null

  const navHeaders = NavItems.map(header => {
    const { name, icon, path, login, role } = header

    // nav item display based on if user is loggedin
    if (currentUser && !login) return null
    else if (!currentUser && login) return null

    // show/hide nav item based on role - future work
     

    const handleClick = (path) => {
      location.replace(path)
    }
    
    return (
      <Nav.Link className='py-1' key={`navbar-${name}`} onClick={e=> handleClick(path)}>
        <h5 className='text-white'>
          {GetIcon(icon)} {name}
        </h5>
      </Nav.Link>
     )
  })

  return (
    <Navbar bg='danger' variant='danger' sticky='top' expand='xxxl' className='m-0' expanded={expanded}>
      <Container className='mx-3 main' fluid>
        <Navbar.Brand className='text-white' href='/'>
          <h3>Golf Statistics Tracker</h3>
        </Navbar.Brand>
        <Navbar.Toggle className='text-white bg-white' aria-controls='basic-navbar-nav' onClick={() => setExpanded(!expanded)}/>
        <Navbar.Offcanvas id='offcanvasNavbar' aria-labelledby='offcanvasNavbar' placement='end'>
          <Offcanvas.Header closeButton className='bg-danger text-white'  onClick={() => setExpanded(!expanded)}>
            <Offcanvas.Title id='offcanvasNavbar' className='fs-4 fw-bolder'>
             Welcome User's Name
            </Offcanvas.Title>
          </Offcanvas.Header>
          <Offcanvas.Body className='bg-danger' as={Container}>
            {navHeaders}
          </Offcanvas.Body>
        </Navbar.Offcanvas>
      </Container>
    </Navbar>
  )
}

export default NavBar