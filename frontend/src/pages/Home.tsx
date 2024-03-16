
import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";

const Home = () => {
    return (
        <HeightWrapper>
            <Top>
                <Header/>
            </Top>
        </HeightWrapper>


    );
};

export default Home;