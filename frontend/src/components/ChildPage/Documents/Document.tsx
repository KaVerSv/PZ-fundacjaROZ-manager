import {faPencil, faReplyAll, faTrashCan} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useState} from "react";
import InfoContainer from "../InfoContainer.tsx";
import DocumentForm from "./DocumentForm.tsx";
import {Mode} from "../Mode.ts";
import {DocumentModel} from "../../../models/DocumentModel.ts";
import {RelativeModel} from "../../../models/RelativeModel.ts";
import useSWR from "swr";

interface DocumentProps {
    document: DocumentModel;
    child_id: string;
    toggleReload: () => void;
}

function Document(props: DocumentProps) {
    const [editMode, setEditMode] = useState(false);
    const handleDeleteDocument = async () => {
        try {
            const response = await fetch(`${BASE_API_URL}/documents/${props.document.id}/`, {
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
    const fetcher: (url: string) => Promise<RelativeModel> = async (url) => {
        if (props.document.relative_id) {
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
        } else return null;
    };
    const {
        data
    } = useSWR<RelativeModel>(`${BASE_API_URL}relatives/${props.document.relative_id}`, fetcher, {refreshInterval: 0});


    return (
        <div className={`bg-orange-500 bg-opacity-60 ${!editMode ? 'p-3' : 'pt-8'} rounded-xl`}>
            <div className='flex justify-end relative'
                 style={editMode ? {flexDirection: "column"} : {flexDirection: "row"}}>
                {!editMode ?
                    <div className='flex gap-2 justify-end'>
                        <div className='text-main_red hover:text-red-500 cursor-pointer'
                             onClick={() => setEditMode(!editMode)}>
                            <FontAwesomeIcon icon={faPencil}/>
                        </div>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={handleDeleteDocument}>
                            <FontAwesomeIcon icon={faTrashCan}/>
                        </div>
                    </div>
                    :
                    <div className='flex gap-2 justify-end p-3 absolute -top-7 w-full'>
                        <span className='font-bold w-[89%]'>Edytuj dokument</span>
                        <div className='text-main_grey hover:text-gray-900 cursor-pointer'
                             onClick={() => setEditMode(false)}>
                            <FontAwesomeIcon icon={faReplyAll}/>
                        </div>
                    </div>
                }
                {editMode && <>
                    <DocumentForm toggleReload={props.toggleReload}
                                  toggleShowForm={() => {
                                      setEditMode(false)
                                  }}
                                  mode={Mode.edit}
                                  childId={props.child_id}
                                  document={props.document}
                    />
                </>

                }
            </div>
            {!editMode && <div className="flex flex-col items-center gap-2 pt-3">
                <div className="grid w-full grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-2 gap-y-6">
                    <InfoContainer note={'Sygnatura'} text={props.document.signature}/>
                    <InfoContainer note={'Specyfikacja'} text={props.document.specification}/>
                    <InfoContainer note={'Data'} text={props.document.date}/>
                </div>
                {data &&
                    <div className='w-full mt-4'>
                        <InfoContainer note={'Rodzic powiązany'}
                                       text={`${data.first_name}${data.second_name ? ' ' + data.second_name + ' ' : ' '}${data.surname}`}/>
                    </div>}
                <button
                    className="bg-blue-500 text-white font-semibold py-2 px-4 rounded"
                    onClick={() => {
                        const fileUrl = props.document.file_name; // Replace this with your file URL
                        const headers = {
                            'Authorization': `Bearer ${localStorage.getItem("token")}`
                        };
                        fetch(fileUrl, {
                            headers,
                        }).then(response => {
                            return response.blob();
                        }).then(blob => {
                            const url = window.URL.createObjectURL(new Blob([blob]));
                            const link = document.createElement('a');
                            link.href = url;
                            link.setAttribute('download', 'filename.ext'); // Replace filename.ext with desired filename
                            document.body.appendChild(link);
                            link.click();
                            link.parentNode.removeChild(link);
                        }).catch(error => {
                            console.error('Error downloading file:', error);
                        });
                    }}
                > Pobierz dokument
                </button>
            </div>}
        </div>
    );
}

export default Document;