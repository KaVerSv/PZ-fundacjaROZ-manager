import React from 'react';

type props = {
    children: React.ReactNode
}
const WidthWrapper = ({children} : props) => {
    return (
        <div className='container mx-auto ps-2'>
            {children}
        </div>
    );
};

export default WidthWrapper;