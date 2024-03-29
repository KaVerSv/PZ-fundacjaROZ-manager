import {ChildModelMaximized, currentChildrenFull} from "../../models/ChildModelMaximized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import ChildInfoContainer from "./ChildInfoContainer.tsx";
import {Link} from "react-router-dom";
import {useEffect} from "react";

interface ChildCardProps {
    childId: string;
}


function ChildCardMaximized(props: ChildCardProps) {

    const child: ChildModelMaximized = currentChildrenFull[parseInt(props.childId) - 1];
    useEffect(() => {
        document.title = child.firstName + ' ' + child.surname;
    }, []);

    return (
        <div className=''>
            <WidthWrapper>
                <div
                    className='flex flex-col lg:flex-row gap-4 border-main_red border-4 p-4 rounded-2xl justify-center'>
                    <div className='flex md:block justify-center'>
                        <img className='pb-2 w-56 sm:w-72 lg:w-80 rounded-2xl' src={child.photoPath}
                             alt='profilePhoto'/>
                    </div>
                    <div className='flex flex-col mt-4 gap-7'>
                        <div className='flex flex-row gap-1.5 mb-5'>
                            <span className='text-2xl font-bold'>{child.firstName}</span>
                            {child.secondName && <span className='text-2xl font-bold'>{child.secondName}</span>}
                            <span className='text-2xl font-bold'>{child.surname}</span>
                        </div>
                        {/*<div>*/}

                        {/*</div>*/}
                        <div className='flex flex-col gap-7 sm:grid xl:gap-4 sm:grid-cols-2 xl:grid-cols-3'>
                            <ChildInfoContainer note='Płeć' text={child.gender === "male" ? 'Mężczyzna' : 'Kobieta'}/>
                            <ChildInfoContainer note='Data urodzenia' text={child.birthDate}/>
                            <ChildInfoContainer note='Miejsce urodzeina' text={child.birthPlace}/>
                        </div>
                        <div className='flex flex-col gap-7'>
                            <ChildInfoContainer note='Adres zamieszkania' text={child.residentialAddress}/>
                            <ChildInfoContainer note='Adres zamieldowania' text={child.registeredAddress}/>
                        </div>
                        <div className='flex flex-col sm:flex-row gap-7'>
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