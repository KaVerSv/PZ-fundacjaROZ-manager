import React from 'react';
import LabelForInput from "./LabelForInput.tsx";

type props = {
    children: React.ReactNode;
    labelFor: string;
    labelNote: string;
}
const InputWrapper = ({children, labelFor, labelNote} : props) => {
    return (
        <div className='flex flex-col mx-5 my-3'>
            <LabelForInput labelFor={labelFor} labelNote={labelNote}/>
            {children}
        </div>
    );
};

export default InputWrapper;