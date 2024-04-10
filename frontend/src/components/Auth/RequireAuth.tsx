import {Navigate, Outlet, useLocation} from "react-router-dom";

const RequireAuth = () =>{
    const location = useLocation();
    const token = localStorage.getItem("token");
    return(
        !isTokenExpired(token) ?
            <Outlet/> :
            <Navigate to={'/login'} state={{from: location}} replace/>
    )
}

function isTokenExpired(token) {
    if (!token) {
        return true; // Token is considered expired if it doesn't exist
    }
    const tokenData = JSON.parse(atob(token.split('.')[1]));
    const expirationTime = tokenData.exp * 1000;
    return Date.now() >= expirationTime;
}
export default RequireAuth;