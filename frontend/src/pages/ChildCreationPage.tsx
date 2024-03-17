import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";

function ChildCreationPage() {
    return (
        <HeightWrapper>
            <Top headerHeight={350}>
                <Header/>
            </Top>
        </HeightWrapper>
    );
}

export default ChildCreationPage;