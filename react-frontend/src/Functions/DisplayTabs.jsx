import Nav from 'react-bootstrap/Nav';

const DisplayTabs = ({ tabs, currentTab, page, setCurrentTab, defaultKey}) => {

  const tabLinks = tabs.map(tab => {
    return (
      <Nav.Item key={`${page}-navtab-${tab}`}>
        <Nav.Link className={`bg-danger${currentTab === tab ? ' text-white border-black border-2 fw-bold' :'-subtle text-black border-bottom'} rounded-top`}  onClick={e => setCurrentTab(tab)}>
          {tab}
        </Nav.Link>
      </Nav.Item>
    )
  })

  return (
    <Nav justify variant='tabs' className='border-bottom border-black border-3 p-1' defaultActiveKey={defaultKey}>
      {tabLinks}
    </Nav>
  )
}

export default DisplayTabs