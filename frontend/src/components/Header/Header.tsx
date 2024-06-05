import Logo from "./Logo.tsx";
import ProfileBlock from "./ProfileBlock.tsx";
import NavBar from "./NavBar/NavBar.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";


function Header() {
    return (<>
            <header className='bg-main_white bg-opacity-80 py-2'>
                <WidthWrapper>
                    <div className='flex justify-between'>
                        <Logo/>
                        <ProfileBlock/>
                    </div>

                </WidthWrapper>
            </header>
            <NavBar/>
        </>

    );
}

export default Header;