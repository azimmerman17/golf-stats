const GetMonthName = (monthNum, style) => {
  switch (monthNum) {
    case 0: 
      if (style === 'long') return 'January'
      if (style === 'short') return 'Jan'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 1: 
      if (style === 'long') return 'Febuary'
      if (style === 'short') return 'Feb'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 2: 
      if (style === 'long') return 'March'
      if (style === 'short') return 'Mar'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 3: 
      if (style === 'long') return 'April'
      if (style === 'short') return 'Apr'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 4:
      if (style === 'long') return 'May'
      if (style === 'short') return 'May'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 5: 
      if (style === 'long') return 'June'
      if (style === 'short') return 'Jun'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 6: 
      if (style === 'long') return 'July'
      if (style === 'short') return 'Jul'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 7: 
      if (style === 'long') return 'August'
      if (style === 'short') return 'Aug'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 8:
      if (style === 'long') return 'September'
      if (style === 'short') return 'Sep'
      if (style === 'number') return `0${monthNum + 1}`
      break
    case 9: 
      if (style === 'long') return 'October'
      if (style === 'short') return 'Oct'
      if (style === 'number') return monthNum + 1
      break
    case 10: 
      if (style === 'long') return 'November'
      if (style === 'short') return 'Nov'
      if (style === 'number') return monthNum + 1
      break
    case 11:
      if (style === 'long')  return 'December'
      if (style === 'short') return 'Dec'
      if (style === 'number') return monthNum + 1
      break
  }
  return 'ERROR'
}

export default GetMonthName