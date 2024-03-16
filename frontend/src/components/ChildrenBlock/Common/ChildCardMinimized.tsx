function ChildCardMinimized() {
    return (
        <a href='/' className='ml-10 flex max-w-72 h-16 bg-main_red rounded-xl hover:bg-red-selected hover:cursor-pointer'>
            <img className='ml-5 p-0.5 rounded-full' src='src/components/ChildrenBlock/2.jpg'/>
            <span className='flex items-center ml-2 text-main_white'>Jan Kowalski</span>
        </a>
    );
}

export default ChildCardMinimized;