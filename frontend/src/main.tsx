import React from 'react'
import ReactDOM from 'react-dom/client'
import AddChildForm from './add-child.tsx'
import ChildrenComponent from './children.tsx'
import './add-child.css'


ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    {/* <AddChildForm/> */}
    <ChildrenComponent/>
  </React.StrictMode>,
)