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
        update(type, token)
    }, [type]);
    const update= (type,token)=>{
        var url = "/todo/get/" + String(type)+"/"+token+"/" ;
        Getreq(url,setdata)
    }

    const change =(e)=>{
        setdata({
            tasks:[]
        })
        settype(e.target.value)
    }
    const refresh =()=>{
        setdata({
            tasks:[]
        })
        settype(0)
    }
    return (
        <div className="any-container content-container">
            <AddTask refresh={refresh} type={type}  update={update}/>
            <div id="lisType">
                <select  onChange={change} >
                    <option id="todo" value={0}>TODO</option>
                    <option value={1}>Complete Task</option>
                </select> 
            </div>
            <List list={data.tasks} setdata={setdata}  update={update}/>
        </div>
    );
}

export default Tasks;
