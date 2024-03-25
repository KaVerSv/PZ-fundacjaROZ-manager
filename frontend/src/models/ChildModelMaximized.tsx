import {GenderEnum} from "./GenderEnum.tsx";
import image from '../assets/2.jpg'

export interface ChildModelMaximized {
    id: string
    pesel: string;
    firstName: string;
    secondName?: string;
    surname: string;
    birthDate: string;
    birthPlace: string;
    residentialAddress: string;
    registeredAddress: string;
    admissionDate: string;
    leavingDate: string;
    photoPath: string;
    gender: GenderEnum;
}

export var currentChildrenFull: ChildModelMaximized[] = [
    {
        id: "1",
        pesel: "12345678901",
        firstName: "Alice",
        secondName: '',
        surname: "Smith Johnson",
        birthDate: "2005-02-10",
        birthPlace: "Cityville",
        residentialAddress: "123 Main St, Cityville",
        registeredAddress: "123 Main St, Cityville",
        admissionDate: "2010-09-01",
        leavingDate: "2022-05-15",
        photoPath: image,
        gender: GenderEnum.female
    },
    {
        id: "2",
        pesel: "23456789012",
        firstName: "Bob",
        secondName: '',
        surname: "Brown Miller",
        birthDate: "2006-04-15",
        birthPlace: "Townsville",
        residentialAddress: "456 Oak St, Townsville",
        registeredAddress: "456 Oak St, Townsville",
        admissionDate: "2011-03-20",
        leavingDate: "2023-08-10",
        photoPath: image,
        gender: GenderEnum.male
    },
    {
        id: "3",
        pesel: "34567890123",
        firstName: "Charlie",
        secondName: '',
        surname: "Jones Williams",
        birthDate: "2007-08-20",
        birthPlace: "Villagetown",
        residentialAddress: "789 Elm St, Villagetown",
        registeredAddress: "789 Elm St, Villagetown",
        admissionDate: "2012-11-05",
        leavingDate: "2024-02-28",
        photoPath: image,
        gender: GenderEnum.male
    },
    {
        id: "4",
        pesel: "45678901234",
        firstName: "Emma",
        secondName: '',
        surname: "Davis Anderson",
        birthDate: "2008-12-05",
        birthPlace: "Hamletsville",
        residentialAddress: "567 Maple St, Hamletsville",
        registeredAddress: "567 Maple St, Hamletsville",
        admissionDate: "2013-07-10",
        leavingDate: "2025-01-20",
        photoPath: image,
        gender: GenderEnum.female
    },
    {
        id: "5",
        pesel: "56789012345",
        firstName: "Finn",
        secondName: '',
        surname: "Wilson Thompson",
        birthDate: "2009-10-30",
        birthPlace: "Ruraltown",
        residentialAddress: "890 Pine St, Ruraltown",
        registeredAddress: "890 Pine St, Ruraltown",
        admissionDate: "2014-04-15",
        leavingDate: "2026-03-12",
        photoPath: image,
        gender: GenderEnum.male
    },
    {
        id: "6",
        pesel: "67890123456",
        firstName: "Grace",
        secondName: '',
        surname: "Taylor Harris",
        birthDate: "2010-03-25",
        birthPlace: "Suburbia",
        residentialAddress: "901 Cedar St, Suburbia",
        registeredAddress: "901 Cedar St, Suburbia",
        admissionDate: "2015-09-08",
        leavingDate: "2027-04-22",
        photoPath: image,
        gender: GenderEnum.female
    },
];