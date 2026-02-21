const GetWeekDay = (dayNum, style) => {
    switch (dayNum) {
    case 0: 
      if (style === 'long') return 'Sunday'
      if (style === 'short') return 'Sun'
      if (style === 'single') return 'Su'
      if (style === 'number') return 7
      break
    case 1: 
      if (style === 'long') return 'Monday'
      if (style === 'short') return 'Mon'
      if (style === 'single') return 'S'
      if (style === 'number') return dayNum
      break
    case 2: 
      if (style === 'long') return 'Tuesday'
      if (style === 'short') return 'Tue'
      if (style === 'single') return 'T'
      if (style === 'number') return dayNum

      break
    case 3: 
      if (style === 'long') return 'Wednesday'
      if (style === 'short') return 'Wed'
      if (style === 'single') return 'W'
      if (style === 'number') return dayNum

      break
    case 4:
      if (style === 'long') return 'Thursday'
      if (style === 'short') return 'Thr'
      if (style === 'single') return 'R'
      if (style === 'number') return dayNum
      break
    case 5: 
      if (style === 'long') return 'Friday'
      if (style === 'short') return 'Fri'
      if (style === 'single') return 'F'
      if (style === 'number') return dayNum
      break
    case 6: 
      if (style === 'long') return 'Saturday'
      if (style === 'short') return 'Sat'
      if (style === 'single') return 'Sa'
      if (style === 'number') return dayNum
      break
  }
  return 'Error'
}

export default GetWeekDay