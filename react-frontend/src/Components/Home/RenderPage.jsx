import { useContext } from 'react' 
import { useSearchParams } from 'react-router-dom';

import { CurrentPage } from '../../Contexts/CurrentPageContext'

import HomePage from './HomePage'
import CourseHome from '../Course/CourseHome'
import FacilityHome from '../Course/Facility/FacilityHome'
import CoursePage from '../Course/Course/CoursePage';
import NewFacility from '../Course/NewFacility';
import FacilityEdit from '../Course/Facility/FacilityEdit';
import NewCourse from '../Course/Course/NewCourse';


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
          return <CoursePage />
        case 'new facility':
          return <NewFacility />
        case 'editFacility':
          return <FacilityEdit />
        case 'newCourse':
          return <NewCourse />
        default:
          if (searchParams.get('facility_id') && searchParams.get('course_id')) return <CoursePage />
          else if (searchParams.get('facility_id')) return <FacilityHome />
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