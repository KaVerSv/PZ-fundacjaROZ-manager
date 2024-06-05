import ChildCardMinimized from "./ChildCardMinimized.tsx";
import WidthWrapper from "../wrappers/WidthWrapper.tsx";
import React from "react";
import CurrentBlockHeader from "./childBlockHeaders/CurrentBlockHeader.tsx";
import useSWR from "swr";
import {ChildModelMinimized} from "../../models/ChildModelMinimized.tsx";
import {BASE_API_URL} from "../../api/contst.ts";

interface ChildBlockProps {
    header: React.ReactNode;
    sortBy: string;
}


function ChildrenBlock(props: ChildBlockProps) {
    let currentSortingFn: (a: ChildModelMinimized, b: ChildModelMinimized) => number;
    switch (props.sortBy) {
        case "name": {
            currentSortingFn = (a, b) => a.first_name.localeCompare(b.first_name);
            break;
        }
        case "nameReversed": {
            currentSortingFn = (a, b) => b.first_name.localeCompare(a.first_name);
            break;
        }
        case "surname": {
            currentSortingFn = (a, b) => a.surname.localeCompare(b.surname);
            break;
        }
        case "surnameReversed": {
            currentSortingFn = (a, b) => b.surname.localeCompare(a.surname);
            break;
        }
        case "birthDate": {
            currentSortingFn = (a, b) => +new Date(a.birth_date) - +new Date(b.birth_date);
            break;
        }
        case "birthDateReversed": {
            currentSortingFn = (a, b) => +new Date(b.birth_date) - +new Date(a.birth_date);
            break;
        }
        case "admissionDate": {
            currentSortingFn = (a, b) => +new Date(a.admission_date) - +new Date(b.admission_date);
            break;
        }
        case "admissionDateReversed": {
            currentSortingFn = (a, b) => +new Date(b.admission_date) - +new Date(a.admission_date);
            break;
        }
        case "leavingDate": {
            currentSortingFn = (a, b) => +new Date(a.leaving_date) - +new Date(b.leaving_date);
            break;
        }
        case "leavingDateReversed": {
            currentSortingFn = (a, b) => +new Date(b.leaving_date) - +new Date(a.leaving_date);
            break;
        }
    }
    const fetcher: (url: string) => Promise<ChildModelMinimized[]> = async (url) => {
        const token = localStorage.getItem("token");

        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }
        return response.json();
    };

    const {data, error, isLoading} = useSWR<ChildModelMinimized[]>(BASE_API_URL +
        `children/${React.isValidElement(props.header) && props.header.type === CurrentBlockHeader ? 'current/' : 'archival/'}`, fetcher, {refreshInterval: 0});

    if (error) return <div>failed to load</div>
    if (isLoading) return <div>loading...</div>
    return (
        <>
            {props.header}
            <WidthWrapper>
                <div className='mt-3 gap-4 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5'>
                    {
                        data.sort((a, b) => currentSortingFn(a, b))
                            .map(
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