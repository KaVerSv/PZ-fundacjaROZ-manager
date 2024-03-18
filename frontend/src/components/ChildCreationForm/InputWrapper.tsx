import React, {FormEventHandler, useState} from 'react';
import LabelForInput from "./LabelForInput.tsx";

type props = {
    children: React.ReactNode;
    labelFor: string;
    labelNote: string;
    shift?: number[];
    alwaysShowLabel?: boolean;
}
const InputWrapper = ({children, labelFor, labelNote, shift, alwaysShowLabel}: props) => {
    const [inputValue, setInputValue] = useState('');

    const handleChange = (event) => {
        setInputValue(event.target.value.trim()); // Update input value state
    };
    return (
        <div className={`flex flex-col mx-5 my-3 relative mb-3 mt-6`} onChange={handleChange}>
            <LabelForInput labelFor={labelFor} labelNote={labelNote} isDirty={alwaysShowLabel || !!inputValue} shift={!!shift? shift : [0,0]}/>
            {children}
        </div>
    );
};

export default InputWrapper;