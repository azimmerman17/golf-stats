import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'

const FormGroupSelect = ({ formData, formObj, setFormObj, disabled, hide, control }) => {
  const { name, placeholder, required, type, field, formText, list } = formData
  
  const selectOptions = list.map(item => {
    const { value, code } = item 

    return <option value={code} key={`${control}-${value}`}>{value}</option>
  })

  return (
    <Form.Group  
      className='mb-3 form-group' 
      as={Col}  
      controlId={`${control}-name`} 
      onChange={e => setFormObj({...formObj, [field]:e.target.value })}
      disabled={disabled}
    >
      <Form.Label>{name}{required ? <sup className='text-danger'>*</sup> : null}</Form.Label>
        <Form.Select aria-label={`Select ${name}`}>
              {selectOptions}
        </Form.Select>
        {formText ? (
          <Form.Text className='text-muted'>
            {formText}
          </Form.Text>
        ) : null}
    </Form.Group>
  )
}

export default FormGroupSelect