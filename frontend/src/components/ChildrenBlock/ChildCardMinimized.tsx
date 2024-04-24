import {ChildModelMinimized} from "../../models/ChildModelMinimized.tsx";
import {Link} from "react-router-dom";

interface ChildProps {
    isArchived: boolean,
    child: ChildModelMinimized
}

// 'src/assets/2.jpg'
function ChildCardMinimized(props: ChildProps) {
    let optionalStyles = props.isArchived ?
        `bg-main_red hover:bg-red_selected` :
        `bg-main_grey hover:bg-grey_selected`;
    return (
        <Link to={`children/${props.child.id}`} className={`mx-auto my-2 sm:m-0 flex max-w-72 h-16 rounded-xl hover:cursor-pointer ${optionalStyles}`}>
            <img className='ml-5 p-0.5 rounded-full' src={props.child.childPhotoLink}/>
            <span
                className='flex items-center ml-2 text-main_white'>{props.child.childName} {props.child.childLastName} {props.child.childSurname}</span>
        </Link>
    );
}

export default ChildCardMinimized;