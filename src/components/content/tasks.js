import { useState,useEffect} from "react"
import "./tasks.css"
import Getreq from "../helper/request/get_request"
import List from "../helper/list/list"
import AddTask from "../helper/addTask/AddTask"
import Loading from "../helper/alert/loading"
import Alert from "../helper/alert/alert"
import {useForceUpdate} from "../helper/alert/alert"


const Tasks = () => {
    const forceUpdate = useForceUpdate();
    const [storage,setStorage] = useState({
        loading: true,
        alert:"",
        alertType:"",
        dataType:""
    })
    const  [type, settype] = useState(0)
    const [data, setdata] = useState({
        tasks:[]
    })

    const updateStorage =(lists)=>{
        var current_state = storage
        for(var i =0 ;i<lists.length;i++){
            current_state[lists[i][0]]=lists[i][1]
        }
        console.log(current_state)
        setStorage(current_state)
    }

    useEffect(() =>setInterval(forceUpdate,10), [])
    useEffect(() => {
        var token="create"
        if(localStorage.getItem("taskToken")!==null) {
            token= localStorage.getItem("taskToken")
        }
        var url = "/todo/get/" + String(type)+"/"+token+"/" ;
        Getreq(url,setdata,updateStorage)
    }, [type]);

    const change =(e)=>{
        setdata({
            tasks:[]
        })
        settype(e.target.value)
    }
    return (
        <>
            <Loading loading={storage.loading}/>
            <Alert alert={storage.alert} update={updateStorage} alertType={storage.alertType} />
            <div className={storage.loading?"any-container content-container loading":"any-container content-container"}>
                <AddTask  update={updateStorage} setdata={setdata} refresh={settype}   type={type} />
                <div id="lisType">
                    <select  onChange={change} >
                        <option id="todo" value={0}>TODO</option>
                        <option value={1}>Complete Task</option>
                    </select> 
                </div>
                <List update={updateStorage} list={data.tasks} setdata={setdata}/>
            </div>
        </>
    );
}

export default Tasks;
