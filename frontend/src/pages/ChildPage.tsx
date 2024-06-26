import Top from "../components/Header/Top.tsx";
import Header from "../components/Header/Header.tsx";
import HeightWrapper from "../components/wrappers/HeightWrapper.tsx";
import ChildCardMaximized from "../components/ChildPage/ChildCardMaximized.tsx";
import {useParams} from "react-router-dom";
import NotesSection from "../components/ChildPage/Notes/NotesSection.tsx";
import RelativesSection from "../components/ChildPage/Relatives/RelativesSection.tsx";
import SchoolsSection from "../components/ChildPage/Schools/SchoolsSection.tsx";
import DocumentSection from "../components/ChildPage/Documents/DocumentSection.tsx";

function ChildPage() {
    let {id} = useParams();
    if (!id) id = '0';
    return (
        <HeightWrapper>
            <Top headerHeight={100}>
                <Header/>
            </Top>
            <div className='flex flex-col sm:flex-row justify-center'>
                <div className={`flex flex-col`}>
                    <ChildCardMaximized childId={id}/>
                    <DocumentSection childId={id}/>
                </div>

                <div className='flex flex-col justify-center' style={{alignItems: "center"}}>
                    <SchoolsSection childId={id}/>
                    <NotesSection childId={id}/>
                    <RelativesSection childId={id}/>
                </div>
            </div>
            <div className='mt-96 flex-row'></div>

        </HeightWrapper>
    );
}

export default ChildPage;