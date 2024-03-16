import React from 'react';

type props = {
    children: React.ReactNode
}
const Wrapper = ({children} : props) => {
    return (
        <div className='container mx-auto p-2 min-h-screen'>
            {children}
        </div>
    );
};

export default Wrapper;