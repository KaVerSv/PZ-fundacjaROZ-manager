import React from 'react';

function SortingTypeChoice(props: { onSortingMethodChange: (sortingMethod: string) => void, isArch: boolean }) {
    const handleSortBy = (e: React.ChangeEvent<HTMLSelectElement>) => {
        props.onSortingMethodChange(e.target.value);
    };
    return (
        <div className="flex gap-2 relative items-center">
            <span className='text-lg text-main_white'>Sortuj według:</span>
            <select
                onChange={handleSortBy}
                className="appearance-none block min-w-40 w-80 bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                defaultValue={'name'}>
                <option value="name">Imienia(A-Z)</option>
                <option value="nameReversed">Imienia(Z-A)</option>
                <option value="surname">Nazwiska(A-Z)</option>
                <option value="surnameReversed">Nazwiska(Z-A)</option>
                <option value="birthDate">Daty urodzenia(Od najmłodszych)</option>
                <option value="birthDateReversed">Daty urodzenia(Od najstarszych)</option>
                <option value="admissionDate">Daty przyjecia(Od najnowszych)</option>
                <option value="admissionDateReversed">Daty przyjecia(Od najstarszych)</option>
                {props.isArch &&
                    <option value="leavingDate">Daty opuszczenia(Od najnowszych)</option>
                }
                {props.isArch &&
                    <option value="leavingDateReversed">Daty opuszczenia(Od najstarszych)</option>
                }
            </select>
            <div
                className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg"
                     viewBox="0 0 20 20">
                    <path
                        d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                </svg>
            </div>
        </div>
    );
}

export default SortingTypeChoice;