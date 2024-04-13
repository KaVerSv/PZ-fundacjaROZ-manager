import {faPencil, faReplyAll, faTrashCan} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useState} from "react";
import InfoContainer from "../InfoContainer.tsx";
import RelativeForm from "./RelativeForm.tsx";
import {Mode} from "../Mode.ts";
import {RelativeModel} from "../../../models/RelativeModel.ts";

interface NoteProps {
    relative: RelativeModel;
    child_id: string;
    toggleReload: () => void;
}

function Relative(props: NoteProps) {
    const [editMode, setEditMode] = useState(false);
    const handleDeleteChild = async () => {
        try {
            const response = await fetch(`${BASE_API_URL}/children/${props.child_id}/relatives/${props.relative.id}/`, {
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
                {!editMode && <span className='font-bold w-[89%]'>{props.relative.first_name} {props.relative.second_name} {props.relative.surname}</span>}
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
                        <span className='font-bold w-[89%]'>Edytuj rodzica</span>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={() => setEditMode(false)}>
                            <FontAwesomeIcon icon={faReplyAll}/>
                        </div>
                    </div>
                }
                {editMode && <>
                <RelativeForm toggleReload={props.toggleReload}
                              toggleShowForm={() => {
                                  setEditMode(false)
                              }}
                              mode={Mode.edit}
                              childId={props.child_id}
                             relative={props.relative}
                    />
                </>

                }
            </div>
            {!editMode && <div className='flex flex-col gap-6 relative mt-6'>
                <InfoContainer note={'Email'} text={props.relative.e_mail}/>
                <InfoContainer note={'Adres zamieszkania'} text={props.relative.residential_address}/>
                <InfoContainer note={'Telefon'} text={props.relative.phone_number}/>

            </div>}
        </div>
    );
}

export default Relative;