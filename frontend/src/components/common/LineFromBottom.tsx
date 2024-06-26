interface LineParams {
    isHovered: boolean;
    additionalStyles?: string;
}

function LineFromBottom(props: LineParams) {
    return (
        <div
            className={`absolute w-full bg-main_white h-1 left-0.5 transition-transform duration-500 ${props.additionalStyles} transform ${props.isHovered ? 'translate-y-[-10px]' : ''} `}></div>

    );
}

export default LineFromBottom;