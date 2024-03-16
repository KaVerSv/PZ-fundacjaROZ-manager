import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import CurrentChildrenBlock from "../components/ChildrenBlock/CurrentChildren/CurrentChildrenBlock.tsx";

const Home = () => {
    return (
        <HeightWrapper>
            <Top>
                <Header/>
            </Top>
            <CurrentChildrenBlock/>
        </HeightWrapper>


    );
};

export default Home;