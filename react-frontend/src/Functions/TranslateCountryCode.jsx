import CountryList from '../Assests/CountryList'

const TranslateCountryCode = (nation, returnData) => {
  const item = CountryList.filter(i => i.code.toLowerCase() === nation.toLowerCase() || i.map.toLowerCase() === nation.toLowerCase())[0]

  const {country, map, code } = item

  switch (returnData) {
    case 'country':
      return country
    case 'map':
      return map
    case 'code':
      return code

  }




}

export default TranslateCountryCode