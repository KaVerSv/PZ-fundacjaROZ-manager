import WidthWrapper from "../../wrappers/WidthWrapper.tsx";
import {Link} from "react-router-dom";
import {useState} from "react";
import LineFromBottom from "../../common/LineFromBottom.tsx";

function CurrentBlockHeader() {
    const [isHovered, setIsHovered] = useState(false);
    return (
        <div className='flex bg-main_red mt-2'>
            <WidthWrapper>
                <div className='flex items-center justify-between'>
                    <span className='text-main_white'>Obecni wychowankowie</span>
                    <Link className='relative' to={'/addchild'}>
                        <div className='flex items-center gap-1'
                             onMouseEnter={() => setIsHovered(true)}
                             onMouseLeave={() => setIsHovered(false)}>
                            <span className= {`text-main_white text-4xl pb-1 ${isHovered ? 'rotate-90' : ''} transition-transform duration-300`}>+</span>
                            <span className='text-main_white'>Dodaj wychowanka</span>
                        </div>
                        <LineFromBottom isHovered={isHovered}/>
                    </Link>
                </div>
            </WidthWrapper>
        </div>
    );
}

export default CurrentBlockHeader;