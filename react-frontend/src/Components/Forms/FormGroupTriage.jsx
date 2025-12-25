import FormGroupNumber from './FormGroupNumber'
import FormGroupSelect from './FormGroupSelect'
import FormGroupText from './FormGroupText'
import FormGroupTypeahead from './FormGroupTypeahead'

const FormGroupTriage = ({ formData, formObj, setFormObj, disabled, hide, control, validated }) => {
  const { type } = formData

  if (hide) return null

  switch (type) {
    case 'text': 
      return <FormGroupText formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} />
    case 'number':
      return <FormGroupNumber formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} />
    case 'select':
      return <FormGroupSelect formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} />
    case 'typeahead':
      return <FormGroupTypeahead formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} />
      default:
      return <p>{type}</p>
  }
}


export default FormGroupTriage