import BigLogo from "./BigLogo.tsx";
import FormInput from "../common/FormInput.tsx";
import {SubmitHandler, useForm} from "react-hook-form";
import {Link, useLocation, useNavigate} from "react-router-dom";
import {BASE_API_URL} from "../../api/contst.ts";
import {useEffect, useState} from "react";

interface FormData {
    email: string;
    password: string;
}

function LoginForm() {
    const navigate = useNavigate();
    const location = useLocation();
    const [loginError, setLoginError] = useState(false);
    const {register, handleSubmit, formState: {errors, isValid}, setFocus} = useForm<FormData>({
        mode: 'onChange'
    });

    useEffect(() => {
        setFocus('email');
    }, [])

    const onSubmit: SubmitHandler<FormData> = async (formData) => {
        try {
            const response = await fetch(BASE_API_URL + '/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({email: formData.email, password: formData.password}),
            });
            if (!response.ok) {
                throw new Error('Invalid credentials');
            }

            const data = await response.json();
            const jwtToken = data.token;
            localStorage.setItem("token", jwtToken);

            const from = location.state?.from?.pathname || '/'
            navigate(from, {replace: true});
        } catch (error) {
            setLoginError(true);
        }
    };

    const onFocus = () => {
        setLoginError(false)
    }

    return (
        <div className='flex gap-5 p-2'>
            <div className='hidden lg:block'>
                <BigLogo/>
            </div>

            <div className='flex flex-col gap-7 bg-main_red px-4 py-5 rounded-xl sm:px-10'>
                <div className='flex justify-center'>
                    <span className='text-2xl text-main_white'>Zaloguj się</span>
                </div>
                <div>
                    <form className='flex flex-col gap-3' onSubmit={handleSubmit(onSubmit)} onFocus={onFocus}>
                        <FormInput name={'email'} type={'text'} label={'Email'} register={register}
                                   error={errors.email}
                                   rules={{
                                       required: 'Pole wymagane',
                                       pattern: {
                                           value: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                                           message: 'Niewłaściwy adres e-mail',
                                       }
                                   }}
                                   labelColor='text-main_white'/>
                        <FormInput name={'password'} type={'password'} label={'Hasło'} register={register}
                                   error={errors.password} rules={{required: 'Pole wymagane'}}
                                   labelColor='text-main_white'/>
                        {loginError && <div className='flex justify-center'>
                            <span className='text-red-600'>Niepoprawny email lub hasło</span>
                        </div>}
                        <button
                            disabled={!isValid}
                            className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey"
                            type="submit">
                            Zalogouj się
                        </button>
                    </form>
                </div>
                <div>
                    <div className='flex justify-center gap-6 sm:gap-10'>
                        <Link to={'/'}>
                            <div>
                                <span className='text-main_white opacity-70 hover:underline'>Zapomniałem hasła</span>
                            </div>
                        </Link>

                        <Link to={'/registration'}>
                            <div>
                                <span className='text-main_white opacity-70 hover:underline'>Utwórz konto</span>
                            </div>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default LoginForm;