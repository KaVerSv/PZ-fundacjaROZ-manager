import WidthWrapper from "../../wrappers/WidthWrapper.tsx";

function CurrentBlockHeader() {
    return (
        <div className='flex bg-main_red mt-2'>
            <WidthWrapper>
                <div className='flex items-center justify-between'>
                    <span className='text-main_white'>Obecni wychowankowie</span>
                    <div className='flex items-center gap-1'>
                        <span className='text-main_white text-4xl pb-1'>+</span>
                        <span className='text-main_white'>Dodaj wychowanka</span>
                    </div>
                </div>
            </WidthWrapper>
        </div>
    );
}

export default CurrentBlockHeader;