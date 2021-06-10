import appData from "../appData/appData"
export default function Postreq(url,body,set="",loaded=""){
    body.token =  localStorage.getItem('taskToken')
    var headers = { 'Content-Type': 'application/json' }
    if (localStorage.getItem('Token') !== null){
        headers["Authorization"]="Token " + localStorage.getItem('Token')
    }
    const requestdata = {
        method: 'POST',
        headers: headers,
        body:JSON.stringify(body)
    }
    fetch(appData.url+ url,requestdata)
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        if (set){
            set(data)
        }
        if (loaded){
            loaded(0)
        }
    })
}