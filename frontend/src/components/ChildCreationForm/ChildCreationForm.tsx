import {SubmitHandler, useForm} from "react-hook-form";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import InputWrapper from "./InputWrapper.tsx";
import FormInput from "../common/FormInput.tsx";
import {useEffect, useState} from "react";
import {GenderEnum} from "../../models/GenderEnum.tsx";
import {ChildModelMaximized} from "../../models/ChildModelMaximized.tsx";
import {BASE_API_URL} from "../../api/contst.ts";
import {useNavigate} from "react-router-dom";

interface FormData extends ChildModelMaximized {
    image: File
    gender: GenderEnum;
}

interface ChildCreationFormProps {
    editMode?: boolean;
    childId?: string;
}

function ChildCreationForm(props: ChildCreationFormProps) {
    //const currentChild: ChildModelMaximized | null = props.editMode && props.childId ? currentChildrenFull[parseInt(props.childId) -1] : null;
    // const fetcher: (url: string) => Promise<ChildModelMaximized> = async (url) => {
    //     const response = await fetch(url);
    //     if (!response.ok) {
    //         throw new Error(`API request failed with status ${response.status}`);
    //     }
    //     const jsonData: ChildModelMaximized = await response.json();
    //     Object.keys(jsonData).forEach(key => {
    //         setValue(key, jsonData[key]);
    //     });
    //     document.title = jsonData.first_name + ' ' + jsonData.surname;
    //
    //     return jsonData;
    // };
    // const {data} = useSWR<ChildModelMaximized>(BASE_API_URL + `/children/${parseInt(props.childId)}`, fetcher, );
    const navigate = useNavigate();
    useEffect(() => {
        const fetchData = async () => {
            try {
                // Perform your API call or any asynchronous operation to fetch data
                const response = await fetch(`${BASE_API_URL}/children/${parseInt(props.childId)}`);
                const jsonData: ChildModelMaximized = await response.json();
                Object.keys(jsonData).forEach(key => {
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-expect-error
                    setValue(key, jsonData[key]);
                });
                setPreview(jsonData.photo_path);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        // Call the fetchData function when the component mounts
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
        console.log(formData)
        setValue("relatives", [1]);
        setLoading(true);
        try {

            // Make POST request using Fetch API
            const response = await fetch(`${BASE_API_URL}/children/${props.editMode? parseInt(props.childId) + '/' : ''}`, {
                method: props.editMode ? 'PUT' : 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            // Check if request was successful
            if (!response.ok) throw new Error('Network response was not ok');

            navigate('/');

        } catch (error) {
            console.error('Error:', error.message);
            setError(true);
        } finally {
            setLoading(false);
        }
    };
    const validateGender = (value: GenderEnum) => {
        return value === GenderEnum.notDefined ? 'Pole wymagane' : true;
    };


    const handleUploadedFile = (event) => {
        const file = event.target.files[0];


        const urlImage = URL.createObjectURL(file);


        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        setPreview(urlImage);
    };

    return (
        <div className='mt-3'>
            <WidthWrapper>
                <form className='flex flex-col items-center border-main_red border-4 p-2 rounded-2xl'
                      onSubmit={handleSubmit(onSubmit)} onChange={()=>{setError(false)}}>
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
                                {...register('image', {})}
                                accept="image/*" // Allow only image files
                                onChange={handleUploadedFile}
                            />
                        </div>
                        <div className='flex flex-col sm:w-[90%] md:w-auto'>
                            <div className='flex flex-col sm:grid sm:grid-cols-2 xl:flex xl:flex-row'>
                                <FormInput name={'first_name'} type={'text'} label={'Imie'} register={register}
                                           rules={{required: 'Pole wymagane'}} error={errors.first_name}/>
                                <FormInput name={"second_name"} type={"text"} label={"Drugie Imie"} register={register}
                                           rules={{}} error={errors.second_name}/>
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
                </form>
            </WidthWrapper>
        </div>
    );
}

export default ChildCreationForm;