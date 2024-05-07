import {SubmitHandler, useForm} from "react-hook-form";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useEffect, useState} from "react";
import FormInput from "../../common/FormInput.tsx";
import {Mode} from "../Mode.ts";
import {SchoolModel} from "../../../models/ShoolModel.ts";

interface Props {
    toggleReload: () => void;
    toggleShowForm: () => void;
    mode: Mode;
    childId: string;
    school?: SchoolModel;
}


function SchoolForm(props: Props) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    const {
        register,
        handleSubmit,
        formState: {errors, isValid},
        setFocus,
        setValue,
        getValues
    } = useForm<SchoolModel>({
        mode: "onChange",
        defaultValues: {
            id: props.school?.id,
            name: props.school?.name,
            address: props.school?.address,
            phone_number: props.school?.phone_number,
            e_mail: props.school?.e_mail,
            start_date: props.school?.start_date,
            end_date: props.school?.end_date
        }
    },);

    useEffect(() => {
        setFocus('name');
    }, []);

    const onSubmit: SubmitHandler<SchoolModel> = async (schoolFormData) => {
        setLoading(true);
        if(getValues("end_date") ==="") setValue('end_date', null)
        try {
            const response = await fetch( `${BASE_API_URL}${props.mode === Mode.edit ? `schools/${props.school.id}/` :  `children/${props.childId}/schools/`}`   , {
                method: props.mode === Mode.edit ? 'PUT' : 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(schoolFormData),
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
            <FormInput name={"name"} type={"text"} label={"Nazwa szkoły"}
                       register={register}
                       error={errors.name}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"address"} type={"text"} label={"Adres szkoły"}
                       register={register}
                       error={errors.address}/>
            <FormInput name={"phone_number"} type={"text"} label={"Telefon"}
                       register={register}
                       error={errors.phone_number}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"e_mail"} type={"text"} label={"Email"}
                       register={register}
                       error={errors.e_mail}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"start_date"} type={"date"} label={"Rozpoczęto naukę"}
                       register={register} rules={{required: 'Pole wymagane'}}
                       error={errors.start_date}/>
            <FormInput name={"end_date"} type={"date"} label={"Ukończono naukę"}
                       register={register}
                       error={errors.end_date}/>
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
                    {props.mode === Mode.create ? 'Dodaj szkolę' : 'Zapisz zmiany'}
                </button>
            </div>

        </form>
    );
}

export default SchoolForm;