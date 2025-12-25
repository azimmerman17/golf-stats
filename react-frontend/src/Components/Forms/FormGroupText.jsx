import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'

const FormGroupText = ({ formData, formObj, setFormObj, disabled, control, validated }) => {
  const { name, placeholder, required, type, field, formText, validationText } = formData

  return (
    <Form.Group  
      className='mb-3 form-group' 
      as={Col}  
      controlId={`${control}-name`} 
      onChange={e => setFormObj({...formObj, [field]:e.target.value })}
      disabled={disabled}
      required={required}
    >
      <Form.Label>{name}{required ? <sup className='text-danger'>*</sup> : null}</Form.Label>
        <Form.Control type={type} placeholder={placeholder} />
        {formText ? (
          <Form.Text className='text-muted'>
            {formText}
          </Form.Text>
        ) : null}
          <Form.Control.Feedback type='invalid'>
            {validationText}
          </Form.Control.Feedback>
      </Form.Group>
  )
}

export default FormGroupText
