import { useState } from 'react'
import './add-child.css'

interface FormData {
  pesel: string;
  first_name: string;
  second_name: string;
  surname: string;
  birth_date: string;
  birthplace: string;
  residential_address: string;
  registered_address: string;
  admission_date: string;
  leaving_date: string;
  photo_path: string;
}
const sampleData = {
  "pesel": "00311502873",
  "first_name": "k",
  "second_name": "k",
  "surname": "k",
  "birth_date": "2000-11-15",
  "birthplace": "k",
  "residential_address": "k",
  "registered_address": "k",
  "admission_date": "2024-03-16",
  "leaving_date": "2024-03-28",
  "photo_path": "k"
};

const AddChildForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    pesel: '',
    first_name: 'aaa',
    second_name: 'aaa',
    surname: 'aaa',
    birth_date: '2024-03-06',
    birthplace: '',
    residential_address: 'aaaa',
    registered_address: 'sss',
    admission_date: '2024-03-06',
    leaving_date: '2024-03-06',
    photo_path: 'nie_puste'
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
        const response = await fetch('http://localhost:8000/fundacjaROZ/api/add_child/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const responseData = await response.json();
            console.log('Dane wysłane:', responseData);
            console.log('Sukces');
        } else {
            throw new Error('Błąd podczas wysyłania danych');
        }
    } catch (error) {
        console.error('Błąd podczas wysyłania danych:', error);
        console.log('Coś sie zjebało')
    }
};

  return (
        <main>
            <form onSubmit={handleSubmit}>
                <div id="left">
                  <img src="../public/profilowe.png" alt="profilowe"/>

                  <input type="file" name="newImage"/>
                </div>
                <div id="right">
                  <div className="form-row">
                    <label htmlFor="firstName">Imię</label>
                    <input type="text" name="firstName" value={formData.first_name} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="secondName">Drugie imię</label>
                    <input type="text" name="secondName" value={formData.second_name} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="surname">Nazwisko</label>
                    <input type="text" name="surname" value={formData.surname} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="birthDate">Data urodzenia</label>
                    <input type="date" name="birthDate" value={formData.birth_date} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="birthplace">Miejsce urodzenia</label>
                    <input type="text" name="birthplace" value={formData.birthplace} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="pesel">PESEL</label>
                    <input type="text" name="pesel" value={formData.pesel} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="residentalAddress">Adres zamieszkania</label>
                    <input type="text" name="residentalAddress" value={formData.residential_address} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="registeredAddress">Adres zameldowania</label>
                    <input type="text" name="registeredAddress" value={formData.registered_address} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="admissionDate">Data przyjęcia</label>
                    <input type="date" name="admissionDate" value={formData.admission_date} onChange={handleChange} />
                  </div>

                  <div className="form-row">
                    <button type="submit">Odrzuć zmiany</button>
                  </div>
                
                  <div className="form-row">
                    <button type="submit">Zapisz zmiany</button>
                  </div>
                </div>
            </form>
        </main>
  );
};

export default AddChildForm;