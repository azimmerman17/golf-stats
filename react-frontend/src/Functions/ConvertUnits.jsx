const ConvertUnits = (data, inUnit, outUnit) => {
  // IN -YARDS
  if (inUnit == 'yards') {
    // OUT
    switch (outUnit) {
      case 'feet':
        return Math.round(data * 3)
      case 'meters':
        return Math.round(data * 0.9144)
      default:
        return data
    }
  }
  // IN - METERS
  else if (inUnit == 'meters') {
    // OUT
    switch (outUnit) {
      case 'yards':
        return Math.round(data / 0.9144)
      case 'feet':
        return Math.round(data * 3 / 0.9144)
      default:
        return data
    }
  }
  // IN - FEET
  else if (inUnit == 'feet') {
    // OUT
    switch (outUnit) {
      case 'yards':
        return Math.round(data / 3)
      case 'meters':
        return Math.round(data / 3 * 0.9144)
      default:
        return data
    }
  }
}

export default ConvertUnits