import React from 'react';
type props = {
    children: React.ReactNode
}
function Top({children} : props) {
    return (
        <div className="bg-[url('src/components/Header/assets/ROZ_background_Top.jpeg')] bg-cover bg-center bg-clip-border" style={{paddingBottom:'500px', backgroundPosition:'center 0px'}}>
            {children}
        </div>
    );
}

export default Top;