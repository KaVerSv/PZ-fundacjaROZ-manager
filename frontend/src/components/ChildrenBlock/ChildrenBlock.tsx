import ChildCardMinimized from "./ChildCardMinimized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import React from "react";
import CurrentBlockHeader from "./childBlockHeaders/CurrentBlockHeader.tsx";
import useSWR from "swr";
import {ChildModelMinimized} from "../../models/ChildModelMinimized.tsx";
import {BASE_API_URL} from "../../api/contst.ts";
import useAuth from "../../hooks/useAuth.ts";

interface ChildBlockProps {
    header: React.ReactNode
}


function ChildrenBlock(props: ChildBlockProps) {
    const auth = useAuth();
    const fetcher: (url: string) => Promise<ChildModelMinimized[]> = async (url) => {
        const token = auth.auth.token; // Retrieve your JWT token from wherever you store it
        console.log(token);

        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    };

    const {data, error, isLoading} = useSWR<ChildModelMinimized[]>(BASE_API_URL +
        `children/${React.isValidElement(props.header) && props.header.type === CurrentBlockHeader ? 'current/' : 'archival/'}`, fetcher, {refreshInterval:0});

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
                                    key={child.id}
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