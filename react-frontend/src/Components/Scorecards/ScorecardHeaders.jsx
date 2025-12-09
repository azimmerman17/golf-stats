import ScorecardData from './ScorecardData'
import  { ScorecardHeader, ScorecardHeaderBody, ScorecardScoringBody } from './Utilities/ScorecardHeaders'


const ScorecardHeaders = ({ side, holes, units, body, headerArr }) => {
  const headings = headerArr.map(header => {

    if (units === 'yards' && header === 'Meters') return null
    if (units === 'meters' && header === 'Yards') return null

    const holeData = holes.map(hole => {
      const { number, tee_id, gender } = hole
      
      if (window.innerWidth < 768 ) {
        if (number > 9 && side === 'out') return null
        if ((number === 'In' || number === 'Total') && side === 'out') return null
        if (number < 10 && side === 'in') return null
        if (number === 'Out' && side === 'in') return null
      }

      if (body) {
        return (
          <td key={`scorecard-table-body-${header}-${side}-${tee_id}-${gender}-${number}-data`} className={number === 'Out' || number === 'In' || number === 'Total' ? 'fw-bold' : null} colSpan={side === 'out' && number === 'Out' ? 2 : 1}>
            <ScorecardData hole={hole} label={header} />
          </td>
        )
      }

      return (
        <th key={`scorecard-table-header-${header}-${side}-${tee_id}-${gender}-${number}-data`} colSpan={side === 'out' && number === 'Out' ? 2 : 1}>
          <ScorecardData hole={hole} label={header} />
        </th>
      )
    })

    return (
      <tr key={`scorecard-table-header-${header}-${side}`} className='text-center scorecard-text'>
        <th>{header}</th>
        {holeData}
      </tr>
    )
  })

  return headings
}

export default ScorecardHeaders