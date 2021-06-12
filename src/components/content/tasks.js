import { useState,useEffect } from "react"
import "./tasks.css"
import Getreq from "../helper/request/get_request"
import Postreq from "../helper/request/post_request"
import List from "../helper/list/list"
import AddTask from "../helper/addTask/AddTask"


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
    }, [type]);

    const change =(e)=>{
        console.log(e.target.value)
        setdata({
            tasks:[]
        })
        settype(e.target.value)
    }
    return (
        <div className="any-container content-container">
            <AddTask setdata={setdata} refresh={settype}   type={type} />
            <div id="lisType">
                <select  onChange={change} >
                    <option id="todo" value={0}>TODO</option>
                    <option value={1}>Complete Task</option>
                </select> 
            </div>
            <List list={data.tasks} setdata={setdata}/>
        </div>
    );
}

export default Tasks;
