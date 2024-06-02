import {Link} from "react-router-dom";
import {ChildModelMinimized} from "../../models/ChildModelMinimized.tsx";
import {useEffect, useState} from "react";
import photoPath from "/profilowe.png"
import fetchImage from "../../api/fetchImage.ts";

interface ChildProps {
    isArchived: boolean,
    child: ChildModelMinimized
}

// 'src/assets/2.jpg'
function ChildCardMinimized(props: ChildProps) {
    const [imageUrl, setImageUrl] = useState('');
    useEffect(()=>{
        fetchImage(props.child.photo_path).then((url)=>setImageUrl(url));
    },[])
    const optionalStyles = props.isArchived ?
        `bg-main_red hover:bg-red_selected` :
        `bg-main_grey hover:bg-grey_selected`;
    return (
        <Link to={`children/${props.child.id}`}
              className={`flex flex-col gap-2 mx-auto my-2 sm:m-0 max-w-60 max-h-80 rounded-xl hover:cursor-pointer ${optionalStyles}`}>
            <img className='p-3 h-[80%] rounded-full' src={imageUrl? imageUrl : photoPath} alt=''/>
            <span
                className='flex items-center mx-auto text-lg text-main_white'>{props.child.first_name} {props.child.second_name} {props.child.surname}</span>
        </Link>
    );
}

export default ChildCardMinimized;