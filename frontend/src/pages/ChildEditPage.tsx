import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import Header from "../components/Header/Header.tsx";
import Top from "../components/Header/Top.tsx";
import ChildCreationForm from "../components/ChildCreationForm/ChildCreationForm.tsx";
import {useParams} from "react-router-dom";


function ChildEditPage() {
    let { id } = useParams();
    if(!id) id='0';
    return (
        <HeightWrapper>
            <Top headerHeight={350}>
                <Header/>
            </Top>
            <ChildCreationForm editMode={true} childId={id}/>
            <div className='mt-96'></div>
        </HeightWrapper>
    );
}

export default ChildEditPage;