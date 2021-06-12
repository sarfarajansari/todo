import React,{ useContext } from 'react';
import {Context} from "../storage/storage"

const Alert = () => {
    const [state,setState] = useContext(Context)
    console.log(state)
    if(state.alert){
        return (
            <div  className={"alert alert-success"} id="msg-alert" role="alert">
                {state.alert}
            </div>
        )
    }
    return <></>
}
export default Alert;
