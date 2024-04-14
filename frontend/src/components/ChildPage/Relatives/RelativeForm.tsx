import {SubmitHandler, useForm} from "react-hook-form";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useEffect, useState} from "react";
import FormInput from "../../common/FormInput.tsx";
import {Mode} from "../Mode.ts";
import {RelativeModel} from "../../../models/RelativeModel.ts";

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
        }
    },);

    useEffect(() => {
        setFocus('first_name');
    }, []);

    const onSubmit: SubmitHandler<RelativeModel> = async (relativeFormData) => {
        setLoading(true);
        console.log(relativeFormData);
        try {
            const response = await fetch(Mode.edit ? `${BASE_API_URL}children/${props.childId}/relatives/` :  `${BASE_API_URL}relatives/${props.relative.id}/`, {
                method: props.mode === Mode.edit ? 'PUT' : 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(relativeFormData),
            });
            console.log(response);
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
            <div className='w-full text-right'>
                {error && <div className='flex justify-center'>
                    <span className='text-sm text-red-800'>Coś poszło nie tak.<br/>Sprobuj ponownie</span>
                </div>}
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