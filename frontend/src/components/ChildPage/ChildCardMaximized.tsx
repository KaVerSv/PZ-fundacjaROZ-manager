import {ChildModelMaximized, currentChildrenFull} from "../../models/ChildModelMaximized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import ChildInfoContainer from "./ChildInfoContainer.tsx";
import {Link} from "react-router-dom";

interface ChildCardProps {
    childId: string;
}


function ChildCardMaximized(props: ChildCardProps) {

    const child: ChildModelMaximized = currentChildrenFull[parseInt(props.childId) - 1];


    return (
        <div className='bg-main_red'>
            <WidthWrapper>
                <div className='flex flex-col sm:flex-row justify-center'>
                    <div className='px-2 items-center'>
                        <img className='px-1 py-2 w-56 sm:w-64' src={child.photoPath} alt='profilePhoto'/>
                    </div>
                    <div className='flex flex-col '>
                        <div className='flex flex-row gap-2'>
                            <ChildInfoContainer note='' text={child.firstName}/>
                            {child.secondName && <ChildInfoContainer note='' text={child.secondName}/>}
                            <ChildInfoContainer note='' text={child.surname}/>
                        </div>
                        <div>
                            <ChildInfoContainer note='Płeć' text={child.gender === "male" ? 'Mężczyzna' : 'Kobieta'}/>
                        </div>
                        <div className='md:flex md:flex-row gap-4'>
                            <ChildInfoContainer note='Data urodzenia' text={child.birthDate}/>
                            <ChildInfoContainer note='Miejsce urodzeina' text={child.birthPlace}/>
                        </div>
                        <div>
                            <ChildInfoContainer note='Adres zamieszkania' text={child.residentialAddress}/>
                            <ChildInfoContainer note='Adres zamieldowania' text={child.registeredAddress}/>
                        </div>
                        <div className='md:flex md:flex-row gap-4'>
                            <ChildInfoContainer note='Data przyjęcia' text={child.admissionDate}/>
                            <ChildInfoContainer note='Data opuszczenia' text={child.leavingDate}/>
                        </div>
                    </div>
                </div>
                <div className='flex justify-center'>
                    <Link to={`/children-edit/${child.id}`}>
                        <button
                            className='mt-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded'
                            type="submit">
                            Edutuj
                        </button>
                    </Link>

                </div>
            </WidthWrapper>
        </div>
    );
}

export default ChildCardMaximized;