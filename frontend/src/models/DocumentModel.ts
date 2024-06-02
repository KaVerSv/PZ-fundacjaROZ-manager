export interface DocumentModel {
    id: string;
    signature: string;
    specification: string;
    date: string | null;
    file_name: string;
    child_id: number | string;
    relative_id: number | null;
    file: File | null;
}