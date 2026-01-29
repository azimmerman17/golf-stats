// Formula - Index x (Slope / 113) + ( Rating – Par) 

const CalculateCourseHandicap = (index, rating, slope, par) => {
  //  reassign Plus (+) Handicaps to a negative number
  if (index[0] === '+') index = -index

  return Math.round(index * (slope / 113) + (rating - par),0)
}

export default CalculateCourseHandicap