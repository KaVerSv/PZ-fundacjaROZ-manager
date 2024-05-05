import WidthWrapper from "../../wrappers/WidthWrapper.tsx";
import SortingTypeChoice from "../SortingTypeChoice.tsx";

function ArchiveBlockHeader(props: {onSortingMethodChange : (sortingMethod: string)=>void;}) {
    return (
        <div className='flex bg-main_grey mt-2 items-center' style={{minHeight: '44px'}}>
            <WidthWrapper>
                <div className='flex items-center justify-between'>
                    <span className='text-main_white'>Archiwalni wychowankowie</span>
                    <SortingTypeChoice isArch={true} onSortingMethodChange={props.onSortingMethodChange}/>
                    <div className="w-64"></div>
                </div>
            </WidthWrapper>
        </div>
    );
}

export default ArchiveBlockHeader;