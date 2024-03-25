import ChildCardMinimized from "./ChildCardMinimized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import React from "react";
import CurrentBlockHeader from "./childBlockHeaders/CurrentBlockHeader.tsx";
import {ChildModelMinimized} from "../../models/ChildModelMinimized.tsx";

interface ChildBlockProps {
    header: React.ReactNode
}

export const currentChildren: ChildModelMinimized[] = [
    {
        id: "1",
        childName: "Alice",
        childLastName: "Smith",
        childSurname: "Johnson",
        childPhotoLink: 'src/assets/2.jpg'
    },
    {
        id: "2",
        childName: "Bob",
        childLastName: "Brown",
        childSurname: "Miller",
        childPhotoLink: 'src/assets/2.jpg'
    },
    {
        id: "3",
        childName: "Charlie",
        childLastName: "Jones",
        childSurname: "Williams",
        childPhotoLink: 'src/assets/2.jpg'
    },
    {
        id: "4",
        childName: "Emma",
        childLastName: "Davis",
        childSurname: "Anderson",
        childPhotoLink: 'src/assets/2.jpg'
    },
    {
        id: "5",
        childName: "Finn",
        childLastName: "Wilson",
        childSurname: "Thompson",
        childPhotoLink: 'src/assets/2.jpg'
    },
    {
        id: "6",
        childName: "Grace",
        childLastName: "Taylor",
        childSurname: "Harris",
        childPhotoLink: 'src/assets/2.jpg'
    },
];

function ChildrenBlock(props: ChildBlockProps) {
    return (
        <>
            {props.header}
            <WidthWrapper>
                <div className='mt-3 gap-4 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5'>
                    {
                        currentChildren.map(
                            child =>
                                <ChildCardMinimized
                                    key = {child.id}
                                    isArchived={React.isValidElement(props.header) && props.header.type === CurrentBlockHeader}
                                    child={{
                                        childName: child.childName,
                                        childSurname: child.childSurname,
                                        childLastName: child.childLastName,
                                        id: child.id,
                                        childPhotoLink: child.childPhotoLink
                                    }}/>
                        )
                    }
                </div>
            </WidthWrapper>

        </>
    );
}

export default ChildrenBlock;