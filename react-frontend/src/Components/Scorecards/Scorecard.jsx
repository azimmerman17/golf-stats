import { useState } from 'react'
import Table from 'react-bootstrap/Table'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import  { ScorecardHeader, ScorecardHeaderBody, ScorecardScoringBody } from './Utilities/ScorecardHeaders'
import ScoreCardData from './ScorecardData'
import ScorecardHeaders from './ScorecardHeaders'

const Scorecard = ({ holes, gender, scores, hole_count }) => {
  if (gender === 'Male') holes = holes.M
  else holes = holes.F

  // hard code units
  let units = 'yards'
  
  let yardsIn = 0
  let metersIn = 0
  let parIn = 0
  
  let yardsOut = 0
  let metersOut = 0
  let parOut = 0

  holes.forEach(h => {
    const { meters, number, par, yards } = h
    if (number < 9) {
      yardsOut += yards
      metersOut += meters
      parOut += par
    } else {
      yardsIn += yards
      metersIn += meters
      parIn += par
    }
  })

  if (holes.length === hole_count) {
    holes.push(
      {number: 'Out', meters: metersOut, par: parOut, si: null, yards: yardsOut},
      { number: 'In', meters: metersIn, par: parIn, si: null, yards: yardsIn},
      { number: 'Total', meters: metersOut + metersIn, par: parOut + parIn, si: null, yards: yardsOut + yardsIn}
    )
  } 

  return (
    <Table bordered size='sm'>
      <thead>
        <ScorecardHeaders side={window.innerWidth < 768 ? 'out' : 'total'} holes={holes} units={units} headerArr={ScorecardHeader} />
      </thead>
      <tbody>
        <ScorecardHeaders side={window.innerWidth < 768 ? 'out' : 'total'} holes={holes} units={units} body={true} headerArr={ScorecardHeaderBody} />

      {scores ? (
        <tr>
          <td>Scores</td>
        </tr>
      ) : null}
      </tbody>
      {window.innerWidth < 768 ? (
        <>
          <thead>
            <tr><th colSpan={12}></th></tr>
            <ScorecardHeaders side='in' holes={holes} units={units} headerArr={ScorecardHeader} />
          </thead>
          <tbody>
            <ScorecardHeaders side='in' holes={holes} units={units} body={true} headerArr={ScorecardHeaderBody} />
            {scores ? (
              <tr>
                <td>Scores</td>
              </tr>
            ) : null}
          </tbody>
        </>
      ) : null}
    </Table>
  )
}

export default Scorecard