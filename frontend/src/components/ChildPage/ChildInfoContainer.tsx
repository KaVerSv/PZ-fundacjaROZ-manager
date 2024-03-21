interface InfoProps {
    note: string;
    text: string;
}

function ChildInfoContainer(props: InfoProps) {
    return (
        <div className='flex flex-row gap-2 items-end'>
            {props.note && <span className='text-main_white text-md'>{props.note}:</span>}
            <span className='text-main_white text-lg'>{props.text}</span>
        </div>
    );
}

export default ChildInfoContainer;