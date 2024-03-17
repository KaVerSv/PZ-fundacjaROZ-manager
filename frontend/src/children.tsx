import React, { useState, useEffect } from 'react';

const ChildrenComponent: React.FC = () => {
    const [currentChildren, setCurrentChildren] = useState([]);
    const [archivalChildren, setArchivalChildren] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/fundacjaROZ/children/');
                if (response.ok) {
                    const data = await response.json();
                    setCurrentChildren(data.current_children);
                    setArchivalChildren(data.archival_children);
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
            <div className="children-container">
                {currentChildren.map((child: any) => (
                    <a href={`./child.tsx?pesel=${child.pesel}`}>
                        <div className="child-1">
                            <img src={'./public/profilowe.png'}/>
                            <p>{child.first_name} {child.second_name} {child.surname}</p>
                        </div>
                    </a>
                ))}
            </div>
            <div className="stripe-2">
                Archiwalni wychowankowie
            </div>
            <div className="children-container">
                {archivalChildren.map((child: any) => (
                    <div className="child-2">
                       <img src={'./public/profilowe.png'}/>
                        <p>{child.first_name} {child.second_name} {child.surname}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ChildrenComponent;