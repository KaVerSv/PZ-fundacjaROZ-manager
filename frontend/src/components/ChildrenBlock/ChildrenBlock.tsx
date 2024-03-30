import ChildCardMinimized from "./ChildCardMinimized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import React from "react";
import CurrentBlockHeader from "./childBlockHeaders/CurrentBlockHeader.tsx";
import useSWR from "swr";
import {ChildModelMinimized} from "../../models/ChildModelMinimized.tsx";
import {BASE_API_URL} from "../../api/contst.ts";

interface ChildBlockProps {
    header: React.ReactNode
}

/*
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
*/

function ChildrenBlock(props: ChildBlockProps) {
    const fetcher: (url: string) => Promise<ChildModelMinimized[]> = async (url) => {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    };
    const { data, error, isLoading } = useSWR<ChildModelMinimized[]>(BASE_API_URL +
        `/children/${React.isValidElement(props.header) && props.header.type === CurrentBlockHeader ? 'archival/' : 'current/'}`, fetcher);
    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>
    return (
        <>
            {props.header}
            <WidthWrapper>
                <div className='mt-3 gap-4 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5'>
                    {
                        data.map(
                            child =>
                                <ChildCardMinimized
                                    key = {child.id}
                                    isArchived={React.isValidElement(props.header) && props.header.type === CurrentBlockHeader}
                                    child={child}/>
                        )
                    }
                </div>
            </WidthWrapper>

        </>
    );
}

export default ChildrenBlock;