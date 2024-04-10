import Note from "./Note.tsx";
import {NoteModel} from "../../models/NoteModel.ts";

interface NotesBlockProps{
    notes: NoteModel[];
}

function NotesBlock(props: NotesBlockProps) {


    return (
        <div className='flex flex-col gap-5'>
            {props.notes.map((note)=><Note key={note.id} note={note}/>)}
        </div>
    );
}

export default NotesBlock;