import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import RegistrationForm from "../components/Auth/RegistrationForm.tsx";
import {useEffect} from "react";


function Registration() {
    useEffect(() => {
        document.title = "Utwórz konto";
    }, []);
    return (
        <HeightWrapper>
            <div>
                <div className='flex h-10 w-full bg-main_white'></div>
                <div className='flex h-10 w-full bg-main_red mb-10'></div>
            </div>
            <div className='flex items-center  justify-center'>
                <RegistrationForm/>
            </div>
        </HeightWrapper>
    );
}

export default Registration;