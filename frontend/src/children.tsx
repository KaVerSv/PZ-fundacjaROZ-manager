import React, { useState, useEffect } from 'react';

const ChildrenComponent: React.FC = () => {
    const [children, setChildren] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/fundacjaROZ/children/');
                if (response.ok) {
                    const data = await response.json();
                    setChildren(data);
                } else {
                    throw new Error('Błąd podczas pobierania danych');
                }
            } catch (error) {
                console.error('Błąd podczas pobierania danych:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <div className="stripe-1">
                Obecni wychowankowie
            </div>
            <div className="children-container"> {/* Dodaj klasę "children-container" */}
                {children.map((child: any) => (
                    <div className="child">
                        <img src={`../public/${child.photo_path}`} alt='profilowe'/>
                        <span>{child.first_name} {child.second_name} {child.surname}</span>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ChildrenComponent;