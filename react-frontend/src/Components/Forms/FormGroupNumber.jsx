import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'

const FormGroupNumber = ({ formData, formObj, setFormObj, disabled, control }) => {
  const { name, placeholder, required, type, field, formText, min, max } = formData

  return (
    <Form.Group  
      className='mb-3 form-group' 
      as={Col}  
      controlId={`${control}-name`} 
      onChange={e => setFormObj({...formObj, [field]:e.target.value })}
      disabled={disabled}
      min={min}
      max={max}
    >
      <Form.Label>{name}{required ? <sup className='text-danger'>*</sup> : null}</Form.Label>
        <Form.Control type={type} placeholder={placeholder} />
        {formText ? (
          <Form.Text className='text-muted'>
            {formText}
          </Form.Text>
        ) : null}
      </Form.Group>
  )
}

export default FormGroupNumber