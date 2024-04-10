import {FieldError, RegisterOptions, UseFormRegister} from "react-hook-form";
import InputWrapper from "../ChildCreationForm/InputWrapper.tsx";


interface FormProps {
    name: string;
    type: string;
    label: string;
    placeholder?: string;
    error?: FieldError;
    register: UseFormRegister<any>;
    rules?: RegisterOptions;
}

function FormInput(props: FormProps) {
    if (!props.placeholder) props.placeholder = props.label;
    let alwaysShowLabels: boolean = false;
    if (props.type === "date") alwaysShowLabels = true;
    return (
        <InputWrapper labelFor={props.name} labelNote={props.label} error={props.error}
                      alwaysShowLabel={alwaysShowLabels}>
            {props.type === "textarea" ?
                <textarea
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    id={props.name}
                    placeholder={props.placeholder}
                    {...props.register(props.name, props.rules)} />

                :
                <input
                    className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                    type={props.type} id={props.name}
                    placeholder={props.placeholder}
                    {...props.register(props.name, props.rules)} />
            }
        </InputWrapper>

    );
}

export default FormInput;