// import { StandardHeaders } from './Utilities/ScorecardHeaders'
// import { OutHeaders, InHeaders, FullHeaders } from './Utilities/ScorecardSideHeaders'


const ScorecardData = ({ label, hole }) => {
  const { meters, number, par, si, yards } = hole
  
  switch (label) {
    case 'Hole':
      return number
    case 'Yards':
      return yards
    case 'Meters':
      return meters
    case 'Par':
      return par
    case 'SI':
      return si
  }
}

export default ScorecardData