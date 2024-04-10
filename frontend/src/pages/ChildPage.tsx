import Top from "../components/Header/Top.tsx";
import Header from "../components/Header/Header.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import ChildCardMaximized from "../components/ChildPage/ChildCardMaximized.tsx";
import {useParams} from "react-router-dom";
import NotesSection from "../components/Notes/NotesSection.tsx";

function ChildPage() {
    let { id } = useParams();
    if(!id) id='0';
    return (
        <HeightWrapper>
            <Top headerHeight={350}>
                <Header/>
            </Top>
            <div className='flex flex-col sm:flex-row justify-center'>
                <ChildCardMaximized childId={id}/>
                <NotesSection/>
            </div>

            <div className='mt-96'></div>
        </HeightWrapper>
    );
}

export default ChildPage;