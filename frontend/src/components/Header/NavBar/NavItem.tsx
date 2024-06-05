import LineFromBottom from "../../common/LineFromBottom.tsx";
import {useState} from "react";

interface NavProps{
    navText: string
}
function NavItem(props: NavProps) {
    const [isHowered, setIsHowered] = useState(false)
    return (
        <div className='relative cursor-pointer' onMouseEnter={() => setIsHowered(true)} onMouseLeave={() => setIsHowered(false)}>
            <span className='text-main_white font-roboto text-sm lg:text-lg'>{props.navText}</span>
            <LineFromBottom isHovered={isHowered} additionalStyles='top-8'/>
        </div>
    );
}

export default NavItem;