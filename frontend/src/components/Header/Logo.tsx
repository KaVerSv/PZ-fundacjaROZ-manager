import logo from './assets/logo.png';

function Logo() {
    return (
        <div className='flex'>
            <div className='absolute flex'>
                <img className= 'w-24 h-auto lg:w-40' style={{paddingBottom:'4px'}} src={logo} alt="Logo"/>
                <span className='font-oswald uppercase text-sm text-main_red hidden sm:flex lg:text-lg items-end'> rozwój opieka zaufanie</span>
            </div>
        </div>

    );
}

export default Logo;
