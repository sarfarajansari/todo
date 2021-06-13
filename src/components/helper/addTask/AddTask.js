import {  useState } from "react";
import "./addTask.css"
import Postreq from "../request/post_request"

const AddTask = (props) => {
    const [NewTask, setNewTask] = useState("")
    const AddNewTask=(e)=>{
        e.preventDefault();
        var body = {task:NewTask}
        setNewTask("")
        document.getElementById("todo").selected="selected"
        props.refresh(0)
        Postreq("/todo/post/",body,props.update,props.setdata);

    }
    const handleData =(e)=>{setNewTask(e.target.value)}
    return (
        <form onSubmit={AddNewTask} className="form-container">
            <input autoComplete="off" type="text" required value={NewTask} onChange={handleData} name="task" placeholder="New Task"/>
            <input type="submit" value="Add Task"/>
        </form>
    );
}

export default AddTask;
