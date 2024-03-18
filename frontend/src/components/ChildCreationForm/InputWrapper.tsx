import React, {FormEventHandler, useState} from 'react';
import LabelForInput from "./LabelForInput.tsx";

type props = {
    children: React.ReactNode;
    labelFor: string;
    labelNote: string;
}
const InputWrapper = ({children, labelFor, labelNote}: props) => {
    const [inputValue, setInputValue] = useState('');

    const handleChange = (event) => {
        setInputValue(event.target.value.trim()); // Update input value state
    };
    return (
        <div className={`flex flex-col mx-5 my-3 relative mb-3 mt-6`} onChange={handleChange}>
            <LabelForInput labelFor={labelFor} labelNote={labelNote} isDirty={!!inputValue}/>
            {children}
        </div>
    );
};

export default InputWrapper;