// Distances are centered around Male Golfers, Female Golfers deduct 80%
const HoleCatagories  = [
  {par: 3, minLength: 0, maxLength: 125, description: 'Short Par 3'},
  {par: 3, minLength: 126, maxLength: 175, description: 'Meduim Par 3'},
  {par: 3, minLength: 176, maxLength: 999, description: 'Long Par 3'},
  {par: 4, minLength: 0, maxLength: 300, description: 'Reachable Par 4'},
  {par: 4, minLength: 301, maxLength: 350, description: 'Short Par 4'},
  {par: 4, minLength: 351, maxLength: 425, description: 'Meduim Par 4'},
  {par: 4, minLength: 425, maxLength: 999, description: 'Long  Par 4'},
  {par: 5, minLength: 0, maxLength: 450, description: 'Reachable Par 5'},
  {par: 5, minLength: 476, maxLength: 500, description: 'Short Par 5'},
  {par: 5, minLength: 501, maxLength: 575, description: 'Meduim Par 5'},
  {par: 5, minLength: 576, maxLength: 999, description: 'Long Par 5'},
]

export default HoleCatagories