import { useContext } from 'react' 
import { useSearchParams } from 'react-router-dom';

import { CurrentPage } from '../../Contexts/CurrentPageContext'

import HomePage from './HomePage'
import CourseHome from '../Course/CourseHome'
import FacilityHome from '../Course/Facility/FacilityHome'


const RenderPage = ({ path, setTitle }) => {
  const [searchParams, setSearchParams] = useSearchParams();
  const { currentPage, setCurrentPage } = useContext(CurrentPage)

  setTitle(`Golf Statitics App - ${path.split(' ').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')}`)


  switch(path) {  
    case 'about':
      return path
    // Course Group
    case 'course':
      switch (currentPage) {
        case 'facility':
          return  <FacilityHome />
        case 'course':
          return 'course'
        default:
          if (searchParams.get('facility_id')) return  <FacilityHome />
          else if (searchParams.get('facility_id') && searchParams.get('course_id')) return  'course'
          return <CourseHome />
      }



    // Profile Group
    case 'profile':
       switch (currentPage) {
        default:
          return path
      }

    
    default:
      return <HomePage />
  }
}

export default RenderPage