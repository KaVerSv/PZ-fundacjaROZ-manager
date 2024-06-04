import NavItem from "./NavItem.tsx";
import WidthWrapper from "../../wrappers/WidthWrapper.tsx";
import {NavLink} from "react-router-dom";

function NavBar() {
    return (
        <div className='bg-main_red'>
            <WidthWrapper>
                <nav className='flex gap-4'>
                    <NavLink to={'/'}><NavItem navText="Strona główna"></NavItem></NavLink>
                    <NavItem navText="Jakaś strona"></NavItem>
                    <NavItem navText="Strony nie ma"></NavItem>
                </nav>

            </WidthWrapper>

        </div>
    );
}

export default NavBar;