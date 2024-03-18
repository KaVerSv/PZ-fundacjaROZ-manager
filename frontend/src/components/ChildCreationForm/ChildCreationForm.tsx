import {SubmitHandler, useForm} from "react-hook-form";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import InputWrapper from "./InputWrapper.tsx";
import FormInput from "./FormInput.tsx";

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
    const {register, handleSubmit, formState: {errors}} = useForm<FormData>({
        mode: 'onChange'

    })
    const onSubmit: SubmitHandler<FormData> = (data) => {
        console.log(data)
    };
    const validateGender = (value: GenderEnum) => {
        return value === GenderEnum.notDefined ? 'Pole Obowiązkowe' : true;
    };
    return (
        <div className='mt-3'>
            <WidthWrapper>
                <form className='flex flex-col items-center border-main_red border-4 p-2 rounded-2xl'
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
                                <FormInput name={'firstName'} type={'text'} label={'Imie'} register={register}
                                           rules={{required: 'Pole Obowiązkowe'}} error={errors.firstName}/>
                                <FormInput name={"secondName"} type={"text"} label={"Drugie Imie"} register={register}
                                           rules={{required: 'Pole Obowiązkowe'}} error={errors.secondName}/>
                                <FormInput name={"surname"} type={"text"} label={"Nazwisko"} register={register}
                                           rules={{required: 'Pole Obowiązkowe'}} error={errors.surname}/>
                                <InputWrapper labelFor="gender" labelNote="Płeć" error={errors.gender}>
                                    <select
                                        className="appearance-none block min-w-40 w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                        id="gender" {...register('gender', {required: true, validate: validateGender})}
                                        defaultValue={GenderEnum.notDefined}>
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
                                <FormInput name={"birthDate"} type={"date"} label={"Data urodzenia"} register={register}
                                           rules={{required: 'Pole Obowiązkowe'}} error={errors.birthDate}/>
                                <FormInput name={"birthplace"} type={"text"} label={"Miejsce urodzenia"}
                                           register={register} rules={{required: 'Pole Obowiązkowe'}}
                                           error={errors.birthplace}/>
                                <FormInput name={"pesel"} type={"text"} label={"PESEL"} register={register}
                                           rules={{required: 'Pole Obowiązkowe'}} error={errors.pesel}/>
                            </div>
                            <div className='flex flex-col'>
                                <FormInput name={"residentialAddress"} type={"text"} label={"Adres zamieszkania"}
                                           register={register} rules={{required: 'Pole Obowiązkowe'}}
                                           error={errors.residentialAddress}/>
                                <FormInput name={"registeredAddress"} type={"text"} label={"Adres zameldowania"}
                                           register={register} rules={{required: 'Pole Obowiązkowe'}}
                                           error={errors.registeredAddress}/>
                            </div>
                            <div className='flex flex-col sm:flex-row'>
                                <FormInput name={"admissionDate"} type={"date"} label={"Data przyjęcia"}
                                           register={register} rules={{required: 'Pole Obowiązkowe'}}
                                           error={errors.admissionDate}/>
                                <FormInput name={"leavingDate"} type={"date"} label={"Data opuszczenia"}
                                           register={register} rules={{required: 'Pole Obowiązkowe'}}
                                           error={errors.leavingDate}/>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button
                            className='mt-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded'
                            type="submit">Dodaj dziecko
                        </button>
                    </div>
                </form>
            </WidthWrapper>
        </div>
    );
}

export default ChildCreationForm;