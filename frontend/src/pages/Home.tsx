import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import ChildrenBlock from "../components/ChildrenBlock/Common/ChildrenBlock.tsx";
import CurrentBlockHeader from "../components/ChildrenBlock/CurrentChildren/CurrentBlockHeader.tsx";
import ArchiveBlockHeader from "../components/ChildrenBlock/ArchiveChildren/ArchiveBlockHeader.tsx";

const Home = () => {
    return (
        <HeightWrapper>
            <Top>
                <Header/>
            </Top>
            <ChildrenBlock header={<CurrentBlockHeader/>}/>
            <ChildrenBlock header={<ArchiveBlockHeader/>}/>
        </HeightWrapper>


    );
};

export default Home;