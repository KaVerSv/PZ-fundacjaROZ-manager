import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import AddChildForm from './add-child.tsx'
//import './index.css'
import './add-child.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <AddChildForm/>
  </React.StrictMode>,
)
