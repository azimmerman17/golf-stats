import { useContext } from 'react';
import Breadcrumb from 'react-bootstrap/Breadcrumb';


const Breadcrumbs = ({ list }) => {
  const listItems = list.map((item, i) => {
    const  { name, change, active } = item

    return (
    <Breadcrumb.Item 
      // onClick={e => setCurrentPage(change)}
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