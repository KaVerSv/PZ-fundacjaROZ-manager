import {SubmitHandler, useForm} from "react-hook-form";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import FormInput from "../common/FormInput.tsx";
import {useEffect, useState} from "react";
import {ChildModelMaximized} from "../../models/ChildModelMaximized.tsx";
import {BASE_API_URL} from "../../api/contst.ts";
import {useNavigate} from "react-router-dom";
import fetchImage from "../../api/fetchImage.ts";


interface FormData extends ChildModelMaximized {
    image: File
}

interface ChildCreationFormProps {
    editMode?: boolean;
    childId?: string;
}

function ChildCreationForm(props: ChildCreationFormProps) {

    const navigate = useNavigate();
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`${BASE_API_URL}/children/${parseInt(props.childId)}`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem("token")}`
                    }
                });
                const jsonData: ChildModelMaximized = await response.json();
                Object.keys(jsonData).forEach(key => {
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-expect-error
                    setValue(key, jsonData[key]);
                });
                const url = await fetchImage(`${BASE_API_URL}/children/${parseInt(props.childId)}/photo`);
                setPreview(url);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        if (props.editMode) fetchData();
    }, []);

    const {
        register,
        handleSubmit,
        formState: {errors},
        setValue,
    } = useForm<FormData>({
        mode: 'onChange'
    })
    const [preview, setPreview] = useState<string>();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);
    const onSubmit: SubmitHandler<FormData> = async (formData) => {
        setLoading(true);
        setValue('leaving_date', formData.leaving_date === "" ? null : formData.leaving_date)
        try {
            let response = await fetch(`${BASE_API_URL}children/${props.editMode ? parseInt(props.childId) + '/' : ''}`, {
                method: props.editMode ? 'PUT' : 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) throw new Error('Network response was not ok');
            if (formData.image) {
                const data = await response.json();
                const id = data.id;
                const formDataToSend = new FormData();
                formDataToSend.append('photo', formData.image)

                response = await fetch(`${BASE_API_URL}children/${id}/photo/`, {
                    method: 'PUT',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem("token")}`
                    },
                    body: formDataToSend,
                });
                if (!response.ok) throw new Error('Network response was not ok');
            }

            if (props.editMode) {
                navigate(`/children/${props.childId}`)
            } else navigate('/');

        } catch (error) {
            console.error('Error:', error.message);
            setError(true);
        } finally {
            setLoading(false);
        }
    };

    const handleUploadedFile = (event) => {
        const file = event.target.files[0];

        setValue('image', file);
        const urlImage = URL.createObjectURL(file);

        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        setPreview(urlImage);
    };

    return (
        <div className='mt-3'>
            <WidthWrapper>
                <form className='flex flex-col items-center border-main_red border-4 p-2 rounded-2xl'
                      onSubmit={handleSubmit(onSubmit)} onChange={() => {
                    setError(false)
                }}>
                    <div className='flex flex-col items-center'>
                        <div className='flex flex-col lg:flex-row items-center'>
                            <div className='flex flex-col px-2 items-center'>
                                <div>
                                    {!preview && <img className='px-1 rounded-2xl pb-2 w-56 sm:w-72'
                                                      src="../../../public/profilowe.png"
                                                      alt='profileImg'/>}
                                    {preview && <img className='px-1 rounded-2xl pb-2 w-56 sm:w-72' src={preview}
                                                     alt='profileImg'/>}
                                </div>
                                <input
                                    className="appearance-none block w-64 sm:w-auto bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                                    type="file"
                                    accept="image/*" // Allow only image files
                                    onChange={handleUploadedFile}
                                />
                            </div>
                            <div className='flex flex-col sm:w-[90%] md:w-auto'>
                                <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                    <FormInput name={'first_name'} type={'text'} label={'Imię'} register={register}
                                               rules={{required: 'Pole wymagane'}} error={errors.first_name}/>
                                    <FormInput name={"second_name"} type={"text"} label={"Drugie Imię"}
                                               register={register}
                                               rules={{}} error={errors.second_name}/>
                                    <FormInput name={"surname"} type={"text"} label={"Nazwisko"} register={register}
                                               rules={{required: 'Pole wymagane'}} error={errors.surname}/>
                                    {/*<InputWrapper labelFor="gender" labelNote="Płeć" error={errors.gender}>*/}
                                    {/*    <select*/}
                                    {/*        className="appearance-none block min-w-40 w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"*/}
                                    {/*        id="gender" {...register('gender', {*/}
                                    {/*        required: true,*/}
                                    {/*        validate: validateGender*/}
                                    {/*    })}*/}
                                    {/*        defaultValue={GenderEnum.notDefined}>*/}
                                    {/*        <option disabled hidden value={GenderEnum.notDefined}>Płeć</option>*/}
                                    {/*        <option value={GenderEnum.male}>Mężczyzna</option>*/}
                                    {/*        <option value={GenderEnum.female}>Kobieta</option>*/}
                                    {/*    </select>*/}
                                    {/*    <div*/}
                                    {/*        className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">*/}
                                    {/*        <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg"*/}
                                    {/*             viewBox="0 0 20 20">*/}
                                    {/*            <path*/}
                                    {/*                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>*/}
                                    {/*        </svg>*/}
                                    {/*    </div>*/}
                                    {/*</InputWrapper>*/}
                                </div>
                                <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                    <FormInput name={"birth_date"} type={"date"} label={"Data urodzenia"}
                                               register={register}
                                               rules={{required: 'Pole wymagane'}} error={errors.birth_date}/>
                                    <FormInput name={"birthplace"} type={"text"} label={"Miejsce urodzenia"}
                                               register={register} rules={{required: 'Pole wymagane'}}
                                               error={errors.birthplace}/>
                                    <FormInput name={"pesel"} type={"text"} label={"PESEL"} register={register}
                                               rules={{required: 'Pole wymagane'}} error={errors.pesel}/>
                                </div>
                                <div className='flex flex-col'>
                                    <FormInput name={"residential_address"} type={"text"} label={"Adres zamieszkania"}
                                               register={register} rules={{required: 'Pole wymagane'}}
                                               error={errors.residential_address}/>
                                    <FormInput name={"registered_address"} type={"text"} label={"Adres zameldowania"}
                                               register={register} rules={{required: 'Pole wymagane'}}
                                               error={errors.registered_address}/>
                                </div>
                                <div className='flex flex-col sm:flex-row'>
                                    <FormInput name={"admission_date"} type={"date"} label={"Data przyjęcia"}
                                               register={register} rules={{required: 'Pole wymagane'}}
                                               error={errors.admission_date}/>
                                    <FormInput name={"leaving_date"} type={"date"} label={"Data opuszczenia"}
                                               register={register}
                                               error={errors.leaving_date}/>
                                </div>
                            </div>
                        </div>
                        <div>
                            {error && <div className='flex justify-center'>
                                <span className='text-sm text-red-800'>Coś poszło nie tak.<br/>Sprobuj ponownie</span>
                            </div>}
                            <button
                                className='mt-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded disabled:opacity-30'
                                type="submit"
                                disabled={loading}>
                                {props.editMode ? 'Zapisz zmiany' : 'Dodaj dziecko'}
                            </button>
                        </div>
                    </div>

                </form>
            </WidthWrapper>
        </div>
    );
}

export default ChildCreationForm;