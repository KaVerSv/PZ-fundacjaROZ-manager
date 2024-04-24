import LoginForm from "../components/Auth/LoginForm.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import {useEffect} from "react";

function Login() {
    useEffect(() => {
        document.title = "Zaloguj się";
    }, []);
    return (
        <HeightWrapper>
            <div>
                <div className='flex h-10 w-full bg-main_white'></div>
                <div className='flex h-10 w-full bg-main_red mb-10'></div>
            </div>
            <div className='flex items-center h-[60vh] justify-center'>
                <LoginForm/>
            </div>
        </HeightWrapper>

    );
}

export default Login;