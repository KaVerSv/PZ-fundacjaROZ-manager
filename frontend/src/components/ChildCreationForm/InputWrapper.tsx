import React, {useState} from 'react';
import LabelForInput from "./LabelForInput.tsx";
import {FieldError} from "react-hook-form";

type props = {
    children: React.ReactNode;
    labelFor: string;
    labelNote: string;
    shift?: number[];
    alwaysShowLabel?: boolean;
    error?: FieldError;
}
const InputWrapper = ({children, labelFor, labelNote, shift, alwaysShowLabel, error}: props) => {
    const [inputValue, setInputValue] = useState('');

    // @ts-ignore
    const handleChange = (event) => {
        setInputValue(event.target.value.trim()); // Update input value state
    };
    return (
        <div className={`flex flex-col ${alwaysShowLabel? 'min-w-56 sm:min-w-56 md:min-w-72':''} mx-5 my-3 relative mb-3 mt-6`} onChange={handleChange}>
            <LabelForInput labelFor={labelFor} labelNote={labelNote} isDirty={alwaysShowLabel || !!inputValue} shift={!!shift? shift : [0,0]}/>
            {children}
            {error && <div
                className={`text-red-600 absolute bottom-11 self-end`}>
                <span>{error.message}</span>
            </div>}
        </div>
    );
};

export default InputWrapper;