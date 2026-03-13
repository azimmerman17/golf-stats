import FormGroupNumber from './FormGroupNumber'
import FormGroupSelect from './FormGroupSelect'
import FormGroupText from './FormGroupText'
import FormGroupTypeahead from './FormGroupTypeahead'

const FormGroupTriage = ({ formData, formObj, setFormObj, disabled, hide, control, validated, labelAfter }) => {
  const { type } = formData

  if (hide) return null

  switch (type) {
    case 'text': 
      return <FormGroupText formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} labelAfter={labelAfter} />
    case 'number':
      return <FormGroupNumber formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} labelAfter={labelAfter} />
    case 'select':
      return <FormGroupSelect formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} labelAfter={labelAfter} />
    case 'typeahead':
      return <FormGroupTypeahead formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} labelAfter={labelAfter} />
    // case 'check':
    //   return <FormGroupCheck formData={formData} formObj={formObj} setFormObj={setFormObj} disabled={disabled} control={control} validated={validated} labelAfter={labelAfter} />  
    default:
      return <p>{type}</p>
  }
}


export default FormGroupTriage