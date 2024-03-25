import {SubmitHandler, useForm} from "react-hook-form";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import InputWrapper from "./InputWrapper.tsx";
import FormInput from "../common/FormInput.tsx";
import {useState} from "react";
import {GenderEnum} from "../../models/GenderEnum.tsx";
import {ChildModelMaximized, currentChildrenFull} from "../../models/ChildModelMaximized.tsx";

interface FormData extends ChildModelMaximized {
    pesel: string;
    firstName: string;
    secondName: string;
    surname: string;
    birthDate: string;
    birthPlace: string;
    residentialAddress: string;
    registeredAddress: string;
    admissionDate: string;
    leavingDate: string;
    photoPath: string;
    image: File
    gender: GenderEnum;
}

interface ChildCreationFormProps {
    editMode?: boolean;
    childId?: string;
}

function ChildCreationForm(props: ChildCreationFormProps) {
    const currentChild: ChildModelMaximized | null = props.editMode && props.childId ? currentChildrenFull[parseInt(props.childId) -1] : null;
    const {register, handleSubmit, formState: {errors}} = useForm<FormData>({
        mode: 'onChange',
        defaultValues: currentChild
    })
    const [preview, setPreview] = useState();
    const onSubmit: SubmitHandler<FormData> = (data) => {
        console.log(data)
    };
    const validateGender = (value: GenderEnum) => {
        return value === GenderEnum.notDefined ? 'Pole wymagane' : true;
    };


    const handleUploadedFile = (event) => {
        const file = event.target.files[0];


        const urlImage = URL.createObjectURL(file);


        // @ts-ignore
        setPreview(urlImage);
    };

    return (
        <div className='mt-3'>
            <WidthWrapper>
                <form className='flex flex-col items-center border-main_red border-4 p-2 rounded-2xl'
                      onSubmit={handleSubmit(onSubmit)}>
                    <div className='flex flex-col lg:flex-row items-center'>
                        <div className='flex flex-col px-2 items-center'>
                            <div>
                                {!preview && <img className='px-1 rounded-2xl pb-2 w-56 sm:w-72'
                                                  src={currentChild ? currentChild!.photoPath : 'src/components/ChildCreationForm/profilowe.png'}
                                                  alt='profileImg'/>}
                                {preview && <img className='px-1 rounded-2xl pb-2 w-56 sm:w-72' src={preview} alt='profileImg'/>}
                            </div>
                            <input
                                className="appearance-none block w-64 sm:w-auto bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                type="file"
                                {...register('image', {})}
                                accept="image/*" // Allow only image files
                                onChange={handleUploadedFile}
                            />
                        </div>
                        <div className='flex flex-col sm:w-[90%] md:w-auto'>
                            <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                <FormInput name={'firstName'} type={'text'} label={'Imie'} register={register}
                                           rules={{required: 'Pole wymagane'}} error={errors.firstName}/>
                                <FormInput name={"secondName"} type={"text"} label={"Drugie Imie"} register={register}
                                           rules={{}} error={errors.secondName}/>
                                <FormInput name={"surname"} type={"text"} label={"Nazwisko"} register={register}
                                           rules={{required: 'Pole wymagane'}} error={errors.surname}/>
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
                                           rules={{required: 'Pole wymagane'}} error={errors.birthDate}/>
                                <FormInput name={"birthPlace"} type={"text"} label={"Miejsce urodzenia"}
                                           register={register} rules={{required: 'Pole wymagane'}}
                                           error={errors.birthPlace}/>
                                <FormInput name={"pesel"} type={"text"} label={"PESEL"} register={register}
                                           rules={{required: 'Pole wymagane'}} error={errors.pesel}/>
                            </div>
                            <div className='flex flex-col'>
                                <FormInput name={"residentialAddress"} type={"text"} label={"Adres zamieszkania"}
                                           register={register} rules={{required: 'Pole wymagane'}}
                                           error={errors.residentialAddress}/>
                                <FormInput name={"registeredAddress"} type={"text"} label={"Adres zameldowania"}
                                           register={register} rules={{required: 'Pole wymagane'}}
                                           error={errors.registeredAddress}/>
                            </div>
                            <div className='flex flex-col sm:flex-row'>
                                <FormInput name={"admissionDate"} type={"date"} label={"Data przyjęcia"}
                                           register={register} rules={{required: 'Pole wymagane'}}
                                           error={errors.admissionDate}/>
                                <FormInput name={"leavingDate"} type={"date"} label={"Data opuszczenia"}
                                           register={register} rules={{required: 'Pole wymagane'}}
                                           error={errors.leavingDate}/>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button
                            className='mt-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded'
                            type="submit">
                            {currentChild? 'Zapisz zmiany' : 'Dodaj dziecko'}
                        </button>
                    </div>
                </form>
            </WidthWrapper>
        </div>
    );
}

export default ChildCreationForm;