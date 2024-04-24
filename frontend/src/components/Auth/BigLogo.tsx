import {Link} from "react-router-dom";

function BigLogo() {
    return (
        <div className='flex h-full items-center'>
            <Link to={'/'}>
                <div className='flex flex-col items-center'>
                    <img className='w-24 h-auto lg:w-64' style={{paddingBottom: '4px'}} src='logo.png' alt="Logo"/>
                    <span className='font-oswald uppercase text-3xl text-main_red hidden sm:flex items-end'> rozwój opieka zaufanie</span>
                </div>
            </Link>
        </div>
    );
}

export default BigLogo;