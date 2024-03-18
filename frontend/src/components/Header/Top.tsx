import React from 'react';
type props = {
    children: React.ReactNode
    headerHeight: number
}
function Top({children, headerHeight} : props) {
    return (
        <div
            className="bg-cover bg-no-repeat bg-center bg-clip-border bg-[url('src/components/Header/assets/ROZ_background_Top.jpeg')]"
            style={{paddingBottom: `${headerHeight}px`, backgroundPosition: 'center -80px'}}>
            {children}
        </div>
    );
}

export default Top;