const GetPlayerType = (code) => {
  switch (code) {
    case 'A':
      return	'Amatuer'
    case 'P':
      return 'Professional'
    case 'T':
      return 'Tour Professional'
    case 'C':
      return 'College'
    case 'J':
      return 'Junior'
  }
}

export default GetPlayerType