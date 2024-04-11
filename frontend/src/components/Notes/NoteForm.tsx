import {SubmitHandler, useForm} from "react-hook-form";
import {BASE_API_URL} from "../../api/contst.ts";
import {useEffect, useState} from "react";
import FormInput from "../common/FormInput.tsx";
import {NoteModel} from "../../models/NoteModel.ts";
import {Mode} from "./Mode.ts";

interface Props {
    toggleReload: () => void;
    toggleShowForm: () => void;
    mode: Mode;
    childId: string;
    note?: NoteModel;
}


interface NoteFormData {
    id?: string;
    child_id: string;
    title: string;
    contents: string;
}

function NoteForm(props: Props) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    const {
        register,
        handleSubmit,
        formState: {errors, isValid},
        setFocus,
        getValues
    } = useForm<NoteFormData>({
        mode: "onChange",
        defaultValues: {
            child_id: props.childId,
            id: props.note?.id,
            title: props.note?.title,
            contents: props.note?.contents
        }
    },);

    useEffect(() => {
        setFocus('title');
    }, []);

    const onSubmit: SubmitHandler<NoteFormData> = async (noteFormData) => {
        setLoading(true);
        try {
            const response = await fetch(`${BASE_API_URL}/children/${props.childId}/notes/${props.note ? props.note.id + '/' : ''}`, {
                method: props.mode === Mode.edit ? 'PUT' : 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(noteFormData),
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
              className={`${props.mode === Mode.create ? 'bg-amber-500' : ''} w-full bg-opacity-30 rounded-2xl py-1`}>
            {JSON.stringify(props.childId)}
            <FormInput name={"title"} type={"text"} label={"Tytuł"}
                       register={register}
                       error={errors.title}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"contents"} type={"textarea"} label={'Treść'}
                       register={register}
                       error={errors.contents}
                       defaultValue={getValues('contents')}
                       rules={{
                           required: 'Pole wymagane',
                       }}/>
            <div className='w-full text-right'>
                {error && <div className='flex justify-center'>
                    <span className='text-sm text-red-800'>Coś poszło nie tak.<br/>Sprobuj ponownie</span>
                </div>}
                <button
                    disabled={!isValid || loading}
                    className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey mr-2 mb-1"
                    type="submit">
                    {props.mode === Mode.create ? 'Dodaj notatkę' : 'Zapisz zmiany'}
                </button>
            </div>

        </form>
    );
}

export default NoteForm;