import React from 'react';
import logo from './assets/logo.png';
function Logo() {
    return (
        <div className='flex'>
            <img className='min-w-2 h-auto pb-1.5' src={logo} alt="Logo"/>
            <span className='flex font-oswald uppercase items-end pb-0.5 text-xs'> rozwój opieka zaufanie</span>
        </div>

    );
}

export default Logo;
