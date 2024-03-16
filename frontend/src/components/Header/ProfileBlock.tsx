import bell from './assets/dzwon.svg'

function ProfileBlock() {
    return (
        <div className='flex gap-5 mt-3 mb-1 lg:mt-7 lg:mb-5'>
            <span className='flex text-nowrap items-center text-xl'>User Name</span>
            <img className='w-1/6 sm:w-1/5' src={bell} alt={'bell'}/>
        </div>
    );
}

export default ProfileBlock;