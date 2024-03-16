import { useState } from 'react'
import './add-child.css'

interface FormData {
  pesel: string;
  firstName: string;
  secondName: string;
  surname: string;
  birthDate: string;
  birthplace: string;
  residentialAddress: string;
  registeredAddress: string;
  admissionDate: string;
  leavingDate: string;
  photoPath: string;
}

const AddChildForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    pesel: '',
    firstName: '',
    secondName: '',
    surname: '',
    birthDate: '',
    birthplace: '',
    residentialAddress: '',
    registeredAddress: '',
    admissionDate: '',
    leavingDate: '',
    photoPath: ''
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
        const response = await fetch('http://localhost:8000/fundacjaROZ/add-child/', {
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
                    <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="secondName">Drugie imię</label>
                    <input type="text" name="secondName" value={formData.secondName} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="surname">Nazwisko</label>
                    <input type="text" name="surname" value={formData.surname} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="birthDate">Data urodzenia</label>
                    <input type="date" name="birthDate" value={formData.birthDate} onChange={handleChange} />
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
                    <input type="text" name="residentalAddress" value={formData.residentialAddress} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="registeredAddress">Adres zameldowania</label>
                    <input type="text" name="registeredAddress" value={formData.registeredAddress} onChange={handleChange} />
                  </div>
  
                  <div className="form-row">
                    <label htmlFor="admissionDate">Data przyjęcia</label>
                    <input type="date" name="admissionDate" value={formData.admissionDate} onChange={handleChange} />
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