import {ChildModelMaximized} from "../../models/ChildModelMaximized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import ChildInfoContainer from "./ChildInfoContainer.tsx";
import {Link} from "react-router-dom";
import useSWR from "swr";
import {BASE_API_URL} from "../../api/contst.ts";

interface ChildCardProps {
    childId: string;
}


function ChildCardMaximized(props: ChildCardProps) {
    const fetcher: (url: string) => Promise<ChildModelMaximized> = async (url) => {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        const jsonData = await response.json();
        document.title = jsonData.first_name + ' ' + jsonData.surname;
        return jsonData;
    };
    const { data, error, isLoading} = useSWR<ChildModelMaximized>(BASE_API_URL + `/children/${parseInt(props.childId)}`, fetcher);

    const child: ChildModelMaximized = data;



    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return (
        <div className=''>
            <WidthWrapper>
                <div
                    className='flex flex-col lg:flex-row gap-4 border-main_red border-4 p-4 rounded-2xl justify-center'>
                    <div className='flex md:block justify-center'>
                        <img className='pb-2 w-56 sm:w-72 lg:w-80 rounded-2xl'
                             src={child.photo_path ? child.photo_path : 'profilowe.png'}
                             alt='profilePhoto'/>
                    </div>
                    <div className='flex flex-col mt-4 gap-7'>
                        <div className='flex flex-row gap-1.5 mb-5'>
                            <span className='text-2xl font-bold'>{child.first_name}</span>
                            {child.second_name && <span className='text-2xl font-bold'>{child.second_name}</span>}
                            <span className='text-2xl font-bold'>{child.surname}</span>
                        </div>
                        {/*<div>*/}

                        {/*</div>*/}
                        <div className='flex flex-col gap-7 sm:grid xl:gap-4 sm:grid-cols-2 xl:grid-cols-3'>
                            <ChildInfoContainer note='Płeć' text={child.gender === 'Female' ? 'Kobieta' : 'Mężczyzna'}/>
                            <ChildInfoContainer note='Data urodzenia' text={child.birth_date }/>
                            <ChildInfoContainer note='Miejsce urodzeina' text={child.birthplace}/>
                        </div>
                        <div className='flex flex-col gap-7'>
                            <ChildInfoContainer note='Adres zamieszkania' text={child.residential_address}/>
                            <ChildInfoContainer note='Adres zamieldowania' text={child.registered_address}/>
                        </div>
                        <div className='flex flex-col sm:flex-row gap-7'>
                            <ChildInfoContainer note='Data przyjęcia' text={child.admission_date}/>
                            {child.leaving_date && <ChildInfoContainer note='Data opuszczenia' text={child.leaving_date}/>}
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