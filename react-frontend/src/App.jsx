import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css'

import NavBar from './Components/Home/NavBar';
import Footer from './Components/Home/Footer';

function App() {
  const [title, setTitle] = useState('Golf Statitics App')

  useEffect(() => {
    document.title = title
  }, [title])
  

  return (
    <>
      <Router>
      {/* CONTEXT PROVIDERS */}
        
      {/* PAGES */}
      <Container fluid>
        <Row className='mb-3'> 
          <NavBar />
        </Row>
        <Row className='p-2 main m-auto mb-5'>
          PAGE BODY
          <Routes>
            {/* <Route exact path='/' element={<HomePage />} /> */}
            {/* New User */}
            {/* Reset Password */}
          </Routes>
        </Row>
        <Row>
          <Footer />
        </Row>
      </Container>
      {/* CONTEXT PROVIDERS CLOSE */}
      </Router>
    </>
  )
}

export default App
