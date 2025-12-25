import Alert from 'react-bootstrap/Alert'

const Messages = ({ text, color }) => {

  return (
    <Alert key={color} variant={color} dismissible >
           {text}
    </Alert>
  )
}

export default Messages