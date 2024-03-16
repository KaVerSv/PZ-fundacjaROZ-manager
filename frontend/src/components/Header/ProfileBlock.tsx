import React from 'react';
import bell from './assets/dzwon.svg'

function ProfileBlock() {
    return (
        <div className='flex gap-5'>
            <span className='flex text-nowrap items-center text-xl'>User Name</span>
            <img className='sm:w-1/12' src={bell} alt={'bell'}/>
        </div>
    );
}

export default ProfileBlock;