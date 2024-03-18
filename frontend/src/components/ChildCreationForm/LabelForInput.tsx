import React from 'react';
interface LabelProps {
    labelFor: string;
    labelNote: string;
}
function LabelForInput(props: LabelProps) {
    return (
        <label htmlFor={props.labelFor}>{props.labelNote}:</label>
    );
}

export default LabelForInput;