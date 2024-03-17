import WidthWrapper from "../../wrappers/WidthWrapper.tsx";

function ArchiveBlockHeader() {
    return (
        <div className='flex bg-main_grey mt-2 items-center' style={{minHeight: '44px'}}>
            <WidthWrapper>
                <div className='flex items-center justify-between'>
                    <span className='text-main_white'>Archiwalni wychowankowie</span>
                </div>
            </WidthWrapper>
        </div>
    );
}

export default ArchiveBlockHeader;