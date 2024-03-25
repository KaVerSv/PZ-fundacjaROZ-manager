import {SubmitHandler, useForm} from "react-hook-form";
import BigLogo from "./BigLogo.tsx";
import FormInput from "../common/FormInput.tsx";
import {Link} from "react-router-dom";

interface FormData {
    email: string;
    name: string;
    surname: string;
    pesel: string;
    password: string;
    password_confirm: string;
}

function RegistrationForm() {

    const {register, handleSubmit, formState: {errors}} = useForm<FormData>({
        mode: 'onChange'
    });

    const onSubmit: SubmitHandler<FormData> = (data) => {
        console.log(data)
    };

    return (
        <div className='flex gap-5 p-2'>
            <div className='hidden lg:block'>
                <BigLogo/>
            </div>

            <div className='flex flex-col gap-7 bg-main_red px-4 py-5 rounded-xl sm:px-10'>
                <div className='flex justify-center'>
                    <span className='text-2xl text-main_white'>Utwórz konto</span>
                </div>
                <div>
                    <form className='flex flex-col gap-3' onSubmit={handleSubmit(onSubmit)}>
                        <FormInput name={'email'} type={'text'} label={'Email'} register={register}
                                   error={errors.email} labelColor='text-main_white'></FormInput>
                        <FormInput name={'name'} type={'text'} label={'Imie'} register={register}
                                   error={errors.password} labelColor='text-main_white'/>
                        <FormInput name={'surname'} type={'text'} label={'Nazwisko'} register={register}
                                   error={errors.password} labelColor='text-main_white'/>
                        <FormInput name={'pesel'} type={'text'} label={'Pesel'} register={register}
                                   error={errors.password} labelColor='text-main_white'/>
                        <FormInput name={'password'} type={'password'} label={'Hasło'} register={register}
                                   error={errors.password} labelColor='text-main_white'/>
                        <FormInput name={'password_confirm'} type={'password'} label={'Powtórz haslo'}
                                   register={register}
                                   error={errors.password} labelColor='text-main_white'/>
                        <button
                            className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline"
                            type="submit">
                            Utwórz konto
                        </button>
                    </form>
                </div>
                <div>
                    <div className='flex justify-center gap-6 sm:gap-10'>
                        <Link to={'/login'}>
                            <div>
                                <span className='text-main_white opacity-70 hover:underline'>Zaloguj się</span>
                            </div>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default RegistrationForm;