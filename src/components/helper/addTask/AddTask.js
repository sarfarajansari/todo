import { useState } from "react";
import "./addTask.css"
import Postreq from "../request/post_request"
const AddTask = (props) => {
    const [NewTask, setNewTask] = useState("")
    const AddNewTask=(e)=>{
        e.preventDefault();
        var body = {
            task:NewTask
        }
        Postreq("/todo/post/",body)
        setTimeout(()=>{
            document.getElementById("todo").selected="selected"
            if(props.type===1){
                props.refresh()
            }
            else{
            props.update(0,localStorage.getItem("taskToken"))
            }
            setNewTask("")
        },100)

    }
    const handleData =(e)=>{setNewTask(e.target.value)}
    return (
        <form onSubmit={AddNewTask} className="form-container">
            <input type="text" required value={NewTask} onChange={handleData} name="task" placeholder="New Task"/>
            <input type="submit" value="Add Task"/>
        </form>
    );
}

export default AddTask;
