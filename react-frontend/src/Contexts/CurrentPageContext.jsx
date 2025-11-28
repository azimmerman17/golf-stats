// context for the current navigated page
import { createContext, useState } from 'react';

export const CurrentPage = createContext()

const CurrentPageProvider = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('')

  return (
    <CurrentPage.Provider value={{ currentPage, setCurrentPage }}>
        {children}
    </CurrentPage.Provider>
  )
}

export default CurrentPageProvider