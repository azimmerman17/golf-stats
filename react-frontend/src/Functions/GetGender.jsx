const GetGender = (code) => {
  switch (code) {
    case 'M':
      return 'Male'
    case 'F':
      return 'Female'
    default:
      return code
  }
}

export default GetGender