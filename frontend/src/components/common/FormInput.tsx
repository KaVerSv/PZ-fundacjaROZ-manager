import {FieldError, RegisterOptions, UseFormRegister} from "react-hook-form";
import InputWrapper from "../ChildCreationForm/InputWrapper.tsx";
import useAutosizeTextArea from "../../hooks/AutoSizeTextArea.ts";
import {useRef, useState} from "react";

interface FormProps {
    name: string;
    type: string;
    label: string;
    labelColor?: string;
    placeholder?: string;
    error?: FieldError;
    register: UseFormRegister<any>;
    rules?: RegisterOptions;
    defaultValue?: string;
}

function FormInput({name, type, label, labelColor, placeholder, register, rules, error, defaultValue}: FormProps) {
    if (!placeholder) placeholder = label;
    let alwaysShowLabels: boolean = false;
    if (type === "date") alwaysShowLabels = true;

    const textAreaRef = useRef<HTMLTextAreaElement>(null);
    const[value, setValue] = useState('');
    useAutosizeTextArea(textAreaRef.current, value);

    const handleChange = (evt: React.ChangeEvent<HTMLTextAreaElement>) => {
        const val = evt.target?.value;

        setValue(val);
    };
    return (
        <InputWrapper labelFor={name} labelNote={label} error={error} alwaysShowLabel={alwaysShowLabels}
                      labelColor={labelColor}>
            {
                type === "textarea" ?
                    <textarea
                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                        id={name}
                        placeholder={placeholder}
                        {...register(name, rules)}
                        onChange={handleChange}
                        ref={textAreaRef}
                        rows={1}
                        value={value}/>
                    :
                    <input
                        className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                        type={type} id={name}
                        placeholder={placeholder}
                        {...register(name, rules)} />
            }
        </InputWrapper>

    );
}

export default FormInput;