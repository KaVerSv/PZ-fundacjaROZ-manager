import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFileCirclePlus} from "@fortawesome/free-solid-svg-icons";
import {NoteModel} from "../../models/NoteModel.ts";
import useSWR from "swr";
import {BASE_API_URL} from "../../api/contst.ts";
import {useState} from "react";
import NoteForm, {Mode} from "./NoteForm.tsx";
import Note from "./Note.tsx";

interface NotesBlockProps {
    childId: string
}


function NotesSection(props: NotesBlockProps) {

    const [showNoteForm, setShowNoteForm] = useState(false);

    const fetcher: (url: string) => Promise<NoteModel[]> = async (url) => {

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
    } = useSWR<NoteModel[]>(`${BASE_API_URL}children/${props.childId}/notes/`, fetcher, {refreshInterval: 0});

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return (
        <div
            className='flex flex-col gap-1.5 w-[90%] sm:w-72 border-main_red border-4 rounded-2xl m-2 p-3 sm:mb-auto'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold text-lg'>Notatki</span>
                <div className='text-main_red hover:text-red-600 cursor-pointer' onClick={() => {
                    setShowNoteForm(!showNoteForm)
                }}>
                    <FontAwesomeIcon icon={faFileCirclePlus}/>
                </div>
            </div>
            <div className='w-full flex justify-center'>
                <div className='w-[80%] border-[1px] border-red-700 rounded-[100%]'></div>
            </div>
            {showNoteForm && <div>
                <NoteForm toggleReload={() => {
                    mutate()
                }}
                          toggleShowForm={() => {
                              setShowNoteForm(false);
                          }} mode={Mode.create} childId={props.childId}/>
            </div>}

            {data.length !== 0 ?
                <div className='flex flex-col gap-5'>
                    {data.map((note) => <Note toggleReload={mutate} key={note.id} note={note}/>)}
                </div> :
                <span className='mx-auto'>Póki co nie ma notatek</span>}
        </div>
    );
}

export default NotesSection;