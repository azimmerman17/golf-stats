const TranslateUnitName = (value, unit) => {
  switch (unit) {
    case 'Altitue Units':
      if (value === 'FT') return	'Feet'
      if (value === 'M') return	'Meters'
    case 'Distance Units':
      if (value === 'Y') return	'Yards'
      if (value === 'M') return	'Meters'
    case 'Speed Units':
      if (value === 'MPH') return	'Miles/Hour'
      if (value === 'KPH') return	'Kilometers/Hour'
      if (value === 'MPS') return	'Meters/Second'
    case 'Temperature Units':
      if (value === 'F') return	'Fahrenheit'
      if (value === 'C') return	'Celsius'
    case 'Weight Units':
      if (value === 'LB') return	'Pounds'
      if (value === 'KG') return	'Kilograms'
      if (value === 'ST') return	'Stones'
    case 'Height Units':
      if (value === 'FT') return	'Feet/Inches'
      if (value === 'CM') return	'Centimeters'
  }
}

export default TranslateUnitName

