import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import ChildCreationForm from "../components/ChildCreationForm/ChildCreationForm.tsx";
import {useEffect} from "react";


function ChildCreationPage() {

    useEffect(() => {
        document.title = "Dodaj wychowanka";
    }, []);
    return (
        <HeightWrapper>
            <Top headerHeight={100}>
                <Header/>
            </Top>
            <ChildCreationForm/>
            <div className='mt-96'></div>
        </HeightWrapper>
    );
}

export default ChildCreationPage;