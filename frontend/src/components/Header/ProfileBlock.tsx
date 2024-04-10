import bell from './assets/dzwon.svg'
import {useEffect, useState} from "react";
import {BASE_API_URL} from "../../api/contst.ts";
import { jwtDecode } from "jwt-decode";

interface User {
    email: "admin@admin.com";
    first_name: "admin";
    surname: "admin";
}

function ProfileBlock() {
    const [user, setUser] = useState({});

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`${BASE_API_URL}/users/${jwtDecode(localStorage.getItem("token"))?.user_id}`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem("token")}`
                    }
                });
                const user: User = await response.json();
                setUser(user);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData();
    }, []);
    return (
        <div className='flex gap-5 mt-3 mb-1 lg:mt-7 lg:mb-5'>
            <span className='flex text-nowrap items-center text-xl'>{user? user.first_name + " " + user.surname : "problem"}</span>
            <img className='w-1/6 sm:w-1/5' src={bell} alt={'bell'}/>
        </div>
    );
}

export default ProfileBlock;