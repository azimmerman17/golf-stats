import { useState } from 'react'
import { useFloating, useDismiss, useRole, useClick, useInteractions, useId, FloatingFocusManager, FloatingOverlay, FloatingPortal} from '@floating-ui/react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import EquipmentDetails from './EquipmentDetails';

const EquipmentItem = ({ item }) => {
  const [ open, setOpen ] = useState(false)

  const { club, spec, distance } = item
  const { catagory, make, model, name, short_name, active } = club

  // define border color for button
  let variantList = [
    {catagory: 'Driver', variant: 'dark'},
    {catagory: 'Wood', variant:'secondary'},
    {catagory: 'Hybrid', variant:'warning'},
    {catagory: 'Iron', variant:'danger'},
    {catagory: 'Wedge', variant:'primary'},
    {catagory: 'Putter', variant:'succes'},
   ]

   let variant = variantList.filter(l => l.catagory == catagory)[0] ? variantList.filter(l => l.catagory == catagory)[0].variant : 'info'

  // Floating UI box logic
  const { refs, context } = useFloating({
    open: open,
    onOpenChange: setOpen
  })

  // Set Floating UI Props
  const click = useClick(context)
  const role = useRole(context)
  const dismiss = useDismiss(context, { outsidePressEvent: 'mousedown' })

  const { getReferenceProps, getFloatingProps } = useInteractions([
    click,
    role,
    dismiss
  ]);

  const headingId = useId();
  const descriptionId = useId()

  return (
    <>
      <Button variant={variant} className='p-1 my-1 text-center shadow-lg w-100 h-100' ref={refs.setReference} {...getReferenceProps()}>
        <Card className='m-0 p-0'>
          <Card.Body className='m-0 p-1 w-100 h-100'>
            <Card.Title className='mt-1 pt-1 mb-2 pb-0'>{short_name}</Card.Title>
            <Card.Text className='m-0 fs-6'>{make}</Card.Text>
            <Card.Text className='m-0 mb-2 fs-6'>{model}</Card.Text>
          </Card.Body>
        </Card>
      </Button>      
      {open ?  (
        <FloatingPortal>
          <FloatingOverlay className='Data-Dialog-overlay player-dialog' lockScroll>
            <FloatingFocusManager context={context}>
              <Container className='Data-Dialog' ref={refs.setFloating} aria-labelledby={headingId} aria-describedby={descriptionId} {...getFloatingProps()}>
                <EquipmentDetails item={item} />
              </Container>
            </FloatingFocusManager>
          </FloatingOverlay>
        </FloatingPortal>
      ) : null}
    </>

  )
}

export default EquipmentItem