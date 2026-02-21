const ConvertWeight = (value, inUnit, outUnit) => {
  if (inUnit === outUnit) return value
  else if (inUnit === 'LB') {
    if (outUnit === 'KG') return (value / 2.205).toFixed(1)
    if (outUnit === 'ST') return (value / 14).toFixed(1)
  } else if (inUnit === 'KG') {
    if (outUnit === 'LB') return (value * 2.205).toFixed(1)
    if (outUnit === 'ST') return (value / 6.35).toFixed(1) 
  } else if (inUnit === 'ST') {
    if (outUnit === 'LB') return (value * 14).toFixed(1)
    if (outUnit === 'KG') return (value * 6.35).toFixed(1) 
  }
  return value
}

export default ConvertWeight