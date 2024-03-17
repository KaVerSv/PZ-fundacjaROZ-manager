import React, { useState, useEffect } from 'react';

const ChildComponent: React.FC = () => {
    const [childData, setChildData] = useState<any>({});
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const pesel = urlParams.get('pesel');

        const fetchChildData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/fundacjaROZ/child/?pesel=${pesel}`);
                if (response.ok) {
                    const data = await response.json();
                    setChildData(data);
                    setLoading(false);
                } else {
                    throw new Error('Błąd podczas pobierania danych');
                }
            } catch (error) {
                console.error('Błąd podczas pobierania danych:', error);
                setLoading(false);
            }
        };

        if (pesel) {
            fetchChildData();
        }
    }, []);

    if (loading) {
        return <div>Ładowanie...</div>;
    }

    return (
        <main>
            <div id="left">
                <img src="../public/profilowe.png" alt="profilowe"/>
            </div>

            <div id="right">
                  <div className="form-row">
                    <label>Imię</label>
                    <span>{childData.first_name} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Drugie imię</label>
                    <span>{childData.second_name} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Nazwisko</label>
                    <span>{childData.surname} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Data urodzenia</label>
                    <span>{childData.birth_date} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Miejsce urodzenia</label>
                    <span>{childData.birthplace} </span>
                  </div>
  
                  <div className="form-row">
                    <label>PESEL</label>
                    <span>{childData.pesel} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Adres zamieszkania</label>
                    <span>{childData.residential_address} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Adres zameldowania</label>
                    <span>{childData.registered_address} </span>
                  </div>
  
                  <div className="form-row">
                    <label>Data przyjęcia</label>
                    <span>{childData.admission_date} </span>
                  </div>
            </div>
        </main>
    );
};

export default ChildComponent;