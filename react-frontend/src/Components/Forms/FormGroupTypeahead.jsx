import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Form from 'react-bootstrap/Form'
import { Typeahead } from 'react-bootstrap-typeahead'

const FormGroupTypeahead = ({ formData, formObj, setFormObj, disabled, hide, control }) => {
  const { name, placeholder, required, type, field, formText, list } = formData

  const filterFields = ['code', 'value']

  const handleChange = (e) => {
    console.log(e)
  }

  return (
    <Form.Group  
      className='mb-3 form-group' 
      as={Col}  
      controlId={`${control}-name`} 
      // onChange={e => setFormObj({...formObj, [field]:e.target.value })}
      disabled={disabled}
    >
      <Form.Label>{name}{required ? <sup className='text-danger'>*</sup> : null}</Form.Label>
       <Typeahead
        filterBy={filterFields}
        id={`${control}-name`} 
        labelKey='value'
        options={list}
        placeholder={placeholder}
        onChange={e =>  setFormObj({...formObj, [field]:e[0].code})}
        flip
        minLength={2}
        renderMenuItemChildren={list => (
          <Container fluid>
            <Row>
              <h6>{list.value}</h6>
            </Row>
            <Row>
              <small>code: {list.code.toUpperCase()}</small>
            </Row>
          </Container>
        )}
      />
     </Form.Group>
  )
}

export default FormGroupTypeahead
