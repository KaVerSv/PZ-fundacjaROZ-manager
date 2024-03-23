import logo from "../../../public/logo.png";
function BigLogo() {
    return (
        <div className='flex h-full items-center'>
            <div className='flex flex-col items-center'>
                <img className='w-24 h-auto lg:w-64' style={{paddingBottom: '4px'}} src={logo} alt="Logo"/>
                <span className='font-oswald uppercase text-3xl text-main_red hidden sm:flex items-end'> rozwój opieka zaufanie</span>
            </div>
        </div>
    );
}

export default BigLogo;