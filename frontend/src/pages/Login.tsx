import React from 'react';
import LoginForm from "../components/Auth/LoginForm.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import WidthWrapper from "../components/wrappers/WidthWrapper.tsx";

function Login(props) {
    return (
        <HeightWrapper>
            <WidthWrapper>
                <div>

                </div>
                <LoginForm/>
            </WidthWrapper>
        </HeightWrapper>

    );
}

export default Login;