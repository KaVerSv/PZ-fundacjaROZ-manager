interface LabelProps {
    labelFor: string;
    labelNote: string;
    isDirty: boolean;
    shift: number[]
    labelColor?: string;
}
const defaults: Pick<LabelProps, 'labelColor'> = {
    labelColor: 'text-gray-700'
}


function LabelForInput(props: LabelProps) {
    props = {
        ...defaults,
        ...props
    }
    return (
        <label className={`tracking-wide ${props.labelColor} font-bold mb-2 absolute -top-5 left-3 transition-transform duration-300 text-sm ${
            props.isDirty ? 'transform -translate-y-1 opacity-100' : 'transform opacity-0 translate-y-full'
        }`} htmlFor={props.labelFor}>{props.labelNote}:</label>
    );
}

export default LabelForInput;