import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import ChildrenBlock from "../components/ChildrenBlock/ChildrenBlock.tsx";
import CurrentBlockHeader from "../components/ChildrenBlock/childBlockHeaders/CurrentBlockHeader.tsx";
import ArchiveBlockHeader from "../components/ChildrenBlock/childBlockHeaders/ArchiveBlockHeader.tsx";

const Home = () => {
    return (
        <HeightWrapper>
            <Top headerHeight={500}>
                <Header/>
            </Top>
            <ChildrenBlock header={<CurrentBlockHeader/>}/>
            <ChildrenBlock header={<ArchiveBlockHeader/>}/>
        </HeightWrapper>


    );
};

export default Home;