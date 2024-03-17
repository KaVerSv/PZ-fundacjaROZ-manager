import ChildCardMinimized from "./ChildCardMinimized.tsx";
import WidthWrapper from "../../wrappers/WidthWrapper.tsx";
import React from "react";
import CurrentBlockHeader from "../CurrentChildren/CurrentBlockHeader.tsx";

interface ChildBlockProps {
    header: React.ReactNode
}

function ChildrenBlock(props: ChildBlockProps) {
    return (
        <>
            {props.header}
            <WidthWrapper>
                <div className='mt-3 gap-4 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5'>
                    <ChildCardMinimized
                        isArchived={React.isValidElement(props.header) && props.header.type === CurrentBlockHeader}
                        child={{
                            childName: 'Jan', childSurname: 'Kowalski',
                            childPhotoLink: 'src/components/ChildrenBlock/2.jpg'
                        }}/>
                    <ChildCardMinimized
                        isArchived={React.isValidElement(props.header) && props.header.type === CurrentBlockHeader}
                        child={{
                            childName: 'Jan', childSurname: 'Kowalski',
                            childPhotoLink: 'src/components/ChildrenBlock/2.jpg'
                        }}/>
                    <ChildCardMinimized
                        isArchived={React.isValidElement(props.header) && props.header.type === CurrentBlockHeader}
                        child={{
                            childName: 'Jan', childSurname: 'Kowalski',
                            childPhotoLink: 'src/components/ChildrenBlock/2.jpg'
                        }}/>
                    <ChildCardMinimized
                        isArchived={React.isValidElement(props.header) && props.header.type === CurrentBlockHeader}
                        child={{
                            childName: 'Jan', childSurname: 'Kowalski',
                            childPhotoLink: 'src/components/ChildrenBlock/2.jpg'
                        }}/>

                </div>
            </WidthWrapper>

        </>
    );
}

export default ChildrenBlock;