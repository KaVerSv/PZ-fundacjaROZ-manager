import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faFolderPlus} from "@fortawesome/free-solid-svg-icons";
import useSWR from "swr";
import {BASE_API_URL} from "../../../api/contst.ts";
import {useState} from "react";
import DocumentForm from "./DocumentForm.tsx";
import Document from "./Document.tsx";
import {Mode} from "../Mode.ts";
import {DocumentModel} from "../../../models/DocumentModel.ts";

interface NotesBlockProps {
    childId: string
}


function DocumentSection(props: NotesBlockProps) {

    const [showDocumentFrom, setShowDocumentFrom] = useState(false);
    const [isWrapped, setIsWrapped] = useState(true);
    const fetcher: (url: string) => Promise<DocumentModel[]> = async (url) => {

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
    } = useSWR<DocumentModel[]>(`${BASE_API_URL}children/${props.childId}/documents/`, fetcher, {refreshInterval: 0});

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>

    return (
        <div
            className='flex flex-col gap-1.5 border-main_red border-4 rounded-2xl m-2 p-3 sm:mb-auto'>
            <div className='flex flex-row justify-between'>
                <span className='font-bold text-lg'>Dokumenty</span>
                <div className='text-main_red hover:text-red-600 cursor-pointer' onClick={() => {
                    setShowDocumentFrom(!showDocumentFrom)
                }}>
                    <FontAwesomeIcon icon={faFolderPlus}/>
                </div>
            </div>
            <div className='w-full flex justify-center'>
                <div className='w-[80%] border-[1px] border-red-700 rounded-[100%]'></div>
            </div>
            {showDocumentFrom && <div>
                <DocumentForm toggleReload={() => {
                    mutate()
                }}
                              toggleShowForm={() => {
                                  setShowDocumentFrom(false);
                              }} mode={Mode.create} childId={props.childId}/>
            </div>}

            {data.length !== 0 ?
                <div className='flex flex-col gap-5'>
                    <button
                        className="bg-blue-500 text-white font-semibold py-2 px-4 rounded"
                        onClick={() => setIsWrapped(!isWrapped)}
                    > {isWrapped ? 'Rozwiń dokumenty' : 'Zwiń dokumenty'}
                    </button>
                    <div className={`flex flex-col gap-5 overflow-hidden ${
                        isWrapped ? 'max-h-0 absolute' : 'max-h-full'
                    }`}>
                        {data
                            .map((document) => <Document toggleReload={mutate} child_id={props.childId}
                                                         key={document.id} document={document}/>)}
                    </div>
                </div>
                :
                <span className='mx-auto'>Póki co nie ma dokumentów</span>}
        </div>
    );
}

export default DocumentSection;