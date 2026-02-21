import GetMonthName from "./GetMonthName";
import GetWeekDay from "./GetWeekDay";

const FormatDate = (timestamp, utc, monthLength, weekDay, delimiter) => {
  let dt = new Date(timestamp)

  let day = utc ? dt.getUTCDay() : dt.getDay()
  let month = utc ? dt.getUTCMonth() : dt.getMonth()
  let date = utc ? dt.getUTCDate() : dt.getDate()
  let year = utc ? dt.getUTCFullYear(): dt.getFullYear()

  if  (delimiter) return `${GetMonthName(month, 'number')}${delimiter}${date < 10 ? `0${date}` : date}${delimiter}${year}`
  return `${weekDay ? `${GetWeekDay(day, weekDay)} ` : ''}${GetMonthName(month, monthLength)} ${date < 10 ? `0${date}` : date}, ${year}`
}

export default FormatDate