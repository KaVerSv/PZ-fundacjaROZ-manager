import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import ChildrenBlock from "../components/ChildrenBlock/ChildrenBlock.tsx";
import CurrentBlockHeader from "../components/ChildrenBlock/childBlockHeaders/CurrentBlockHeader.tsx";
import ArchiveBlockHeader from "../components/ChildrenBlock/childBlockHeaders/ArchiveBlockHeader.tsx";
import {useEffect, useState} from "react";

const Home = () => {
    useEffect(() => {
        document.title = "Strona głowna";
    }, []);
    const [currentChildrenSortingMethod, setCurrentChildrenSortingMethod] = useState('name');
    const [archivalChildrenSortingMethod, setArchivalChildrenSortingMethod] = useState('name');


    const handleCurrentChildrenSortingMethodChange = (method: string) => {
        setCurrentChildrenSortingMethod(method);
    };

    const handleArchivalChildrenSortingMethodChange = (method: string) => {
        setArchivalChildrenSortingMethod(method);
    };

    return (
        <HeightWrapper>
            <Top headerHeight={300}>
                <Header/>
            </Top>
            <ChildrenBlock sortBy={currentChildrenSortingMethod}
                           header={<CurrentBlockHeader
                               onSortingMethodChange={handleCurrentChildrenSortingMethodChange}/>}/>
            <ChildrenBlock sortBy={archivalChildrenSortingMethod}
                           header={<ArchiveBlockHeader
                               onSortingMethodChange={handleArchivalChildrenSortingMethodChange}/>}/>
        </HeightWrapper>


    );
};

export default Home;