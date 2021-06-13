import React,{ useEffect ,useState} from 'react';
import "./alert.css"


const Alert = (props) => {
    useEffect(() => {
        window.onscroll=()=>{
            props.update([["alert",""]])
        }
    },[])
    if(props.alert){
        return (
            <div  className="alertContainer">
                <div  className={"alert " + props.alertType} id="alert" role="alert">
                    <p>{props.alert}</p>
                </div>
            </div>
        )
    }
    return <></>
}


export function useForceUpdate(){
    const [value, setValue] = useState(0); // integer state
    return () => setValue(value => value + 1); // update the state to force render
}
export default Alert;
