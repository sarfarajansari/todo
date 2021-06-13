import Postreq from "../request/post_request";
import "./list.css";
import {MdDone} from "react-icons/md"
import {  useContext} from "react";
import {Context} from "../storage/storage"



const Checkbox=(props)=>{
    const [state,setState] = useContext(Context)
    const complete=(e)=>{
        var token = localStorage.getItem("taskToken")
        if(e.target.checked){
            e.target.checked=false
            Postreq("/todo/complete/",{"token":token,"id":props.task.id},props.setdata,props.update,setState,state)
        }
        else{
            document.getElementById(p).style.textDecoration="none"
        }
    }


    const task = props.task
    if(!task.done){
        return(
            <input className="checkbox" type="checkbox" name={"task" + String(task.id)}  onClick={complete}/>
        )
    }
    return <MdDone color="rgb(0, 255, 0)"/>
}
const List = (props) => {
    return (
        <div className="list-container">
            {props.list.map((task,index)=>{
                var ms = (index * 200 ) +(200) -(40 * index);
                if(ms>7000){
                    ms=7000;
                }
                var delay =String(ms)+"ms" ;
                return(
                    <div key={"item" + String(index)} className={"list-item"} style={{animationDuration:delay}}>
                        <div style={{background:"none"}}><Checkbox update={props.update} setdata={props.setdata} task={task} /> </div>
                         <p>{task.task}</p>
                    </div>
                )
            })}
        </div>
    );
}

export default List;
