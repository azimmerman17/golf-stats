const InfoDisplay = ({data, label}) => {
  return (
    <div className='text-center my-2'>
      <h6 className='m-0'>{data}</h6>
      <p className='text-muted mb-0'><small>{label}</small></p>
    </div>
  )
}

export default InfoDisplay