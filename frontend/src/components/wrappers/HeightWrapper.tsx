import React from 'react';

type props = {
    children: React.ReactNode
}
const HeightWrapper = ({children} : props) => {
    return (
        <div className='min-h-screen'>
            {children}
        </div>
    );
};

export default HeightWrapper;