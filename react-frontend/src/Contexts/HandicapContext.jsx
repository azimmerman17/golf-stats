import { createContext, useEffect, useState } from 'react';

export const HandicapContext = createContext()

const HandicapContextProvider = ({ children }) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const USER = import.meta.env.VITE_USERID

  const [handicapContext, setHandicapContext] = useState({})

  useEffect(() =>{
    const getHandicap = async () => {
      // app designed for local single user use, hardcoded id
      let historyRes = await fetch(BASE_URL + 'handicap/' + USER)
      let history = await historyRes.json()

      let currentRes = await fetch(BASE_URL + 'handicap/' + USER + '/current')
      let current = await currentRes.json()
      setHandicapContext({history, current})
    }

    if (!handicapContext.current) getHandicap()
  },[handicapContext])

  return (
    <HandicapContext.Provider value={{ handicapContext, setHandicapContext }}>
        {children}
    </HandicapContext.Provider>
  )
}

export default HandicapContextProvider