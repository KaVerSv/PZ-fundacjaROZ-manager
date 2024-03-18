interface LabelProps {
    labelFor: string;
    labelNote: string;
    isDirty: boolean;
    shift: number[]
}
function LabelForInput(props: LabelProps) {
    return (
        <label className={`tracking-wide text-gray-700 font-bold mb-2 absolute bottom-9 left-3 transition-transform duration-300 text-sm ${
            props.isDirty ? 'transform -translate-y-1 opacity-100' : 'transform opacity-0 translate-y-full'
        }`} htmlFor={props.labelFor}>{props.labelNote}:</label>
    );
}

export default LabelForInput;