import {faPencil, faReplyAll, faTrashCan} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useState} from "react";
import InfoContainer from "../InfoContainer.tsx";
import SchoolForm from "./SchoolForm.tsx";
import {Mode} from "../Mode.ts";
import {SchoolModel} from "../../../models/ShoolModel.ts";

interface NoteProps {
    school: SchoolModel;
    child_id: string;
    toggleReload: () => void;
}

function School(props: NoteProps) {
    const [editMode, setEditMode] = useState(false);
    const handleDeleteSchool = async () => {
        try {
            const response = await fetch(`${BASE_API_URL}/children/${props.child_id}/schools/${props.school.id}/`, {
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
        <div className={`${!props.school.end_date? 'bg-orange-500' : 'bg-main_grey'} bg-opacity-60 ${!editMode?'p-3': 'pt-8' } rounded-xl`}>
            <div className='flex justify-between' style={editMode ? {flexDirection: "column"} : {flexDirection: "row"}}>
                {!editMode && <span className='font-bold w-[89%]'>{props.school.name}</span>}
                {!editMode ?
                    <div className='flex gap-2 justify-end'>
                        <div className='text-main_red hover:text-red-500 cursor-pointer'
                             onClick={() => setEditMode(!editMode)}>
                            <FontAwesomeIcon icon={faPencil}/>
                        </div>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={handleDeleteSchool}>
                            <FontAwesomeIcon icon={faTrashCan}/>
                        </div>
                    </div>
                    :
                    <div className='flex gap-2 justify-end p-3 absolute -top-7 w-full'>
                        <span className='font-bold w-[89%]'>Edytuj szkolę</span>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={() => setEditMode(false)}>
                            <FontAwesomeIcon icon={faReplyAll}/>
                        </div>
                    </div>
                }
                {editMode && <>
                <SchoolForm toggleReload={props.toggleReload}
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
            {!editMode && <div className='flex flex-col gap-6 mt-6'>
                <InfoContainer note={'Email'} text={props.school.e_mail}/>
                <InfoContainer note={'Adres szkoły'} text={props.school.address}/>
                <InfoContainer note={'Telefon'} text={props.school.phone_number}/>
                <InfoContainer note={'Rozpoczęto naukę'} text={props.school.start_date}/>
                {props.school.end_date && <InfoContainer note={'Ukończono naukę'} text={props.school.end_date}/>}
            </div>}
        </div>
    );
}

export default School;