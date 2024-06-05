import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faUserPlus} from "@fortawesome/free-solid-svg-icons";
import useSWR from "swr";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useState} from "react";
import RelativeForm from "./RelativeForm.tsx";
import Relative from "./Relative.tsx";
import {Mode} from "../Mode.ts";
import {RelativeModel} from "../../../models/RelativeModel.ts";

interface NotesBlockProps {
    childId: string
}


function RelativesSection(props: NotesBlockProps) {

    const [showRelativesFrom, setShowRelativesFrom] = useState(false);
    const [isWrapped, setIsWrapped] = useState(true);
    const fetcher: (url: string) => Promise<RelativeModel[]> = async (url) => {

        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem("token")}`,
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    };
    const {
        data,
        error,
        isLoading,
        mutate
    } = useSWR<RelativeModel[]>(`${BASE_API_URL}children/${props.childId}/relatives/`, fetcher, {refreshInterval: 0});

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return (
        <div
            className='flex flex-col gap-1.5 w-[90%] sm:w-96 border-main_red border-4 rounded-2xl m-2 p-3 sm:mb-auto'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold text-lg'>Rodzice</span>
                <div className='text-main_red hover:text-red-600 cursor-pointer' onClick={() => {
                    setShowRelativesFrom(!showRelativesFrom)
                }}>
                    <FontAwesomeIcon icon={faUserPlus}/>
                </div>
            </div>
            <div className='w-full flex justify-center'>
                <div className='w-[80%] border-[1px] border-red-700 rounded-[100%]'></div>
            </div>
            {showRelativesFrom && <div>
                <RelativeForm toggleReload={() => {
                    mutate()
                }}
                              toggleShowForm={() => {
                                  setShowRelativesFrom(false);
                              }} mode={Mode.create} childId={props.childId}/>
            </div>}

            {data.length !== 0 ?
                <div className='flex flex-col gap-5'>
                    <button
                        className="bg-blue-500 text-white font-semibold py-2 px-4 rounded"
                        onClick={() => setIsWrapped(!isWrapped)}
                    > {isWrapped ? 'Rozwiń rodziców' : 'Zwiń rodziców'}
                    </button>
                    <div className={`flex flex-col gap-5 overflow-hidden ${
                        isWrapped ? 'max-h-0 absolute' : 'max-h-full'
                    }`}>
                        {data
                            .sort((a, b) => {
                                if(a.alive === false) return 1;
                                else return a.first_name.localeCompare(b.first_name)
                            })
                            .map((relative) => <Relative toggleReload={mutate} child_id={props.childId}
                                                         key={relative.id} relative={relative}/>)}
                    </div>
                </div>
                :
                <span className='mx-auto'>Póki co nie ma rodziców</span>}
        </div>
    );
}

export default RelativesSection;