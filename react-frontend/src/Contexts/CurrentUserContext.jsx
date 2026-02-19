import { createContext, useEffect, useState } from 'react';

export const CurrentUser = createContext()

const CurrentUserProvider = ({ children }) => {
  const BASE_URL = import.meta.env.VITE_BACKEND_URL
  const USER = import.meta.env.VITE_USERNAME

  const [currentUser, setCurrentUser] = useState([])

  useEffect(() =>{
    const getuser = async () => {
      // app designed for local single user use, hardcoded id
      let response = await fetch(BASE_URL + 'person/' + USER)
      let user = await response.json()
      setCurrentUser(user)
    }

    if (!currentUser.length) getuser()
  },[currentUser])

  return (
    <CurrentUser.Provider value={{ currentUser, setCurrentUser }}>
        {children}
    </CurrentUser.Provider>
  )
}

export default CurrentUserProvider