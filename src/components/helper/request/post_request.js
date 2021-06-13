import appData from "../appData/appData"
import {handleErrors} from "./get_request"



export default function Postreq(url,body,update,set="",){
    update([["loading",true]])
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
            update([["alert",""]])
            setTimeout(()=>{
                var type = "message"
                if(data.status){
                    type = data.status==0?"message":"error"
                }
                update([["alert",data.message],["alertType",type],["loading",false]])
            },5) 
        }
        else{update([["loading",false]])}
    })
    .catch((error)=>{
        update([["alert",""]])
        setTimeout(()=>{
            update([["alert","some error occured please refresh!"],["alertType","error"],["loading",false]])
        },5)
    })
    
}