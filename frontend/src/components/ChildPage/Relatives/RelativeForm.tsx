import {SubmitHandler, useForm} from "react-hook-form";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useEffect, useState} from "react";
import FormInput from "../../common/FormInput.tsx";
import {Mode} from "../Mode.ts";
import {RelativeModel} from "../../../models/RelativeModel.ts";
import InputWrapper from "../../ChildCreationForm/InputWrapper.tsx";

interface Props {
    toggleReload: () => void;
    toggleShowForm: () => void;
    mode: Mode;
    childId: string;
    relative?: RelativeModel;
}


function RelativeForm(props: Props) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    const {
        register,
        handleSubmit,
        formState: {errors, isValid},
        setFocus,
        setValue,
        getValues
    } = useForm<RelativeModel>({
        mode: "onChange",
        defaultValues: {
            id: props.relative?.id,
            first_name: props.relative?.first_name,
            second_name: props.relative?.second_name,
            surname: props.relative?.surname,
            phone_number: props.relative?.phone_number,
            residential_address: props.relative?.residential_address,
            e_mail: props.relative?.e_mail,
            legal_status: props.relative?.legal_status,
            alive: props.relative?.alive
        }
    },);

    useEffect(() => {
        setFocus('first_name');
    }, []);

    const onSubmit: SubmitHandler<RelativeModel> = async (relativeFormData) => {
        setLoading(true);
        setValue('alive', getValues('alive') === 'true')
        try {
            const response = await fetch( `${BASE_API_URL}${props.mode === Mode.edit ? `relatives/${props.relative.id}/` :  `children/${props.childId}/relatives/`}`   , {
                method: props.mode === Mode.edit ? 'PUT' : 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(relativeFormData),
            });
            if (!response.ok) {
                throw new Error(`API request failed with status ${response.status}`);
            } else {
                props.toggleShowForm();
                props.toggleReload();
            }
        } catch
            (error) {
            console.error('Error:', error.message);
            setError(true);
        } finally {
            setLoading(false);
        }
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}
              className={`${props.mode === Mode.create ? 'bg-amber-500' : ''} w-full bg-opacity-30 rounded-2xl py-1 flex flex-col pt-2`}>
            <FormInput name={"first_name"} type={"text"} label={"Imię"}
                       register={register}
                       error={errors.first_name}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"second_name"} type={"text"} label={"Drugie Imię"}
                       register={register}
                       error={errors.second_name}/>
            <FormInput name={"surname"} type={"text"} label={"Nazwisko"}
                       register={register}
                       error={errors.surname}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"e_mail"} type={"text"} label={"Email"}
                       register={register}
                       error={errors.e_mail}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"residential_address"} type={"text"} label={"Adres zamieszkania"}
                       register={register}
                       error={errors.residential_address}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"phone_number"} type={"text"} label={"Telefon"}
                       register={register}
                       error={errors.phone_number}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"legal_status"} type={"text"} label={"Status Prawny"}
                       register={register}
                       error={errors.legal_status}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <InputWrapper labelFor="alive" labelNote="Żyje" alwaysShowLabel={true} error={errors.alive}>
                <select
                    className="appearance-none block min-w-40 w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id="alive" {...register('alive', {
                    required: true,
                })}>
                    <option selected={true} value={'true'}>Tak</option>
                    <option value={'false'}>Nie</option>
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
            <div className='w-full text-right'>
                {error && <div className='flex justify-center'>
                    <span className='text-sm text-red-800'>Coś poszło nie tak.<br/>Sprobuj ponownie</span>
                </div>}
                <button
                    className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey mr-2 mb-1"
                    type="button"
                    onClick={props.toggleShowForm}>
                    Odrzuć zmiany
                </button>
                <button
                    disabled={!isValid || loading}
                    className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey mr-2 mb-1"
                    type="submit">
                    {props.mode === Mode.create ? 'Dodaj rodzica' : 'Zapisz zmiany'}
                </button>
            </div>

        </form>
    );
}

export default RelativeForm;