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
    female = "female",
    male = "male"
}


function ChildCreationForm() {
    const {register, handleSubmit} = useForm<FormData>()
    const onSubmit: SubmitHandler<FormData> = (data) => {
        console.log(data)
    };

    return (
        <div className='bg-main_red mt-3'>
            <WidthWrapper>
                <form className='flex flex-col items-center' onSubmit={handleSubmit(onSubmit)}>
                    <div className='flex flex-col lg:flex-row'>
                        <div className='flex flex-col'>
                            <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                <InputWrapper labelFor="firstName" labelNote="Imie">
                                    <input type="text" id="firstName"
                                           placeholder="Imie" {...register('firstName')} />
                                </InputWrapper>
                                <InputWrapper labelFor="lastName" labelNote="Drugie Imie">
                                    <input type="text" id="lastName"
                                           placeholder="Drugie Imie" {...register('secondName')} />
                                </InputWrapper>
                                <InputWrapper labelFor="surname" labelNote="Nazwisko">
                                    <input type="text" id="surname" placeholder="Nazwisko" {...register('surname')} />
                                </InputWrapper>
                                <InputWrapper labelFor="gender" labelNote="Płeć">
                                    <select id="gender" {...register('gender')}>
                                        <option value={GenderEnum.male}>Male</option>
                                        <option value={GenderEnum.female}>Female</option>
                                    </select>
                                </InputWrapper>
                            </div>
                            <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                <InputWrapper labelFor="birthDate" labelNote="Data urodzenia">
                                    <input type="date" id="birthDate"
                                           placeholder="Data urodzenia" {...register('birthDate')} />
                                </InputWrapper>
                                <InputWrapper labelFor="birthplace" labelNote="Miejsce urodzenia">
                                    <input type="text" id="birthplace"
                                           placeholder="Miejsce urodzenia" {...register('birthplace')} />
                                </InputWrapper>
                                <InputWrapper labelFor="pesel" labelNote="PESEL">
                                    <input type="text" id="pesel" placeholder="PESEL" {...register('pesel')} />
                                </InputWrapper>
                            </div>
                            <div className='flex flex-col'>
                                <InputWrapper labelFor="Adres zamieszkania" labelNote="Residential Address">
                                    <input type="text" id="residentialAddress"
                                           placeholder="Residential Address" {...register('residentialAddress')} />
                                </InputWrapper>
                                <InputWrapper labelFor="registeredAddress" labelNote="Adres zameldowania">
                                    <input type="text" id="registeredAddress"
                                           placeholder="Adres zameldowania" {...register('registeredAddress')} />
                                </InputWrapper>
                            </div>
                            <div className='flex flex-col sm:flex-row'>
                                <InputWrapper labelFor="admissionDate" labelNote="Data przyjęcia">
                                    <input type="date" id="admissionDate"
                                           placeholder="Admission Date" {...register('admissionDate')} />
                                </InputWrapper>
                                <InputWrapper labelFor="leavingDate" labelNote="Data opuszczenia">
                                    <input type="date" id="leavingDate"
                                           placeholder="Leaving Date" {...register('leavingDate')} />
                                </InputWrapper>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button type="submit">Submit</button>
                    </div>


                </form>
            </WidthWrapper>

        </div>
    );
}

export default ChildCreationForm;