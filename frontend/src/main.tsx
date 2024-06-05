import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./pages/Home.tsx";
import ChildCreationPage from "./pages/ChildCreationPage.tsx";
import ChildPage from "./pages/ChildPage.tsx";
import ChildEditPage from "./pages/ChildEditPage.tsx";
import Login from "./pages/Login.tsx";
import Registration from "./pages/Registration.tsx";
import {AuthProvider} from "./context/AuthProvider.tsx";
import RequireAuth from "./components/Auth/RequireAuth.tsx";


ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <BrowserRouter>
            <AuthProvider>
                <Routes>
                    <Route element={<RequireAuth/>}>
                        <Route path="/" element={<Home/>}/>
                        <Route path="/addchild" element={<ChildCreationPage/>}/>
                        <Route path="/children/:id" element={<ChildPage/>}/>
                        <Route path="/children-edit/:id" element={<ChildEditPage/>}/>
                    </Route>

                    <Route path="/registration" element={<Registration/>}/>
                    <Route path="/login" element={<Login/>}/>
                </Routes>
            </AuthProvider>
        </BrowserRouter>
    </React.StrictMode>,
)
