import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css'

import NavBar from './Components/Home/NavBar';
import Footer from './Components/Home/Footer';
import RenderPage from './Components/Home/RenderPage';

import CurrentPageProvider from './Contexts/CurrentPageContext';

function App() {
  const [title, setTitle] = useState('Golf Statitics App')

  useEffect(() => {
    document.title = title
  }, [title])
  
  return (
    <>
      <Router>
      {/* CONTEXT PROVIDERS */}
       <CurrentPageProvider>
        {/* PAGES */}
        <Container fluid>
          <Row className='mb-3'> 
            <NavBar />
          </Row>
          <Row className='p-2 main m-auto mb-5'>
            <Routes>
              <Route exact path='/' element={<RenderPage path='home' setTitle={setTitle}/>} />
              <Route path='/about' element={<RenderPage path='about' setTitle={setTitle}/>} />
              <Route path='/course' element={<RenderPage path='course' setTitle={setTitle}/>} />
              <Route path='/profile' element={<RenderPage path='profile' setTitle={setTitle}/>} />

              {/* New User */}
              {/* Reset Password */}
            </Routes>
          </Row>
          <Row>
            <Footer />
          </Row>
        </Container>
        {/* CONTEXT PROVIDERS CLOSE */}
        </CurrentPageProvider> 
      </Router>
    </>
  )
}

export default App
