import appData from "../appData/appData"
export default async function Getreq(url,set,loaded="") {
    const response = await fetch(appData.url+ url)
    const data = await response.json()
    set(data)
    if(loaded){
        loaded(0)
    }
    if ("token" in data) {
        localStorage.setItem("taskToken",data.token)
    }
    console.log(data)
    return 0
}