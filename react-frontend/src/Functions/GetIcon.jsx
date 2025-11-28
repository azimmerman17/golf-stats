import { IoGolfSharp, IoLogInOutline, IoLogOutOutline, IoPerson, IoGolf } from 'react-icons/io5';
import { FaHouseChimney } from 'react-icons/fa6';

const GetIcon = (iconName) => {

  console.log(iconName)
  switch (iconName) {
    case 'Courses':
      return <IoGolfSharp />
    case 'Home':
      return <FaHouseChimney />
    case 'Login':
      return <IoLogInOutline />
    case 'Logout':
      return <IoLogOutOutline />
    case 'Profile':
      return <IoPerson />
    default:
      return null
  }
} 

export default GetIcon