import Top from "../components/Header/Top.tsx";
import Header from "../components/Header/Header.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import ChildCardMaximized from "../components/ChildPage/ChildCardMaximized.tsx";
import {useParams} from "react-router-dom";
import NotesSection from "../components/ChildPage/Notes/NotesSection.tsx";
import RelativesSection from "../components/ChildPage/Relatives/RelativesSection.tsx";

function ChildPage() {
    let {id} = useParams();
    if (!id) id = '0';
    return (
        <HeightWrapper>
            <Top headerHeight={350}>
                <Header/>
            </Top>
            <div className='flex flex-col sm:flex-row justify-center'>
                <ChildCardMaximized childId={id}/>
                <div className='flex flex-col justify-center' style={{alignItems: "center"}}>
                    <NotesSection childId={id}/>
                    <RelativesSection childId={id}/>
                </div>
            </div>
            <div className='mt-96 flex-row'></div>

        </HeightWrapper>
    );
}

export default ChildPage;