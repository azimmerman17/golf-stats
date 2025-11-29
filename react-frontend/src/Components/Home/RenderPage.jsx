import { useContext } from 'react' 

import { CurrentPage } from '../../Contexts/CurrentPageContext'

import HomePage from './HomePage'
import CourseHome from '../Course/CourseHome'


const RenderPage = ({ path, setTitle }) => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)

  setTitle(`Golf Statitics App - ${path.split(' ').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')}`)


  switch(path) {  
    case 'about':
      return path
    // Course Group
    case 'course':
      switch (currentPage) {
        default:
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