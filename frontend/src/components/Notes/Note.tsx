import {NoteModel} from "../../models/NoteModel.ts";
import {faPencil, faTrashCan} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";

interface NoteProps {
    note?: NoteModel;
}

function Note(props: NoteProps) {
    return (
        <div className='bg-orange-500 bg-opacity-60 p-3 rounded-xl'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold w-[80%]'>{props.note.title}</span>
                <div className='flex gap-2'>
                    <div className='text-main_red hover:text-red-500 cursor-pointer'>
                        <FontAwesomeIcon icon={faPencil} />
                    </div>
                    <div className='text-main_grey hover:text-gray-900 cursor-pointer'>
                        <FontAwesomeIcon icon={faTrashCan} />
                    </div>

                </div>
            </div>
            <div>
                <p>
                    {props.note.contents}
                </p>
            </div>
        </div>
    );
}

export default Note;