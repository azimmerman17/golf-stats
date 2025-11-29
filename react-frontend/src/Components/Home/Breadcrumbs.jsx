import { useContext } from 'react';
import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { CurrentPage } from '../../Contexts/CurrentPageContext'

const Breadcrumbs = ({ list }) => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)

  const listItems = list.map((item, i) => {
    const  { name, path, page, active } = item

    const handleClick = (page, path) => {
      if (page) setCurrentPage(page)
      else location.replace(path)
    }

    return (
      <Breadcrumb.Item 
        onClick={e => handleClick(path, page)}
        active={!active}
        key={`breadcrumb-${name}`}
        className='breadcrumb-sm'
      >
        {name}
      </Breadcrumb.Item>
    )
  })

  return (
    <Breadcrumb>
      {listItems}
    </Breadcrumb>
  );
}

export default Breadcrumbs