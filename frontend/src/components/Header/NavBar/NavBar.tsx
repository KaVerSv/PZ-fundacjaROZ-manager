import NavItem from "./NavItem.tsx";
import WidthWrapper from "../../wrappers/WidthWrapper.tsx";

function NavBar() {
    return (
        <div className='bg-main_red'>
            <WidthWrapper>
                <nav className='flex gap-4'>
                    <NavItem></NavItem>
                    <NavItem></NavItem>
                    <NavItem></NavItem>
                </nav>

            </WidthWrapper>

        </div>
    );
}

export default NavBar;