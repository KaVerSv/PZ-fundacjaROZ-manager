import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import useSWR from "swr";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useState} from "react";
import SchoolForm from "./SchoolForm.tsx";
import School from "./School.tsx";
import {Mode} from "../Mode.ts";
import {SchoolModel} from "../../../models/ShoolModel.ts";
import {faSchool} from "@fortawesome/free-solid-svg-icons";

interface NotesBlockProps {
    childId: string
}


function SchoolsSection(props: NotesBlockProps) {

    const [showSchoolsFrom, setShowSchoolsFrom] = useState(false);
    const [isHovered, setIsHovered] = useState(false);

    const handleMouseEnter = () => {
        setIsHovered(true);
    };

    const handleMouseLeave = () => {
        setIsHovered(false);
    };

    const [isWrapped, setIsWrapped] = useState(true);
    const fetcher: (url: string) => Promise<SchoolModel[]> = async (url) => {

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
    } = useSWR<SchoolModel[]>(`${BASE_API_URL}children/${props.childId}/schools/`, fetcher, {refreshInterval: 0});

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return (
        <div
            className='flex flex-col gap-1.5 w-[90%] sm:w-96 border-main_red border-4 rounded-2xl m-2 p-3'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold text-lg'>Szkoły</span>
                <div className='text-main_red hover:text-red-600 cursor-pointer relative'
                     onMouseOver={handleMouseEnter}
                     onMouseLeave={handleMouseLeave}
                     onClick={() => {
                         setShowSchoolsFrom(!showSchoolsFrom)
                     }}>
                    <FontAwesomeIcon icon={faSchool}/>
                    <svg id="subElement"
                         className={`absolute size-3 ${isHovered? 'fill-red-600':'fill-main_red'} top-2.5 left-3.5 bg-main_white border border-solid rounded-full`}
                         viewBox="-5.5768 8.267 512.7639 512" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M 250.805 520.267 C 447.874 520.267 571.042 306.934 472.508 136.267 C 426.778 57.061 342.265 8.267 250.805 8.267 C 53.736 8.267 -69.432 221.601 29.103 392.267 C 74.833 471.474 159.345 520.267 250.805 520.267 Z M 226.805 402.267 L 226.805 288.267 L 112.805 288.267 C 99.505 288.267 88.805 277.567 88.805 264.267 C 88.805 250.967 99.505 240.267 112.805 240.267 L 226.805 240.267 L 226.805 126.267 C 226.805 112.967 237.505 102.267 250.805 102.267 C 264.105 102.267 274.805 112.967 274.805 126.267 L 274.805 240.267 L 388.805 240.267 C 402.105 240.267 412.805 250.967 412.805 264.267 C 412.805 277.567 402.105 288.267 388.805 288.267 L 274.805 288.267 L 274.805 402.267 C 274.805 415.567 264.105 426.267 250.805 426.267 C 237.505 426.267 226.805 415.567 226.805 402.267 Z"/>
                    </svg>
                </div>
            </div>
            <div className='w-full flex justify-center'>
                <div className='w-[80%] border-[1px] border-red-700 rounded-[100%]'></div>
            </div>
            {showSchoolsFrom && <div>
                <SchoolForm toggleReload={() => {
                    mutate()
                }}
                            toggleShowForm={() => {
                                setShowSchoolsFrom(false);
                            }} mode={Mode.create} childId={props.childId}/>
            </div>}

            {data.length !== 0 ?
                <div className='flex flex-col gap-5'>
                    <button
                        className="bg-blue-500 text-white font-semibold py-2 px-4 rounded"
                        onClick={() => setIsWrapped(!isWrapped)}
                    > {isWrapped ? 'Rozwiń szkoły' : 'Zwiń szkoły'}
                    </button>
                    <div className={`flex flex-col gap-5 overflow-hidden ${
                        isWrapped ? 'max-h-0 absolute' : 'max-h-full'
                    }`}>
                        {data
                            .sort((a, b) => {
                                if (a.end_date) return 1;
                                return a.name.localeCompare(b.name)
                            })
                            .map((school) => <School toggleReload={mutate} child_id={props.childId}
                                                     key={school.id} school={school}/>)}
                    </div>
                </div>
                :
                <span className='mx-auto'>Póki co nie dodano żadnej szkoły</span>}
        </div>
    );
}

export default SchoolsSection;