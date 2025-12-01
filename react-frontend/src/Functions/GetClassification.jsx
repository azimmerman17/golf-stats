const GetClassification = (code) => {
  switch (code) {
    case 'D':
      return 'Daily-Fee'
    case 'P':
      return 'Private'
    case 'R':
      return 'Resort'
    case 'M':
      return 'Municipal'
    case 'S':
      return 'Semi-Private'
    case 'O':
      return 'Other'
    default:
      return 'Unknown'
  }
}

export default GetClassification
