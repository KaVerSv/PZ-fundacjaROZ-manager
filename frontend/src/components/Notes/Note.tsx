import {NoteModel} from "../../models/NoteModel.ts";
import {faPencil, faTrashCan} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {BASE_API_URL} from "../../api/contst.ts";

interface NoteProps {
    note?: NoteModel;
    toggleReload: () => void;
}

function Note(props: NoteProps) {
    const handleDeleteChild = async () => {
        try {
            const response = await fetch(`${BASE_API_URL}/children/${props.note.child_id}/notes/${props.note.id}/`,{
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem("token")}`
                }
            })
            if (!response.ok) console.error('Failed to delete:', response.statusText);
            else {
                props.toggleReload();
            }
        } catch (error) {
            console.error('Error deleting:', error);
        }
    }

    return (
        <div className='bg-orange-500 bg-opacity-60 p-3 rounded-xl'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold w-[80%]'>{props.note.title}</span>
                <div className='flex gap-2'>
                    <div className='text-main_red hover:text-red-500 cursor-pointer'>
                        <FontAwesomeIcon icon={faPencil} />
                    </div>
                    <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                         onClick={handleDeleteChild}>
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