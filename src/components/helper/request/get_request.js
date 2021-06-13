import appData from "../appData/appData";


export function handleErrors(response) {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response;
}
export default  function Getreq(url,set,updateStorage="",setstate="",state="") {
    fetch(appData.url+ url)
    .then(handleErrors)
    .then(response=>response.json())
    .then((data) =>{
        if(data.status==0){
            set(data)
            if ("token" in data) {
                localStorage.setItem("taskToken",data.token)
            }
        }
        else{
            if(data.message=="User not found"){
                localStorage.removeItem("taskToken")
                if(setstate && state){
                    var current_state = state;
                    current_state.alert ="";
                    current_state.alertType ="";
                    setstate(current_state)
                    setTimeout(()=>{
                        current_state.alert = "some error occured please refresh !";
                        current_state.alertType="error"
                        setstate(current_state)
                    },5)
                }
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
    if(updateStorage){
        updateStorage([["loading",false]])
    }
}