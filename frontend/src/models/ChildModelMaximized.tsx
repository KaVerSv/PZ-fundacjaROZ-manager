import {GenderEnum} from "./GenderEnum.tsx";

export interface ChildModelMaximized {
    pesel: string;
    firstName: string;
    secondName: string;
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
