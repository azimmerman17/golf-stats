import { IoGolfSharp, IoLogInOutline, IoLogOutOutline } from 'react-icons/io5';

const GetIcon = (iconName) => {
  switch (iconName) {
    case 'Course':
      return <IoGolfSharp />
    case 'Logout':
      return <IoLogOutOutline />
    case 'Login':
      return <IoLogInOutline />
  
    default:
      return null
  }
} 

export default GetIcon