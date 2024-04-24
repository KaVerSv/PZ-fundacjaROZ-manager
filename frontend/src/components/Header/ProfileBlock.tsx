import {useEffect, useState} from "react";
import {BASE_API_URL} from "../../api/contst.ts";
import { jwtDecode } from "jwt-decode";
import {faArrowRightFromBracket} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {useNavigate} from "react-router-dom";

interface User {
    email: "admin@admin.com";
    first_name: "admin";
    surname: "admin";
}

function ProfileBlock() {
    const [user, setUser] = useState({email: '', first_name: '', surname:''});
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`${BASE_API_URL}/users/${jwtDecode<{user_id: string}>(localStorage.getItem("token"))?.user_id}`, {
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
            <div className='cursor-pointer hover:text-main_red' onClick={()=>{localStorage.removeItem("token"); navigate('/')}}>
                <FontAwesomeIcon icon={faArrowRightFromBracket} size='2xl'/>
            </div>

        </div>
    );
}

export default ProfileBlock;