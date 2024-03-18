import {SubmitHandler, useForm} from "react-hook-form";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import InputWrapper from "./InputWrapper.tsx";

interface FormData {
    pesel: string;
    firstName: string;
    secondName: string;
    surname: string;
    birthDate: string;
    birthplace: string;
    residentialAddress: string;
    registeredAddress: string;
    admissionDate: string;
    leavingDate: string;
    photoPath: string;
    gender: GenderEnum;
}

enum GenderEnum {
    notDefined = "not",
    female = "female",
    male = "male"
}


function ChildCreationForm() {
    const {register, handleSubmit} = useForm<FormData>()
    const onSubmit: SubmitHandler<FormData> = (data) => {
        console.log(data)
    };

    return (
        <div className='mt-3'>
            <WidthWrapper>
                <form className='flex flex-col items-center border-main_red border-r-4'
                      onSubmit={handleSubmit(onSubmit)}>
                    <div className='flex flex-col lg:flex-row'>
                        <div className='flex items-center'>
                            <input
                                className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"

                                type="file"
                                accept="image/*" // Allow only image files
                            />
                        </div>
                        <div className='flex flex-col'>
                            <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                <InputWrapper labelFor="firstName" labelNote="Imie">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="firstName"
                                        placeholder="Imie" {...register('firstName')} />
                                </InputWrapper>
                                <InputWrapper labelFor="lastName" labelNote="Drugie Imie">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="lastName"
                                        placeholder="Drugie Imie" {...register('secondName')} />
                                </InputWrapper>
                                <InputWrapper labelFor="surname" labelNote="Nazwisko">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="surname" placeholder="Nazwisko" {...register('surname')} />
                                </InputWrapper>
                                <InputWrapper labelFor="gender" labelNote="Płeć">
                                    <select
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        id="gender" {...register('gender')} defaultValue={GenderEnum.notDefined}>
                                        <option disabled hidden value={GenderEnum.notDefined}>Płeć</option>
                                        <option value={GenderEnum.male}>Mężczyzna</option>
                                        <option value={GenderEnum.female}>Kobieta</option>
                                    </select>
                                    <div
                                        className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                                        <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg"
                                             viewBox="0 0 20 20">
                                            <path
                                                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                                        </svg>
                                    </div>
                                </InputWrapper>
                            </div>
                            <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                <InputWrapper labelFor="birthDate" labelNote="Data urodzenia" alwaysShowLabel={true}>
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="date" id="birthDate"
                                        placeholder="Data urodzenia" {...register('birthDate')} />
                                </InputWrapper>
                                <InputWrapper labelFor="birthplace" labelNote="Miejsce urodzenia">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="birthplace"
                                        placeholder="Miejsce urodzenia" {...register('birthplace')} />
                                </InputWrapper>
                                <InputWrapper labelFor="pesel" labelNote="PESEL">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="pesel" placeholder="PESEL" {...register('pesel')} />
                                </InputWrapper>
                            </div>
                            <div className='flex flex-col'>
                                <InputWrapper labelFor="Adres zamieszkania" labelNote="Residential Address">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="residentialAddress"
                                        placeholder="Residential Address" {...register('residentialAddress')} />
                                </InputWrapper>
                                <InputWrapper labelFor="registeredAddress" labelNote="Adres zameldowania">
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="text" id="registeredAddress"
                                        placeholder="Adres zameldowania" {...register('registeredAddress')} />
                                </InputWrapper>
                            </div>
                            <div className='flex flex-col sm:flex-row'>
                                <InputWrapper labelFor="admissionDate" labelNote="Data przyjęcia" alwaysShowLabel={true}>
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="date" id="admissionDate"
                                        placeholder="Admission Date" {...register('admissionDate')} />
                                </InputWrapper>
                                <InputWrapper labelFor="leavingDate" labelNote="Data opuszczenia" alwaysShowLabel={true}>
                                    <input
                                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        type="date" id="leavingDate"
                                        placeholder="Leaving Date" {...register('leavingDate')} />
                                </InputWrapper>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button
                            type="submit">Submit
                        </button>
                    </div>
                </form>
            </WidthWrapper>

        </div>
    );
}

export default ChildCreationForm;