import React from 'react';
import Logo from "./Logo.tsx";
import ProfileBlock from "./ProfileBlock.tsx";
import NavBar from "./NavBar/NavBar.tsx";


function Header () {
    return (
        <header>
            <div className='flex justify-between'>
                <Logo />
                <ProfileBlock />
            </div>
            <NavBar />
        </header>
    );
};

export default Header;