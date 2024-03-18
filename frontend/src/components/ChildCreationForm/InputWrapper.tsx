import React, {useState} from 'react';
import LabelForInput from "./LabelForInput.tsx";

type props = {
    children: React.ReactNode;
    labelFor: string;
    labelNote: string;
}
const InputWrapper = ({children, labelFor, labelNote} : props) => {
    const [isFocused, setIsFocused] = useState(false); // State to track input focus

    const handleFocus = () => {
        setIsFocused(true);
    };

    const handleBlur = () => {
        setIsFocused(false);
    };
    return (
        <div className={`flex flex-col mx-5 my-3 relative mb-3 mt-6 ${isFocused ? '' : ''}`} onFocus={handleFocus} onBlur={handleBlur}>
            <LabelForInput labelFor={labelFor} labelNote={labelNote} isFocused={isFocused}/>
            {children}
        </div>
    );
};

export default InputWrapper;