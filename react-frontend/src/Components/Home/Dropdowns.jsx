import Dropdown from 'react-bootstrap/Dropdown'

const Dropdowns = ({ items, color, id, align, current, setCurrent }) => {

  const dropItems = items.map((item, i) => {
    const { name, selected } = item

    return (
      <Dropdown.Item onClick={e =>  setCurrent(selected)} key={`${id}-${name}-${i}`} className={name === current ? 'fw-bold' : ''}>
        {name}
      </Dropdown.Item>
    )
  })

  return (
    <Dropdown >
      <Dropdown.Toggle variant={color} id={id} align={align} className='border'>
        {current}
      </Dropdown.Toggle>
      <Dropdown.Menu>
       {dropItems}
      </Dropdown.Menu>
    </Dropdown>
  )
}

export default Dropdowns