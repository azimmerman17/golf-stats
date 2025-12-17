import FormGroupNumber from './FormGroupNumber'
import FormGroupSelect from './FormGroupSelect'
import FormGroupText from './FormGroupText'
import FormGroupTypeahead from './FormGroupTypeahead'

const FormGroupTriage = ({ formData, formObj, setFormObj, disabled, hide, control }) => {
  const { type } = formData

  if (hide) return null

  switch (type) {
    case 'text': 
      return <FormGroupText formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} />
    case 'number':
      return <FormGroupNumber formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} />
    case 'select':
      return <FormGroupSelect formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} />
    case 'typeahead':
      return <FormGroupTypeahead formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} />
      default:
      return <p>{type}</p>
  }
}


export default FormGroupTriage