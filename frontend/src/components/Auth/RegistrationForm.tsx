import {SubmitHandler, useForm} from "react-hook-form";
import BigLogo from "./BigLogo.tsx";
import FormInput from "../common/FormInput.tsx";
import {Link} from "react-router-dom";

interface FormData {
    email: string;
    name: string;
    surname: string;
    //pesel: string;
    password: string;
    password_confirm: string;
}

function RegistrationForm() {

    const {register, handleSubmit, formState: { errors, isValid }, getValues} = useForm<FormData>({
        mode: 'onChange'
    });

    const onSubmit: SubmitHandler<FormData> = (data) => {
        console.log(data)
    };

    const validatePasswordMatch = (value: string) => {
        if (value !== getValues("password")) {
            return "Hasłą musą się zgadzać";
        }
        return true;
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
                                   error={errors.email}
                                   rules={{
                                       required: 'Pole wymagane',
                                       pattern: {
                                           value: /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                                           message: 'Niewłaściwy adres e-mail',
                                       }
                                   }}
                                   labelColor='text-main_white'></FormInput>
                        <FormInput name={'name'} type={'text'} label={'Imie'} register={register}
                                   error={errors.name}
                                   rules={{
                                       required: 'Pole wymagane'
                                   }}
                                   labelColor='text-main_white'/>
                        <FormInput name={'surname'} type={'text'} label={'Nazwisko'} register={register}
                                   error={errors.surname}
                                   rules={{
                                       required: 'Pole wymagane'
                                   }}
                                   labelColor='text-main_white'/>
                        {/*<FormInput name={'pesel'} type={'text'} label={'Pesel'} register={register}*/}
                        {/*           error={errors.pesel}*/}
                        {/*           rules={{*/}
                        {/*               required: 'Pole wymagane',*/}
                        {/*               minLength: {value: 11, message: 'Niewłaściwy PESEL'},*/}
                        {/*               maxLength: {value: 11, message: 'Niewłaściwy PESEL'}*/}
                        {/*           }}*/}
                        {/*           labelColor='text-main_white'/>*/}
                        <FormInput name={'password'} type={'password'} label={'Hasło'} register={register}
                                   error={errors.password}
                                   rules={{
                                       required: 'Pole wymagane',
                                       minLength: {value: 6, message: 'Minimum 6 znaków'},
                                       maxLength: {value: 18, message: 'Maximum 18 znaków'}
                                   }}
                                   labelColor='text-main_white'/>
                        <FormInput name={'password_confirm'} type={'password'} label={'Powtórz haslo'}
                                   register={register}
                                   error={errors.password_confirm}
                                   rules={{
                                       required: 'Pole wymagane',
                                       validate: {
                                           validatePasswordMatch
                                       }
                                   }}
                                   labelColor='text-main_white'/>
                        <button
                            disabled={!isValid}
                            className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey"
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