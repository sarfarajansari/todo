import appData from "../appData/appData"
import {handleErrors} from "./get_request"



export default function Postreq(url,body,set="",update="",setstate="",state=""){
    body.token =  localStorage.getItem('taskToken')
    var headers = { 'Content-Type': 'application/json' }
    // if (localStorage.getItem('Token') !== null){
    //     headers["Authorization"]="Token " + localStorage.getItem('Token')
    // }
    const requestdata = {
        method: 'POST',
        headers: headers,
        body:JSON.stringify(body)
    }
    fetch(appData.url+ url,requestdata)
    .then(handleErrors)
    .then(response=>response.json())
    .then((data)=>{
        if (set){
            set(data)
        }
        if("message" in data) {
            if(setstate && state){
                var current_state = state;
                current_state.alert ="";
                current_state.alertType ="";
                setstate(current_state)
                setTimeout(()=>{
                    current_state.alert = data.message;
                    if(data.status){
                        current_state.alertType = data.status==0?"message":"error"
                    }
                    else{
                        current_state.alertType="message"
                    }
                    setstate(current_state)
                },5)
            }  
        }
    })
    .catch((error)=>{
        if(setstate && state){
            var current_state = state;
            current_state.alert ="";
            current_state.alertType ="";
            setstate(current_state)
            setTimeout(()=>{
                current_state.alert = "some error occured please refresh!";
                current_state.alertType="error"
                setstate(current_state)
            },5)
        }
    })
}