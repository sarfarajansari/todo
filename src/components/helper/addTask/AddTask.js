import {  useState , useContext} from "react";
import "./addTask.css"
import Postreq from "../request/post_request"
import {Context} from "../storage/storage"

const AddTask = (props) => {
    const [state,setState] = useContext(Context)
    const [NewTask, setNewTask] = useState("")
    const AddNewTask=(e)=>{
        e.preventDefault();
        var body = {
            task:NewTask
        }
        setNewTask("")
        document.getElementById("todo").selected="selected"
        props.refresh(0)
        Postreq("/todo/post/",body,props.setdata,false,setState,state);

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
