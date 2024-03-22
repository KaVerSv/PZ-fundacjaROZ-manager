import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import Home from "./pages/Home.tsx";
import ChildCreationPage from "./pages/ChildCreationPage.tsx";
import ChildPage from "./pages/ChildPage.tsx";
import ChildEditPage from "./pages/ChildEditPage.tsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Home/>,
    },
    {
        path: "/addchild",
        element: <ChildCreationPage/>,
    },
    {
        path: "/children/:id",
        element: <ChildPage/>
    },
    {
        path: "/children-edit/:id",
        element: <ChildEditPage/>
    }
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <RouterProvider router={router}/>
    </React.StrictMode>,
)
