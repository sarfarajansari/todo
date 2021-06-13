import appData from "../appData/appData";


export function handleErrors(response) {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response;
}
export default  function Getreq(url,set,update) {
    update([["loading",true]])
    fetch(appData.url+ url)
    .then(handleErrors)
    .then(response=>response.json())
    .then((data) =>{
        if(data.status==0){
            set(data)
            update([["loading",false]])
            if ("token" in data) {
                localStorage.setItem("taskToken",data.token)
            }
        }
        else{
            update([["alert",""]])
            setTimeout(()=>{
                update([["alert","some error occured please refresh !"],["alertType","error"],["loading",false]])
            },5) 
            if(data.message=="User not found"){
                localStorage.removeItem("taskToken")
            }
        }
    })
    .catch((error)=>{
        update([["alert",""]])
        setTimeout(()=>{
            update([["alert","some error occured please refresh! Please check your internet connection"],["alertType","error"],["loading",false]])
        },5) 
    })
}