import { useContext } from 'react' 
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

import GetIcon from '../../Functions/GetIcon';

// import { CurrentPage } from '../Contexts/CurrentPageContext'

const DisplayCards = ({ title, icon, page, path, space }) => {
  // const { currentPage, setCurrentPage } = useContext(CurrentPage)

  const handleClick = (page, path) => {
    if (page) setCurrentPage(page)
    else location.replace(path)
  }

  return (
    <Button variant='danger' className='p-1 my-1 text-center shadow-lg nav-card w-100 h-100'  onClick={e => handleClick(page, path)}>
      <Card className='m-0 p-0 w-100 h-100'>
        <Card.Body className='m-0 p-1'>
          <Card.Title className='mt-1 pt-1 mb-0 pb-0'>{title}</Card.Title>
          {space ? <br ></br> : null}
          <Card.Text className='mb-1 pb-2 pt-0 mt-0 fs-2 align-text-bottom'>
            {GetIcon(icon)}
          </Card.Text>
        </Card.Body>
      </Card>
    </Button>
  )
}

export default DisplayCards