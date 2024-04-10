import NotesBlock from "./NotesBlock.tsx";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFileCirclePlus} from "@fortawesome/free-solid-svg-icons";
import {NoteModel} from "../../models/NoteModel.ts";
import useSWR from "swr";
import {BASE_API_URL} from "../../api/contst.ts";

interface NotesBlockProps{
    childId: string
}
function NotesSection(props: NotesBlockProps) {
    const fetcher: (url: string) => Promise<NoteModel[]> = async (url) => {

        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    };

    const {data, error, isLoading} = useSWR<NoteModel[]>(`${BASE_API_URL}children/${props.childId}/notes/`, fetcher, {refreshInterval:0});

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return (
        <div className='flex flex-col gap-1.5 w-[90%] sm:max-w-72 border-main_red border-4 rounded-2xl m-3 p-3 sm:mb-auto'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold text-lg'>Notatki</span>
                <div className='text-main_red hover:text-red-600 cursor-pointer'>
                    <FontAwesomeIcon icon={faFileCirclePlus} />
                </div>
            </div>
            <div className='w-full flex justify-center'>
                <div className='w-[80%] border-[1px] border-red-700 rounded-[100%]'></div>
            </div>

            <NotesBlock notes={data}></NotesBlock>
        </div>
    );
}

export default NotesSection;