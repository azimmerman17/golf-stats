import { IoGolfSharp, IoLogInOutline, IoLogOutOutline, IoPerson, IoGolf } from 'react-icons/io5';
import { FaHouseChimney, FaPlus } from 'react-icons/fa6';
import { GiGolfTee } from "react-icons/gi";


const GetIcon = (iconName) => {
  switch (iconName) {
    case 'Courses':
      return <IoGolfSharp />
    case 'Course Plus':
      return <><FaPlus /><IoGolfSharp /></>
    case 'Home':
      return <FaHouseChimney />
    case 'Login':
      return <IoLogInOutline />
    case 'Logout':
      return <IoLogOutOutline />
    case 'Profile':
      return <IoPerson />  
    case 'Tee':
      return <GiGolfTee />
    default:
      return null
  }
} 

export default GetIcon