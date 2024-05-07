import {SubmitHandler, useForm} from "react-hook-form";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useEffect, useState} from "react";
import FormInput from "../../common/FormInput.tsx";
import {Mode} from "../Mode.ts";
import {RelativeModel} from "../../../models/RelativeModel.ts";
import InputWrapper from "../../ChildCreationForm/InputWrapper.tsx";
import {DocumentModel} from "../../../models/DocumentModel.ts";
import useSWR from "swr";

interface Props {
    toggleReload: () => void;
    toggleShowForm: () => void;
    mode: Mode;
    childId: string | number;
    document?: DocumentModel;
}


function DocumentForm(props: Props) {
    const [loading, setLoading] = useState(false);
    const [errorStatus, setErrorStatus] = useState(false);
    const [isChecked, setIsChecked] = useState(false);

    const handleChange = () => {
        setIsChecked(!isChecked);
        setValue('relative_id', undefined);
    };
    const fetcher: (url: string) => Promise<RelativeModel[]> = async (url) => {

        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem("token")}`,
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    };
    const {
        data,
    } = useSWR<RelativeModel[]>(`${BASE_API_URL}children/${props.childId}/relatives/`, fetcher, {refreshInterval: 0});
    const date = new Date().toISOString();
    const {
        register,
        handleSubmit,
        formState: {errors, isValid},
        setFocus,
        setValue,
        getValues
    } = useForm<DocumentModel>({
        mode: "onChange",
        defaultValues: {
            id: props.document?.id,
            signature: props.document?.signature,
            specification: props.document?.specification,
            date: props.document?.date ? props.document.date : date.substring(0, date.indexOf('T')),
            child_id: props.childId,
            relative_id: props.document?.relative_id,
            file: props.document?.file
        }
    },);

    useEffect(() => {
        setFocus('signature');
    }, []);

    const onSubmit: SubmitHandler<DocumentModel> = async (documentFormData) => {
        try {
            const formData = new FormData();
            formData.append('file', documentFormData.file);
            formData.append('date', documentFormData.date);
            formData.append('signature', documentFormData.signature);
            formData.append('specification', documentFormData.specification);
            formData.append('child_id', documentFormData.child_id.toString());
            if (documentFormData.relative_id) formData.append('relative_id', documentFormData.relative_id.toString());

            console.log(formData)
            const response = await fetch(`${BASE_API_URL}${props.mode === Mode.edit ? `documents/${props.document.id}/` : `documents/`}`, {
                method: props.mode === Mode.edit ? 'PUT' : 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`
                },
                body: formData,
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
            setErrorStatus(true);
        } finally {
            setLoading(false);
        }
    }

    const handleUploadedFile = (event) => {
        const file = event.target.files[0];

        setValue('file', file);
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}
              className={`${props.mode === Mode.create ? 'bg-amber-500' : ''} w-auto bg-opacity-30 rounded-2xl py-1 flex flex-col pt-2`}>
            <FormInput name={"signature"} type={"text"} label={"Sygnatura"}
                       register={register}
                       error={errors.signature}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <FormInput name={"specification"} type={"text"} label={"Specyfikacja"}
                       register={register}
                       error={errors.specification}
                       rules={{
                           required: 'Pole wymagane'
                       }}/>
            <label className="block mx-auto">

                <input type="file" onChange={handleUploadedFile} className="block w-full text-sm text-slate-500
      file:mr-4 file:py-2 file:px-4
      file:rounded-full file:border-0
      file:text-sm file:font-semibold
      file:bg-violet-50 file:text-blue-500
      hover:file:bg-violet-100
    "/>
            </label>
            <label className="ml-5">
                <input type="checkbox" className="accent-main_red" checked={isChecked}
                       onChange={handleChange}/> Dokument jest powiązany z rodzicem
            </label>
            {isChecked &&
                <InputWrapper labelFor="relative_id" labelNote="Rodzic" alwaysShowLabel={true} error={errors.relative_id}>
                    <select
                        className="appearance-none block min-w-40 w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                        id="alive" {...register('relative_id', {
                        required: isChecked,
                    })}>
                        <option selected={true} disabled={true}>Wybierz rodzica</option>
                        {data
                            .map((relative) => <option key={relative.id}
                                                       value={relative.id}>{relative.first_name} {relative.surname}</option>)}
                    </select>
                    <div
                        className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                        <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg"
                             viewBox="0 0 20 20">
                            <path
                                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                        </svg>
                    </div>
                </InputWrapper>}

            <div className='w-full text-right'>
                {errorStatus && <div className='flex justify-center'>
                    <span className='text-sm text-red-800'>Coś poszło nie tak.<br/>Sprobuj ponownie</span>
                </div>}
                <button
                    className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey mr-2 mb-1"
                    type="button"
                    onClick={props.toggleShowForm}>
                    Odrzuć zmiany
                </button>
                <button
                    disabled={!isValid || loading || !getValues('file')}
                    className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-3 mx-auto rounded focus:outline-none focus:shadow-outline disabled:bg-main_grey mr-2 mb-1"
                    type="submit">
                    {props.mode === Mode.create ? 'Dodaj rodzica' : 'Zapisz zmiany'}
                </button>
            </div>

        </form>
    );
}

export default DocumentForm;