import {FieldError, RegisterOptions, UseFormRegister} from "react-hook-form";
import InputWrapper from "../ChildCreationForm/InputWrapper.tsx";

interface FormProps {
    name: string;
    type: string;
    label: string;
    labelColor?: string;
    placeholder?: string;
    error?: FieldError;
    register: UseFormRegister<any>;
    rules?: RegisterOptions;
}

function FormInput({name, type, label, labelColor, placeholder, register, rules, error}: FormProps) {
    if (!placeholder) placeholder = label;
    let alwaysShowLabels: boolean = false;
    if (type === "date") alwaysShowLabels = true;
        return (
            <InputWrapper labelFor={name} labelNote={label} error={error} alwaysShowLabel={alwaysShowLabels} labelColor={labelColor}>
                <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    type={type} id={name}
                    placeholder={placeholder}
                    {...register(name, rules)} />
            </InputWrapper>

        );
}

export default FormInput;