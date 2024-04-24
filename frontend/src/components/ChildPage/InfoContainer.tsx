interface InfoProps {
    note: string;
    text: string;
}

function InfoContainer(props: InfoProps) {
    return (
        <div className='flex flex-col relative min-w-56 sm:min-w-56 md:min-w-72'>
            {props.note && <span className={`tracking-wide text-gray-700 absolute font-bold mb-2 bottom-10 left-1 text-sm`}>
                {props.note}:</span>}
            <span className="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight">{props.text}</span>
        </div>
    );
}

export default InfoContainer;