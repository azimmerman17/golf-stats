import Image from 'react-bootstrap/Image'

const GetFlag = (nation, width) => {
  const flag_url = 'https://flagcdn.com'

  return (
    <Image 
      src={`${flag_url}/w${width}/${nation.toLowerCase()}.png`}
      width={width}
      alt={nation}
      className='shadow-sm'
    />
  )

}

export default GetFlag