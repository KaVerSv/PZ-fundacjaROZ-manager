import {ChildModelMaximized} from "../../models/ChildModelMaximized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import InfoContainer from "./InfoContainer.tsx";
import {Link, useNavigate} from "react-router-dom";
import useSWR from "swr";
import {BASE_API_URL} from "../../api/contst.ts";
import fetchImage from "../../api/fetchImage.ts";

interface ChildCardProps {
    childId: string;
}


function ChildCardMaximized(props: ChildCardProps) {
    const navigate = useNavigate();
    const fetcher: (url: string) => Promise<ChildModelMaximized> = async (url) => {
        const response = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem("token")}`
            }
        });
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        const jsonData = await response.json();
        document.title = jsonData.first_name + ' ' + jsonData.surname;
        return jsonData;
    };
    const {
        data,
        error,
        isLoading
    } = useSWR<ChildModelMaximized>(BASE_API_URL + `/children/${parseInt(props.childId)}`, fetcher);
    const {data: image} = useSWR<string>(`${BASE_API_URL}/children/${parseInt(props.childId)}/photo`, fetchImage);
    const child: ChildModelMaximized = data;

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    const handleDeleteChild = async () => {
        try {
            const response = await fetch(BASE_API_URL + `/children/${parseInt(props.childId)}/`,{
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem("token")}`
            }
        })
            if (response.ok) {
                navigate('/');
            } else {
                console.error('Failed to delete:', response.statusText);
            }
        } catch (error) {
            console.error('Error deleting:', error);
        }
    }
    return (
        <div className=''>
            <WidthWrapper>
                <div className='flex flex-col gap-4 justify-center border-main_red border-4 p-4 rounded-2xl'>
                    <div className='flex flex-col lg:flex-row gap-4  justify-center'>
                        <div className='flex md:block justify-center'>
                            <img className='pb-2 w-56 sm:w-72 lg:w-80 rounded-2xl'
                                 src={image}
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
                            <div
                                className='flex flex-col gap-7 sm:grid sm:grid-cols-1 xl:gap-4 xl:gap-y-7 xl:grid-cols-2 2xl:grid-cols-3'>
                                <InfoContainer note='Płeć'
                                               text={child.gender === 'female' ? 'Kobieta' : 'Mężczyzna'}/>
                                <InfoContainer note='Data urodzenia' text={child.birth_date}/>
                                <InfoContainer note='Miejsce urodzeina' text={child.birthplace}/>
                            </div>
                            <div className='flex flex-col gap-7'>
                                <InfoContainer note='Adres zamieszkania' text={child.residential_address}/>
                                <InfoContainer note='Adres zamieldowania' text={child.registered_address}/>
                            </div>
                            <div className='flex flex-col sm:flex-row gap-7'>
                                <InfoContainer note='Data przyjęcia' text={child.admission_date}/>
                                {child.leaving_date &&
                                    <InfoContainer note='Data opuszczenia' text={child.leaving_date}/>}
                            </div>
                        </div>
                    </div>
                    <div className='flex justify-center flex-col sm:flex-row gap-2 sm:gap-16 items-center'>
                        <Link to={`/children-edit/${child.id}`}>
                            <button
                                className='mt-3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded w-28'
                                type="submit">
                                Edutuj
                            </button>
                        </Link>

                        <button
                            className='mt-3 bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 border border-blue-700 rounded w-28'
                            type="button"
                            onClick={handleDeleteChild}>
                            Usuń
                        </button>
                    </div>
                </div>
            </WidthWrapper>
        </div>
    );
}

export default ChildCardMaximized;