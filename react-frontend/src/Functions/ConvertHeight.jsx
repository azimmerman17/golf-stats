const ConvertHeight = (value, inUnit, outUnit) => {
  if (inUnit === outUnit) return value
  else if (inUnit === 'IN') {
    // IN to FT'IN'
    if (outUnit === 'FT') {
      let feet = Math.floor(value / 12)
      let inch = value % 12
      return `${feet}' ${inch}"`
    }
    // IN to CM
    if (outUnit === 'CM') return (value * 2.54).toFixed(0)
  } else if (inUnit === 'CM') {
    if (outUnit === 'FT') {
      // CM to FT'IN'
      let feet = Math.floor(value / 30.48)
      let inch = Math.round(value % 30.48 / 2.54)
      return `${feet}' ${inch}"`
    } if (outUnit === 'IN') return (value / 2.54).toFixed(0)
  } else if (inUnit === 'FT') {
    value = value.split(`'`)
    let feet = Number(value[0])
    let inch = Number(value[1].split(`"`)[0].trim())
    if (outUnit === 'IN') return feet * 12 + inch
    if (outUnit === 'CM') return ((feet * 12 + inch) * 2.54).toFixed(0)
  }
  return 'ERROR'
}

export default ConvertHeight