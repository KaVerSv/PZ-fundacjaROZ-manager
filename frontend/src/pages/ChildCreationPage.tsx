import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import ChildCreationForm from "../components/ChildCreationForm/ChildCreationForm.tsx";


function ChildCreationPage() {
    return (
        <HeightWrapper>
            <Top headerHeight={350}>
                <Header/>
            </Top>
            <ChildCreationForm/>
        </HeightWrapper>
    );
}

export default ChildCreationPage;