import { useContext, useState } from 'react'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import { CurrentUser } from '../../Contexts/CurrentUserContext'

import Breadcrumbs from '../Home/BreadCrumbs'
import PersonHeader from './PersonHeader'
import DisplayTabs from '../../Functions/DisplayTabs'
import PersonBio from './PersonBio'

const PersonHome = ({}) => {
  const {currentUser, setCurrentUser} = useContext(CurrentUser)
  const [currentTab, setCurrentTab] = useState('Bio')

  if (!currentUser.length) return 'Loading...'

  const breadcrumbList = [
    {name: 'Home', path: '/', active: true},
    {name: 'Profile', path: '/profile', active: false},
  ]

  // filter on the username in the env
  console.log(currentUser)
  const person = currentUser.filter(p => p.username === import.meta.env.VITE_USERNAME)[0]

  console.log(person)

  const tabs = [
    'Bio',
    'User Settings',
    'Handicap',
    'Equipment'
  ]
    const tabs2 = [
    'Rounds',
    'Stats',
    'Combines',
    'Events'
  ]

  const tabView = (tab) => {
    switch (tab) {
      case 'Bio':
        return <PersonBio person={person} />
      case 'User Settings':
        return 'User Settings'
      case 'Handicap':
        return 'Handicap'
      case 'Equipment':
        return 'Equipment'
      case 'Rounds':
        return 'Rounds'
      case 'Stats':
        return 'Stats'
      case 'Combines':
        return 'Combines'
      case 'Events':
        return 'Events'
    }
  }


  return (
    <Container fluid>
      <Row>
        <Breadcrumbs list={breadcrumbList} />
      </Row>
      <Row>
        <PersonHeader person={person} />
      </Row>
      <Row className='border border-danger border-3 rounded shadow-lg mb-2'>
        <DisplayTabs tabs={tabs} currentTab={currentTab} page='facility' setCurrentTab={setCurrentTab} defaultKey={'Bio'} />
        <DisplayTabs tabs={tabs2} currentTab={currentTab} page='facility' setCurrentTab={setCurrentTab} defaultKey={'Bio'} />
        {tabView(currentTab)}
      </Row>
    </Container>
  )
}

export default PersonHome