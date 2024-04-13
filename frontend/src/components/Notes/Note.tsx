import {NoteModel} from "../../models/NoteModel.ts";
import {faPencil, faReplyAll, faTrashCan} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {BASE_API_URL} from "../../api/contst.ts";
import {useState} from "react";
import NoteForm from "./NoteForm.tsx";
import {Mode} from "./Mode.ts";

interface NoteProps {
    note: NoteModel;
    toggleReload: () => void;
}

function Note(props: NoteProps) {
    const [editMode, setEditMode] = useState(false);
    const handleDeleteChild = async () => {
        try {
            const response = await fetch(`${BASE_API_URL}/children/${props.note.child_id}/notes/${props.note.id}/`, {
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
        <div className={`bg-orange-500 bg-opacity-60 ${!editMode?'p-3': 'pt-3' } rounded-xl`}>
            <div className='flex justify-between relative' style={editMode ? {flexDirection: "column"} : {flexDirection: "row"}}>
                {!editMode && <span className='font-bold w-[80%]'>{props.note.title}</span>}
                {!editMode ?
                    <div className='flex gap-2 justify-end'>
                        <div className='text-main_red hover:text-red-500 cursor-pointer'
                             onClick={() => setEditMode(!editMode)}>
                            <FontAwesomeIcon icon={faPencil}/>
                        </div>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={handleDeleteChild}>
                            <FontAwesomeIcon icon={faTrashCan}/>
                        </div>
                    </div>
                    :
                    <div className='flex gap-2 justify-end p-3 absolute -top-4 w-full'>
                        <span className='font-bold w-[80%]'>Edytuj notatkę</span>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={() => setEditMode(false)}>
                            <FontAwesomeIcon icon={faReplyAll}/>
                        </div>
                    </div>
                }
                {editMode && <>
                <NoteForm toggleReload={props.toggleReload}
                              toggleShowForm={() => {
                                  setEditMode(false)
                              }}
                              mode={Mode.edit}
                              childId={props.note.child_id}
                              note={props.note}
                    />
                </>

                }
            </div>
            {!editMode && <div>
                <p>
                    {props.note.contents}
                </p>
            </div>}
        </div>
    );
}

export default Note;