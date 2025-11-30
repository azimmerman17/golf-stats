// context for the current navigated facility
import { createContext, useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';

export const CurrentFacility = createContext()

const CurrentFacilityProvider = ({ children }) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const [searchParams, setSearchParams] = useSearchParams();
  const [currentFacility, setCurrentFacility] = useState(null)

  useEffect(() => {
    const getCourseFacility = async (id) => {
      let response = await fetch(BASE_URL + '/facility/' + id)
      let facility = await response.json()

      setCurrentFacility(facility)
    }

    if (searchParams.get('facility_id') !== null && currentFacility === null) getCourseFacility(searchParams.get('facility_id'))
    else if (currentFacility !== null && searchParams.get('facility_id') !== currentFacility.facility.facility_id)  getCourseFacility(searchParams.get('facility_id'))
  }, [searchParams])

  return (
    <CurrentFacility.Provider value={{ currentFacility, setCurrentFacility }}>
        {children}
    </CurrentFacility.Provider>
  )
}

export default CurrentFacilityProvider