import React,{ useContext,useEffect ,useState} from 'react';
import {Context} from "../storage/storage"
import "./alert.css"


const Alert = () => {
    const [state,setState] = useContext(Context)
    const forceUpdate = useForceUpdate();
    useEffect(() => {
        window.onscroll=()=>{
            var current_state = state;
            current_state.alert="";
            current_state.alertType="";
            setState(current_state)
        }
        setInterval(forceUpdate,10)
    },[])
    if(state.alert){
        return (
            <div  className={"alert " + state.alertType} id="alert" role="alert">
                <p>{state.alert}</p>
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
