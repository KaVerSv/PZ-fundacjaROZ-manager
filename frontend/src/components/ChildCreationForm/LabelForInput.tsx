interface LabelProps {
    labelFor: string;
    labelNote: string;
    isDirty: boolean;
}
function LabelForInput(props: LabelProps) {
    return (
        <label className={`absolute bottom-6 left-0 transition-transform duration-300 text-sm ${
            props.isDirty ? 'transform -translate-y-1 opacity-100' : 'transform opacity-0 translate-y-full'
        }`} htmlFor={props.labelFor}>{props.labelNote}:</label>
    );
}

export default LabelForInput;