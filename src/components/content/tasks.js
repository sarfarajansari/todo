import { useState,useEffect } from "react"
import "./tasks.css"
import Getreq from "../helper/request/get_request"
import Postreq from "../helper/request/post_request"
import List from "../helper/list/list"


const Tasks = () => {
    const  [type, settype] = useState(0)
    const [data, setdata] = useState({
        tasks:[]
    })
    useEffect(() => {
        var token="create"
        if(localStorage.getItem("taskToken")!==null) {
            token= localStorage.getItem("taskToken")
        }
        var url = "/todo/get/" + String(type)+"/"+token+"/" ;
        Getreq(url,setdata)
    }, []);
    
    return (
        <div className="any-container">
            <List list={data.tasks} setdata={setdata}/>
        </div>
    );
}

export default Tasks;
