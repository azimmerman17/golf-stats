import { createContext, useEffect, useState } from 'react';

export const EquipmentContext = createContext()

const EquipmentContextProvider = ({ children }) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const USER = import.meta.env.VITE_USERID

  const [equipmentContext, setEquipmentContext] = useState([])

  useEffect(() =>{
    const getEquipment = async () => {
      // app designed for local single user use, hardcoded id
      let response = await fetch(BASE_URL + 'equipment/user/' + USER)
      let equipment = await response.json()
      setEquipmentContext(equipment)
    }

    if (!equipmentContext.length) getEquipment()
  },[equipmentContext])

  return (
    <EquipmentContext.Provider value={{ equipmentContext, setEquipmentContext }}>
        {children}
    </EquipmentContext.Provider>
  )
}

export default EquipmentContextProvider